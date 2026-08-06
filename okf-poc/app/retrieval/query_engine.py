import os
from llama_index.core import VectorStoreIndex, Settings, PromptTemplate
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from google.api_core.retry import Retry
from google.generativeai import types as genai_types

from .hybrid_search import get_qdrant_vector_store
from app.core.config import settings

# Disable the SDK's internal retry so quota (429) errors surface immediately
# instead of blocking the request thread for a minute or more.
_NO_RETRY = Retry(predicate=lambda exc: False)


def _request_options() -> genai_types.RequestOptions:
    return genai_types.RequestOptions(
        retry=_NO_RETRY,
        timeout=settings.LLM_TIMEOUT_SECONDS,
    )

# 1. Define the Strict OKF Prompt Template
# This satisfies the requirement to distinguish retrieved knowledge and cite sources.
OKF_QA_PROMPT_TMPL = (
    "You are an enterprise AI assistant powered by the Open Knowledge Framework (OKF).\n"
    "Context information from our OKF documents is provided below.\n"
    "---------------------\n"
    "{context_str}\n"
    "---------------------\n"
    "Given the context information and strictly NO prior knowledge, answer the user's query.\n"
    "RULES:\n"
    "1. You MUST strictly base your answer on the provided context.\n"
    "2. Every time you use information, you MUST cite the source document inline using the 'title' "
    "field from the metadata. Example: 'According to [Architecture_v2], the system uses...'\n"
    "3. If the context does not contain the answer, you must say: 'I cannot answer this based on the ingested OKF sources.' "
    "Do not guess or hallucinate.\n\n"
    "Query: {query_str}\n"
    "Answer: "
)
OKF_QA_PROMPT = PromptTemplate(OKF_QA_PROMPT_TMPL)

def configure_llm_settings():
    """
    Configures the global LLM and Embedding models for LlamaIndex.
    We use fast, cost-effective models ideal for a PoC.
    Note: Ensure GEMINI_API_KEY or GOOGLE_API_KEY is set in your .env file.
    Uses transport='rest' for both Gemini (LLM) and GeminiEmbedding to bypass
    gRPC credentials plugin validation which fails for some API key formats.
    """
    api_key = settings.get_gemini_api_key()

    # Force the GOOGLE_API_KEY env var so google.generativeai picks it up
    os.environ["GOOGLE_API_KEY"] = api_key

    # gemini-3.5-flash: current-gen, available on the free tier for new keys
    # Using transport="rest" to prevent gRPC plugin_credentials header rejection errors,
    # plus request_options that disable google-api-core's blocking 429 retry.
    Settings.llm = Gemini(
        model=settings.LLM_MODEL,
        temperature=settings.TEMPERATURE,
        api_key=api_key,
        transport="rest",
        request_options=_request_options(),
    )

    # Gemini embeddings: use transport="rest" to prevent gRPC metadata header rejection issues
    embed_model = settings.EMBEDDING_MODEL
    if not embed_model.startswith("models/"):
        embed_model = f"models/{embed_model}"
    Settings.embed_model = GeminiEmbedding(
        model_name=embed_model,
        api_key=api_key,
        transport="rest",
    )

def get_query_engine(similarity_top_k: int = None):
    """
    Constructs the RAG query engine using LlamaIndex and Qdrant.
    It enables Dense semantic search.
    """
    if similarity_top_k is None:
        similarity_top_k = settings.TOP_K
 
    # 1. Setup Models
    configure_llm_settings()
    
    # 2. Get the Qdrant connection we built earlier
    vector_store = get_qdrant_vector_store()
    
    # 3. Load the Index directly from Qdrant
    # This prevents us from needing to re-index documents every time the server starts
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    
    # 4. Build the engine with dense semantic search (default query mode)
    query_engine = index.as_query_engine(
        similarity_top_k=similarity_top_k,
        vector_store_query_mode="default"
    )

    # 5. Apply our strict OKF anti-hallucination prompt
    query_engine.update_prompts(
        {"response_synthesizer:text_qa_template": OKF_QA_PROMPT}
    )
    
    return query_engine

def get_retriever(similarity_top_k: int = None):
    """
    Utility function: Sometimes we just want to fetch the raw documents
    WITHOUT generating an LLM answer (e.g., for the UI to display citations).
    """
    if similarity_top_k is None:
        similarity_top_k = settings.TOP_K
    configure_llm_settings()
    vector_store = get_qdrant_vector_store()
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    return index.as_retriever(
        similarity_top_k=similarity_top_k,
        vector_store_query_mode="default"
    )