#!/usr/bin/env python3
"""
Build the Qdrant concept index from the knowledge repository (Phase 9).

Usage:
    python -m scripts.build_index                       # embed + upsert (needs GEMINI_API_KEY)
    python -m scripts.build_index --dry-run             # validate documents, no embeddings
    python -m scripts.build_index --source kubernetes   # reserved: filter by category
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings
from app.indexing.indexer import build_concepts_index


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the Qdrant concept index.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate concepts without calling the embedding API",
    )
    args = parser.parse_args()

    result = build_concepts_index(with_embeddings=not args.dry_run)
    print(result)


if __name__ == "__main__":
    main()
