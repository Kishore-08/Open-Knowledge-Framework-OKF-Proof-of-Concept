#!/usr/bin/env python3
"""Inspect the configured OKF Qdrant collection without modifying it."""

import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings
from app.retrieval.hybrid_search import get_qdrant_client


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--collection",
        default=settings.QDRANT_CONCEPTS_COLLECTION,
        help="Collection to inspect (default: configured QDRANT_CONCEPTS_COLLECTION)",
    )
    parser.add_argument("--limit", type=int, default=10, help="Sample points to show")
    args = parser.parse_args()

    client = get_qdrant_client()
    if not client.collection_exists(args.collection):
        print(f"Collection '{args.collection}' does not exist.", file=sys.stderr)
        print("Run an ingestion job or: python -m scripts.build_index", file=sys.stderr)
        return 1

    collection_info = client.get_collection(args.collection)
    print(f"Collection: {args.collection}")
    print(f"Points: {collection_info.points_count or 0}")

    points, _ = client.scroll(
        collection_name=args.collection,
        limit=max(args.limit, 0),
        with_payload=["id", "title", "category", "source_file"],
        with_vectors=False,
    )
    if not points:
        print("No points found.")
        return 0

    print("\nSample points:")
    for point in points:
        payload = point.payload or {}
        title = payload.get("title") or payload.get("id") or point.id
        category = payload.get("category") or "uncategorized"
        source = payload.get("source_file") or "unknown source"
        print(f"  - {title} (category={category}, source={source})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
