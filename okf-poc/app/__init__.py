"""
Main Application Package for the OKF Proof of Concept.

This package contains the core business logic, FastAPI endpoints,
Streamlit UI components, and knowledge processing engines (Ingestion,
OKF Formatting, and Retrieval).
"""

__version__ = "1.0.0"

# Expose core components at the root package level for easy access
from app.core.config import settings
from app.api.main import app as api_app
from app.ingestion.pipeline import run_ingestion_pipeline
from app.retrieval.query_engine import get_query_engine

# Define the public API of the `app` package
__all__ = [
    "settings",
    "api_app",
    "run_ingestion_pipeline",
    "get_query_engine"
]