"""
Main Application Package for the OKF Proof of Concept.

This package contains the core business logic, FastAPI endpoints,
Streamlit UI components, and knowledge processing engines (Ingestion,
OKF Formatting, and Retrieval).
"""

__version__ = "1.0.0"

# ---------------------------------------------------------------------------
# Guard heavy imports so that the UI-only container (which only installs
# streamlit + requests) can import this package without crashing.
# The API container has the full dependency set and will succeed normally.
# ---------------------------------------------------------------------------

try:
    from app.core.config import settings
except ImportError:
    settings = None  # type: ignore[assignment]

try:
    from app.api.main import app as api_app
except ImportError:
    api_app = None  # type: ignore[assignment]

try:
    from app.ingestion.pipeline import run_ingestion_pipeline
except ImportError:
    run_ingestion_pipeline = None  # type: ignore[assignment]

# Define the public API of the `app` package
__all__ = [
    "settings",
    "api_app",
    "run_ingestion_pipeline"
]