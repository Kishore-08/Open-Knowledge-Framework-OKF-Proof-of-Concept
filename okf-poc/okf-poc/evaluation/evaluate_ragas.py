import json
import os
from datetime import datetime
import pandas as pd
from datasets import Dataset
 
# Ragas 0.1.9-compatible metrics (lowercase singleton instances from ragas.metrics).
# NOTE: `response_relevancy` does not exist in ragas 0.1.x - the metric is named
# `answer_relevancy`. Similarly, `ragas.metrics.collections` only exists in
# ragas 0.3+ and exports *classes* there, not instances.
from ragas.metrics import (
    faithfulness,
    answer_correctness,
    context_precision,
    context_recall,
    answer_relevancy,
)
 
# LangChain integrations used by Ragas 0.1.9 for the judge LLM + embeddings.
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_core.outputs import ChatResult, ChatGeneration
from langchain_core.messages import BaseMessage
from typing import Any, Dict, List, Optional, Sequence
 
from ragas import evaluate
 
# Import our consolidated OKF answer engine from the core app
from app.query.engine import generate_answer
 
 
class RagasCompatibleChatGoogleGenerativeAI(ChatGoogleGenerativeAI):
    """
    Adapter that makes ChatGoogleGenerativeAI callable by Ragas 0.1.9.
 
    Ragas 0.1.9's `LangchainLLMWrapper` invokes
    `generate_prompt(prompts=..., temperature=temperature, stop=..., ...)`.
    In langchain-google-genai 1.0.10 that `temperature` kwarg is forwarded
    verbatim into `client.generate_content()` (which does not accept it),
    raising `TypeError: ... unexpected keyword argument 'temperature'`.
 
    This subclass intercepts `_generate`/`_agenerate`, folds `temperature`
    into the `generation_config` dict (where the underlying SDK expects it)
    and discards the extra kwarg instead of forwarding it to the client.
    """
 
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Any = None,
        *,
        generation_config: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> ChatResult:
        temperature = kwargs.pop("temperature", None)
        if temperature is not None:
            generation_config = dict(generation_config or {})
            generation_config["temperature"] = temperature
        return super()._generate(
            messages,
            stop=stop,
            run_manager=run_manager,
            generation_config=generation_config,
            **kwargs,
        )
 
    async def _agenerate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Any = None,
        *,
        generation_config: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> ChatResult:
        temperature = kwargs.pop("temperature", None)
        if temperature is not None:
            generation_config = dict(generation_config or {})
            generation_config["temperature"] = temperature
        return await super()._agenerate(
            messages,
            stop=stop,
            run_manager=run_manager,
            generation_config=generation_config,
            **kwargs,
        )
 
 
def _eval_model_name() -> str:
    """Return the judge LLM model, overridable via the GEMINI_EVAL_MODEL env var."""
    return os.getenv("GEMINI_EVAL_MODEL", "gemini-3.5-flash")
 
 
def _eval_embedding_model_name() -> str:
    """Return the embedding model used by the judge (for correctness/relevancy)."""
    return os.getenv("GEMINI_EVAL_EMBEDDING_MODEL", "models/gemini-embedding-001")
 
 
def load_dataset(filepath: str) -> list:
    """Loads the 20-question evaluation dataset."""
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["questions"]
 
 
def citation_quality(answer: str, sources: list) -> dict:
    """
    Deterministic citation-quality proxy (no extra LLM judge call).
 
    A well-grounded OKF answer must cite the retrieved evidence. For each source
    we check:
 
    * citable    - the source carries both a `title` and a `source_url`
      (the fields the query engine ships to the LLM as the citation line),
    * cited      - the answer text actually mentions that title or URL.
 
    Returns the per-question sub-scores; the overall `citation_score` is the
    fraction of citable sources that the answer visibly cited. This is a
    grounding/attribution proxy - it measures whether the answer points at its
    evidence, not whether the evidence was used verbatim.
    """
    if not sources:
        return {
            "source_count": 0,
            "citable_sources": 0,
            "cited_in_answer": 0,
            "citation_score": 0.0,
            "source_completeness": 0.0,
        }
 
    citable = [
        s
        for s in sources
        if (s.get("title") or "").strip() and (s.get("source_url") or "").strip()
    ]
 
    if not citable:
        return {
            "source_count": len(sources),
            "citable_sources": 0,
            "cited_in_answer": 0,
            "citation_score": 0.0,
            "source_completeness": 0.0,
        }
 
    answer_lower = (answer or "").lower()
    cited = 0
    for s in citable:
        title = (s.get("title") or "").strip().lower()
        url = (s.get("source_url") or "").strip().lower()
        if title and title in answer_lower:
            cited += 1
        elif url and url in answer_lower:
            cited += 1
 
    return {
        "source_count": len(sources),
        "citable_sources": len(citable),
        "cited_in_answer": cited,
        "citation_score": cited / len(citable),
        "source_completeness": len(citable) / len(sources),
    }
 
 
def document_observations(results: list) -> dict:
    """
    Aggregate per-document (source) observations across all evaluated questions.
 
    Tracks, per distinct retrieved source:
      * times_retrieved - in how many questions this document was retrieved,
      * times_cited     - in how many of those answers the document was cited,
      * categories      - the set of OKF categories the document was tagged with.
 
    Returns a dict keyed by source URL (or title when URL is missing).
    """
    docs: dict = {}
    for res in results:
        for s in res["sources"]:
            key = s.get("source_url") or s.get("title") or s.get("id") or "unknown"
            entry = docs.setdefault(
                key,
                {
                    "title": s.get("title"),
                    "source_url": s.get("source_url"),
                    "category": s.get("category"),
                    "times_retrieved": 0,
                    "times_cited": 0,
                },
            )
            entry["times_retrieved"] += 1
            answer_lower = (res["answer"] or "").lower()
            title = (s.get("title") or "").strip().lower()
            url = (s.get("source_url") or "").strip().lower()
            if (title and title in answer_lower) or (url and url in answer_lower):
                entry["times_cited"] += 1
    return docs
 
 
def run_evaluation():
    """
    Executes the 20 questions against our OKF PoC pipeline, formats the results
    for the Ragas framework, and calculates performance metrics.
    """
    print("Starting OKF Pipeline Evaluation using Ragas...")
 
    # 1. Load the dataset
    dataset_path = "evaluation/dataset.json"
    if not os.path.exists(dataset_path):
        print(f"Error: Dataset not found at {dataset_path}")
        return
 
    questions_data = load_dataset(dataset_path)
 
    # Data structures required by Ragas (plus the citation-quality columns we
    # keep alongside for evidence in the results CSV/JSON).
    data = {
        "question": [],
        "answer": [],
        "contexts": [],
        "ground_truth": [],
        "citation_score": [],
        "source_count": [],
        "citable_sources": [],
        "cited_in_answer": [],
        "citation_sources": [],
    }
 
    print(f"Querying {len(questions_data)} questions. This may take a few minutes...")
 
    # 2. Run inferences
    raw_results = []
    for i, item in enumerate(questions_data):
        q = item["question"]
        gt = item["ground_truth"]
 
        print(f"   [{i+1}/{len(questions_data)}] Querying: {q}")
 
        result = generate_answer(q)
 
        # Extract the actual answer text
        answer = result.answer
 
        # Extract the source chunks (contexts) used by the LLM
        contexts = [
            s.get("snippet") or s.get("description") or ""
            for s in result.sources
        ]
 
        # Citation-quality evidence: which sources were citable and did the
        # answer actually cite them?
        citation = citation_quality(answer, result.sources)
 
        # Append to our dataset
        data["question"].append(q)
        data["answer"].append(answer)
        data["contexts"].append(contexts)
        data["ground_truth"].append(gt)
        data["citation_score"].append(citation["citation_score"])
        data["source_count"].append(citation["source_count"])
        data["citable_sources"].append(citation["citable_sources"])
        data["cited_in_answer"].append(citation["cited_in_answer"])
        data["citation_sources"].append(
            [
                {
                    "title": s.get("title"),
                    "source_url": s.get("source_url"),
                    "score": s.get("score"),
                }
                for s in result.sources
            ]
        )
 
        raw_results.append(
            {
                "question": q,
                "answer": answer,
                "sources": [
                    {
                        "title": s.get("title"),
                        "source_url": s.get("source_url"),
                        "category": s.get("category"),
                        "score": s.get("score"),
                    }
                    for s in result.sources
                ],
            }
        )
 
    # 3. Convert to HuggingFace Dataset format (required by Ragas)
    hf_dataset = Dataset.from_dict(data)
 
    # 4. Evaluate
    print("\nRunning Ragas metrics (Faithfulness, Correctness, Precision, Recall, Relevance)...")
 
    metrics = [
        faithfulness,       # Hallucination proxy: fraction of answer claims grounded in context.
        answer_correctness, # Accuracy of the answer against the ground truth.
        context_precision,  # Retrieval quality: relevant OKF chunks ranked at the top.
        context_recall,     # Retrieval quality: ground-truth facts covered by retrieved chunks.
        answer_relevancy,   # Retrieval quality: retrieved OKF chunks pertain to the question.
    ]
 
    llm = RagasCompatibleChatGoogleGenerativeAI(
        model=_eval_model_name(),
        google_api_key=os.getenv("GEMINI_API_KEY"),
        temperature=0,
    )
    embeddings = GoogleGenerativeAIEmbeddings(
        model=_eval_embedding_model_name(),
        google_api_key=os.getenv("GEMINI_API_KEY"),
    )
 
    result = evaluate(
        dataset=hf_dataset,
        metrics=metrics,
        llm=llm,
        embeddings=embeddings,
    )
 
    # 5. Save Results
    os.makedirs("evaluation/results", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
 
    # Save raw DataFrame to CSV for detailed inspection
    df = result.to_pandas()
    csv_path = f"evaluation/results/evaluation_details_{timestamp}.csv"
    df.to_csv(csv_path, index=False)
 
    # Aggregate per-document observations across the whole run.
    doc_obs = document_observations(raw_results)
    hallucination_rate = 1.0 - df["faithfulness"].mean() if "faithfulness" in df else 0.0
 
    # Calculate overall averages to determine if we hit the >80% success requirement
    summary = {
        "timestamp": timestamp,
        "model": _eval_model_name(),
        "embedding_model": _eval_embedding_model_name(),
        "total_questions": len(questions_data),
        "overall_scores": {
            "faithfulness_score": df["faithfulness"].mean(),
            "hallucination_rate": hallucination_rate,
            "answer_correctness_score": df["answer_correctness"].mean(),
            "context_precision_score": df["context_precision"].mean(),
            "context_recall_score": df["context_recall"].mean(),
            "answer_relevancy_score": df["answer_relevancy"].mean(),
            "citation_quality_score": df["citation_score"].mean(),
            "average_cited_sources": df["cited_in_answer"].mean(),
            "average_citable_sources": df["citable_sources"].mean(),
        },
        "retrieval_quality": {
            "context_precision_score": df["context_precision"].mean(),
            "context_recall_score": df["context_recall"].mean(),
            "answer_relevancy_score": df["answer_relevancy"].mean(),
        },
        "answer_correctness": {
            "answer_correctness_score": df["answer_correctness"].mean(),
        },
        "hallucination": {
            "faithfulness_score": df["faithfulness"].mean(),
            "hallucination_rate": hallucination_rate,
        },
        "source_citation_quality": {
            "citation_quality_score": df["citation_score"].mean(),
            "average_cited_sources": df["cited_in_answer"].mean(),
            "average_citable_sources": df["citable_sources"].mean(),
        },
        "document_observations": doc_obs,
        "success_rate_estimate": df["answer_correctness"].mean() * 100
    }
 
    json_path = f"evaluation/results/evaluation_summary_{timestamp}.json"
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=4)
 
    print("\nEvaluation Complete!")
    print(f"   Detailed CSV saved to: {csv_path}")
    print(f"   Summary JSON saved to: {json_path}")
    print("\n--- PERFORMANCE SUMMARY ---")
    print(f"   Model: {summary['model']}")
    print(f"   Faithfulness (Anti-Hallucination): {summary['overall_scores']['faithfulness_score']:.2f}")
    print(f"   Hallucination Rate: {summary['overall_scores']['hallucination_rate']:.2f}")
    print(f"   Answer Correctness: {summary['overall_scores']['answer_correctness_score']:.2f}")
    print(f"   Retrieval Precision: {summary['overall_scores']['context_precision_score']:.2f}")
    print(f"   Retrieval Recall: {summary['overall_scores']['context_recall_score']:.2f}")
    print(f"   Answer Relevancy: {summary['overall_scores']['answer_relevancy_score']:.2f}")
    print(f"   Citation Quality: {summary['overall_scores']['citation_quality_score']:.2f}")
    print(f"   Estimated Success Rate: {summary['success_rate_estimate']:.1f}%")
 
    if summary['success_rate_estimate'] >= 80:
        print("\nSUCCESS: The PoC has met the 80% evaluation requirement!")
    else:
        print("\nWARNING: The PoC did not meet the 80% evaluation requirement. Consider adjusting chunk size or embedding models.")
 
    print(f"\n--- DOCUMENT OBSERVATIONS ({len(doc_obs)} distinct sources retrieved) ---")
    ranked = sorted(doc_obs.items(), key=lambda kv: kv[1]["times_retrieved"], reverse=True)
    for key, obs in ranked[:15]:
        print(
            f"   retrieved={obs['times_retrieved']:2d} cited={obs['times_cited']:2d} "
            f"title={obs['title']!r} category={obs['category']!r}"
        )
 
 
if __name__ == "__main__":
    run_evaluation()