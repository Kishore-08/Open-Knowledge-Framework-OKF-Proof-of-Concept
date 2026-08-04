from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import ingest_router, query_router

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

# Health Check Endpoint
@app.get("/health", tags=["System"])
async def health_check():
    """Simple endpoint to verify the API container is running."""
    return {"status": "healthy", "service": "OKF API"}