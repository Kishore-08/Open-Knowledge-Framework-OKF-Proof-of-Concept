from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from .routers import ingest_router, query_router, concepts_router, ask_router

# Initialize the FastAPI application
app = FastAPI(
    title="Open Knowledge Framework (OKF) - API",
    description="Enterprise PoC backend for ingesting, standardizing, and querying OKF knowledge using Hybrid Search.",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This is required so our Streamlit frontend can communicate with this API via HTTP
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allow all origins for the PoC
    allow_credentials=True,
    allow_methods=["*"], # Allow GET, POST, PUT, DELETE
    allow_headers=["*"],
)

# Register our Modular Routers
# All endpoints will be prefixed with /api/v1
app.include_router(ingest_router, prefix="/api/v1")
app.include_router(query_router, prefix="/api/v1")
app.include_router(concepts_router, prefix="/api/v1")
app.include_router(ask_router, prefix="/api/v1")

# Health Check Endpoint
@app.get("/health", tags=["System"])
async def health_check():
    """
    Reports API liveness plus the status of its dependencies (Qdrant, LLM key).

    Returns HTTP 200 even when a dependency is degraded so the frontend can
    distinguish "API offline" from "LLM key missing" / "Qdrant unreachable".
    """
    from app.retrieval.hybrid_search import get_qdrant_client

    checks = {"qdrant": {"ok": False}, "llm": {"ok": settings.has_gemini_api_key()}}

    try:
        client = get_qdrant_client()
        collections = [c.name for c in client.get_collections().collections]
        checks["qdrant"] = {"ok": True, "collections": collections}
    except Exception as exc:
        checks["qdrant"] = {"ok": False, "error": str(exc)}

    return {
        "status": "healthy" if checks["qdrant"]["ok"] else "degraded",
        "service": "OKF API",
        "checks": checks,
    }