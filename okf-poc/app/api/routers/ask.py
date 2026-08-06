"""
Compatibility shim for the /ask endpoint.

The AI assistant endpoint now lives in the consolidated Q&A module
(`app.api.routers.query`, `ask_router`). This file keeps existing imports
working without a second copy of the handler logic.
"""

from .query import ask_router as router
