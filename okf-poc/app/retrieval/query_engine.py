import os
from llama_index.core import VectorStoreIndex, Settings, PromptTemplate
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from .hybrid_search import get_qdrant_vector_store

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
    Note: Ensure GEMINI_API_KEY is set in your .env file.
    """
    # gemini-2.5-flash is excellent for fast reasoning and following strict prompt instructions
    Settings.llm = Gemini(model="gemini-2.5-flash", temperature=0.1)
    
    # text-embedding-004 creates the dense vectors for our semantic search
    Settings.embed_model = GeminiEmbedding( model_name="models/text-embedding-004" )

def get_query_engine(similarity_top_k: int = 5, sparse_top_k: int = 5):
    """
    Constructs the RAG query engine using LlamaIndex and Qdrant.
    It enables Hybrid Search (Dense vectors + BM25 sparse keywords).
    """
    # 1. Setup Models
    configure_llm_settings()
    
    # 2. Get the Qdrant connection we built earlier
    vector_store = get_qdrant_vector_store()
    
    # 3. Load the Index directly from Qdrant
    # This prevents us from needing to re-index documents every time the server starts
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    
    # 4. Build the engine with Hybrid Search enabled
    query_engine = index.as_query_engine(
        similarity_top_k=similarity_top_k,
        sparse_top_k=sparse_top_k,
        vector_store_query_mode="hybrid", # Fulfills the 'Hybrid Search' bonus feature
        alpha=0.5 # 0.5 balances semantic meaning (vectors) with exact keyword matching (sparse)
    )
    
    # 5. Apply our strict OKF anti-hallucination prompt
    query_engine.update_prompts(
        {"response_synthesizer:text_qa_template": OKF_QA_PROMPT}
    )
    
    return query_engine

def get_retriever(similarity_top_k: int = 5):
    """
    Utility function: Sometimes we just want to fetch the raw documents 
    WITHOUT generating an LLM answer (e.g., for the UI to display citations).
    """
    configure_llm_settings()
    vector_store = get_qdrant_vector_store()
    index = VectorStoreIndex.from_vector_store(vector_store=vector_store)
    return index.as_retriever(
        similarity_top_k=similarity_top_k, 
        vector_store_query_mode="hybrid"
    )