import json
import os
from datetime import datetime
import pandas as pd
from datasets import Dataset

# Ragas metrics
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_correctness,
    context_relevance,
    context_relevancy,
    context_precision,
)

# Import our OKF Query Engine from the core app
from app.retrieval.query_engine import get_query_engine

def load_dataset(filepath: str) -> list:
    """Loads the 20-question evaluation dataset."""
    with open(filepath, "r") as f:
        data = json.load(f)
    return data["questions"]

def run_evaluation():
    """
    Executes the 20 questions against our OKF PoC pipeline, formats the results 
    for the Ragas framework, and calculates performance metrics.
    """
    print("🚀 Starting OKF Pipeline Evaluation using Ragas...")
    print("NOTE: ragas uses an LLM judge. With ragas 0.1.x this is OpenAI by default, "
          "so set OPENAI_API_KEY (or configure a Gemini langchain model) before running.")
    
    # 1. Load the dataset
    dataset_path = "evaluation/dataset.json"
    if not os.path.exists(dataset_path):
        print(f"❌ Error: Dataset not found at {dataset_path}")
        return
        
    questions_data = load_dataset(dataset_path)
    
    # Initialize our RAG Engine
    # Ensure Qdrant container is running and docs are ingested before running this!
    print("🔌 Connecting to Query Engine...")
    try:
        query_engine = get_query_engine()
    except Exception as e:
        print(f"❌ Failed to connect to Vector DB/Query Engine: {e}")
        print("Please ensure Qdrant is running and you have ingested documents.")
        return

    # Data structures required by Ragas
    data = {
        "question": [],
        "answer": [],
        "contexts": [],
        "ground_truth": []
    }

    print(f"🧠 Querying {len(questions_data)} questions. This may take a few minutes...")
    
    # 2. Run inferences
    for i, item in enumerate(questions_data):
        q = item["question"]
        gt = item["ground_truth"]
        
        print(f"   [{i+1}/20] Querying: {q}")
        
        response = query_engine.query(q)
        
        # Extract the actual answer text
        answer = str(response)
        
        # Extract the source chunks (contexts) used by the LLM
        contexts = [node.node.text for node in response.source_nodes] if response.source_nodes else []
        
        # Append to our dataset
        data["question"].append(q)
        data["answer"].append(answer)
        data["contexts"].append(contexts)
        data["ground_truth"].append(gt)

    # 3. Convert to HuggingFace Dataset format (required by Ragas)
    hf_dataset = Dataset.from_dict(data)

    # 4. Evaluate
    print("\n📊 Running Ragas metrics (Faithfulness, Correctness, Precision, Relevance)...")
    
    metrics = [
        faithfulness,        # Measures hallucination rate
        answer_correctness,  # Measures accuracy against ground truth
        context_relevancy,   # Measures if the retrieved OKF chunks actually pertain to the question
        context_precision    # Measures if the relevant OKF chunks were ranked at the top
    ]
    
    result = evaluate(
        hf_dataset,
        metrics=metrics,
    )

    # 5. Save Results
    os.makedirs("evaluation/results", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save raw DataFrame to CSV for detailed inspection
    df = result.to_pandas()
    csv_path = f"evaluation/results/evaluation_details_{timestamp}.csv"
    df.to_csv(csv_path, index=False)
    
    # Calculate overall averages to determine if we hit the >80% success requirement
    summary = {
        "timestamp": timestamp,
        "total_questions": len(questions_data),
        "overall_scores": {
            "faithfulness_score": df["faithfulness"].mean(),
            "answer_correctness_score": df["answer_correctness"].mean(),
            "context_relevance_score": df["context_relevance"].mean(),
            "context_precision_score": df["context_precision"].mean()
        },
        "success_rate_estimate": df["answer_correctness"].mean() * 100 
    }
    
    json_path = f"evaluation/results/evaluation_summary_{timestamp}.json"
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=4)
        
    print("\n✅ Evaluation Complete!")
    print(f"   Detailed CSV saved to: {csv_path}")
    print(f"   Summary JSON saved to: {json_path}")
    print("\n--- PERFORMANCE SUMMARY ---")
    print(f"   Faithfulness (Anti-Hallucination): {summary['overall_scores']['faithfulness_score']:.2f}")
    print(f"   Answer Correctness: {summary['overall_scores']['answer_correctness_score']:.2f}")
    print(f"   Retrieval Precision: {summary['overall_scores']['context_precision_score']:.2f}")
    print(f"   Estimated Success Rate: {summary['success_rate_estimate']:.1f}%")
    
    if summary['success_rate_estimate'] >= 80:
        print("\n🎉 SUCCESS: The PoC has met the 80% evaluation requirement!")
    else:
        print("\n⚠️ WARNING: The PoC did not meet the 80% evaluation requirement. Consider adjusting chunk size or embedding models.")

if __name__ == "__main__":
    run_evaluation()