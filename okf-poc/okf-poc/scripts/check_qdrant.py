#!/usr/bin/env python3
"""Check what's in Qdrant"""

from app.retrieval.hybrid_search import get_qdrant_client

client = get_qdrant_client()
collection_info = client.get_collection("okf_concepts")

print(f"Collection: okf_concepts")
print(f"Points count: {collection_info.points_count}")
print(f"Vectors count: {collection_info.vectors_count}")

# Sample some points
points = client.scroll("okf_concepts", limit=20)[0]
print(f"\nSample points:")
for p in points:
    print(f"  - {p.payload.get('title')} (category={p.payload.get('category')})")
