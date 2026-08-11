#!/usr/bin/env python3
"""
Convert cached documentation HTML into OKF concept files (Phase 4).

Reads every cached page under `cache/<source>/`, cleans the HTML, converts it to
Markdown, splits it into concepts and writes them to `knowledge/<category>/`.

Usage:
    python -m scripts.convert_docs                    # all cached sources
    python -m scripts.convert_docs --source kubernetes
    python -m scripts.convert_docs --dry-run          # print what would be written
"""

import argparse
import os
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yaml

from app.converter.markdown import html_to_markdown, split_into_concepts, write_concept_file
from app.core.config import settings
from app.parser.cleaner import clean_html


def _sources() -> List[dict]:
    if not os.path.exists(settings.SOURCES_CONFIG):
        return []
    with open(settings.SOURCES_CONFIG, "r", encoding="utf-8") as f:
        return (yaml.safe_load(f) or {}).get("sources", [])


def convert_cached_source(source: dict, knowledge_dir: str, dry_run: bool) -> dict:
    """Convert every cached HTML page for a source into concepts."""
    cache_root = os.path.join(settings.CACHE_DIR, source["name"].lower())
    if not os.path.isdir(cache_root):
        return {"source": source["name"], "concepts": 0, "pages": 0, "written": 0}

    category = source.get("category", source["name"].lower())
    source_name = source["name"]
    concepts_written = 0
    pages_processed = 0

    for fname in sorted(os.listdir(cache_root)):
        if not fname.endswith(".html"):
            continue
        path = os.path.join(cache_root, fname)
        pages_processed += 1
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                html = f.read()
        except OSError as exc:
            print(f"⚠️ Could not read {path}: {exc}")
            continue

        # Extract the source URL from the filename? We store hash-based names, so
        # we fall back to the site root as provenance.
        source_url = source["base_url"]

        try:
            cleaned = clean_html(html, base_url=source["base_url"])
            markdown = html_to_markdown(cleaned)
        except Exception as exc:  # noqa: BLE001
            print(f"⚠️ Conversion failed for {path}: {exc}")
            continue

        concepts = split_into_concepts(
            markdown, category=category, source_name=source_name, source_url=source_url
        )
        for concept_id, _title, content in concepts:
            if dry_run:
                print(f"  📄 would write {concept_id}")
                continue
            write_concept_file(knowledge_dir, category, concept_id, content)
            concepts_written += 1

    return {"source": source["name"], "pages": pages_processed, "concepts": concepts_written}


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert cached docs into OKF concepts.")
    parser.add_argument("--source", help="Only convert this source name")
    parser.add_argument("--dry-run", action="store_true", help="Print without writing")
    parser.add_argument("--knowledge-dir", default=settings.KNOWLEDGE_DIR)
    args = parser.parse_args()

    sources = _sources()
    if args.source:
        sources = [s for s in sources if s["name"] == args.source]

    total = {"pages": 0, "concepts": 0}
    for source in sources:
        result = convert_cached_source(source, args.knowledge_dir, args.dry_run)
        total["pages"] += result["pages"]
        total["concepts"] += result["concepts"]
        print(f"📊 {result['source']}: pages={result['pages']} concepts={result['concepts']}")

    print(f"\n✅ Total: pages={total['pages']} concepts={total['concepts']}")
    if args.dry_run:
        print("(dry-run: no files were written)")


if __name__ == "__main__":
    main()
