"""
Core Module.

This module contains application-wide configurations, constants, and utilities.
"""

from .config import settings

# Expose settings directly when importing from app.core
__all__ = ["settings"]