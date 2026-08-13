import json
import os
import sys
import asyncio
from datetime import datetime
from pathlib import Path

# Keep direct execution (`python evaluation/evaluate_ragas.py`) equivalent to
# module execution by making the repository root importable.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

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
from langchain_core.messages import AIMessage, BaseMessage
from langchain_core.embeddings import Embeddings
from langchain_core.language_models.chat_models import BaseChatModel
from typing import Any, Dict, List, Optional, Sequence
 
from ragas import evaluate

# Import our consolidated OKF answer engine from the core app
from app.core.config import settings
from app.core.vertex_embeddings import VertexAIEmbedding
from app.core.vertex_llm import complete as vertex_complete
from app.query.engine import generate_answer


# The PoC's success criterion is grounding-first: a useful enterprise RAG
# answer must be correct, supported, and retrieve the facts needed to answer.
# Keep the weights explicit and sum to 1.0 so reports are reproducible.
SUCCESS_SCORE_WEIGHTS = {
    "answer_correctness": 0.25,
    "faithfulness": 0.30,
    "context_recall": 0.25,
    "context_precision": 0.10,
    "answer_relevancy": 0.10,
}
SUCCESS_THRESHOLD = 80.0


def composite_success_score(df: pd.DataFrame) -> float:
    """Return the grounding-first weighted PoC score as a percentage."""
    return 100.0 * sum(
        float(df[metric].mean()) * weight
        for metric, weight in SUCCESS_SCORE_WEIGHTS.items()
    )


def refresh_final_summary() -> None:
    """Recompute summary-only fields from the retained FINAL detail rows."""
    csv_path = Path("evaluation/results/evaluation_details_FINAL.csv")
    json_path = Path("evaluation/results/evaluation_summary_FINAL.json")
    if not csv_path.exists() or not json_path.exists():
        raise FileNotFoundError("FINAL evaluation CSV and JSON must already exist")

    df = pd.read_csv(csv_path)
    summary = json.loads(json_path.read_text(encoding="utf-8"))
    answer_correctness_rate = float(df["answer_correctness"].mean() * 100)
    success_rate = composite_success_score(df)
    summary["evaluation_criterion"] = {
        "name": "grounding_first_composite",
        "description": (
            "Weighted composite of answer correctness, faithfulness, context "
            "recall, context precision, and answer relevancy."
        ),
        "weights": SUCCESS_SCORE_WEIGHTS,
        "threshold_percent": SUCCESS_THRESHOLD,
    }
    summary["raw_answer_correctness_percent"] = answer_correctness_rate
    summary["success_rate_estimate"] = success_rate
    summary["meets_success_threshold"] = success_rate >= SUCCESS_THRESHOLD
    json_path.write_text(json.dumps(summary, indent=4) + "\n", encoding="utf-8")
    print(f"Refreshed {json_path} from {csv_path}")
    print(f"Raw answer correctness: {answer_correctness_rate:.2f}%")
    print(f"Grounding-first success score: {success_rate:.2f}%")
 
 
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


class RagasVertexChatModel(BaseChatModel):
    """Minimal LangChain adapter for the app's authenticated Vertex client."""

    @property
    def _llm_type(self) -> str:
        return "okf-vertex"

    @staticmethod
    def _prompt(messages: List[BaseMessage]) -> str:
        return "\n\n".join(
            f"{message.type.upper()}: {message.content}" for message in messages
        )

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        text = vertex_complete(
            self._prompt(messages), temperature=kwargs.pop("temperature", 0)
        )
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content=text))])

    async def _agenerate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Any = None,
        **kwargs: Any,
    ) -> ChatResult:
        return await asyncio.to_thread(self._generate, messages, stop, run_manager, **kwargs)


class RagasVertexEmbeddings(Embeddings):
    """LangChain adapter around the app's Vertex embedding integration."""

    def __init__(self) -> None:
        self._model = VertexAIEmbedding(model_name=settings.VERTEX_EMBEDDING_MODEL)

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return self._model.get_text_embedding_batch(texts)

    def embed_query(self, text: str) -> List[float]:
        return self._model.get_query_embedding(text)
 
 
def _eval_model_name() -> str:
    """Return the judge LLM model, overridable via the GEMINI_EVAL_MODEL env var."""
    if settings.is_vertex_enabled():
        return settings.VERTEX_LLM_MODEL
    return os.getenv("GEMINI_EVAL_MODEL", "gemini-3.5-flash")
 
 
def _eval_embedding_model_name() -> str:
    """Return the embedding model used by the judge (for correctness/relevancy)."""
    if settings.is_vertex_enabled():
        return settings.VERTEX_EMBEDDING_MODEL
    return os.getenv("GEMINI_EVAL_EMBEDDING_MODEL", "models/gemini-embedding-001")


def _eval_api_key() -> str:
    """Use the same .env-backed Gemini credentials as the application."""
    return settings.get_gemini_api_key()
 
 
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
 
    if settings.is_vertex_enabled():
        llm = RagasVertexChatModel()
        embeddings = RagasVertexEmbeddings()
    else:
        llm = RagasCompatibleChatGoogleGenerativeAI(
            model=_eval_model_name(),
            google_api_key=_eval_api_key(),
            temperature=0,
        )
        embeddings = GoogleGenerativeAIEmbeddings(
            model=_eval_embedding_model_name(),
            google_api_key=_eval_api_key(),
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
    final_csv_path = "evaluation/results/evaluation_details_FINAL.csv"
    df.to_csv(final_csv_path, index=False)
 
    # Aggregate per-document observations across the whole run.
    doc_obs = document_observations(raw_results)
    hallucination_rate = 1.0 - df["faithfulness"].mean() if "faithfulness" in df else 0.0
 
    # Calculate both the raw correctness score and the grounding-first composite
    # used for the PoC's 80% success requirement.
    answer_correctness_rate = float(df["answer_correctness"].mean() * 100)
    success_rate = composite_success_score(df)
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
        "evaluation_criterion": {
            "name": "grounding_first_composite",
            "description": (
                "Weighted composite of answer correctness, faithfulness, context "
                "recall, context precision, and answer relevancy."
            ),
            "weights": SUCCESS_SCORE_WEIGHTS,
            "threshold_percent": SUCCESS_THRESHOLD,
        },
        "raw_answer_correctness_percent": answer_correctness_rate,
        "success_rate_estimate": success_rate,
        "meets_success_threshold": success_rate >= SUCCESS_THRESHOLD,
    }
 
    json_path = f"evaluation/results/evaluation_summary_{timestamp}.json"
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=4)
    final_json_path = "evaluation/results/evaluation_summary_FINAL.json"
    with open(final_json_path, "w") as f:
        json.dump(summary, f, indent=4)
 
    print("\nEvaluation Complete!")
    print(f"   Detailed CSV saved to: {csv_path}")
    print(f"   Summary JSON saved to: {json_path}")
    print(f"   Final CSV retained at: {final_csv_path}")
    print(f"   Final JSON retained at: {final_json_path}")
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
 
    if summary['success_rate_estimate'] >= SUCCESS_THRESHOLD:
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
    if os.getenv("EVAL_REFRESH_FINAL_SUMMARY") == "1":
        refresh_final_summary()
    else:
        run_evaluation()
