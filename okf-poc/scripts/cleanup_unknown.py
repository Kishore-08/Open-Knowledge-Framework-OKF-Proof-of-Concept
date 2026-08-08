#!/usr/bin/env python3
"""
Clean up junk "Unknown Document" concepts from the OKF knowledge repository.

Concepts produced by a failed ingestion run (empty text, failed LLM metadata
extraction) can end up in `knowledge/` with placeholder titles such as
"Unknown Document", categories like "unknown"/"unclassified", and tags like
"unclassified". This script detects them and MOVES them to a quarantine
directory so the knowledge base only contains properly formatted concepts.

Usage:
    python -m scripts.cleanup_unknown                  # move junk concepts to knowledge/_quarantine/
    python -m scripts.cleanup_unknown --dry-run        # only list what would be moved
    python -m scripts.cleanup_unknown --quarantine-dir /tmp/okf-junk
"""

import argparse
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings
from app.okf.parser import parse_okf_file


# Placeholder values produced by failed metadata extraction.
_PLACEHOLDER_TITLES = {
    "unknown document", "unknown", "unclassified", "metadata extraction failed",
}
_PLACEHOLDER_CATEGORIES = {"", "unknown", "unclassified", "misc"}
_PLACEHOLDER_TAGS = {"unknown", "unclassified"}
_BAD_ID_RE = re.compile(r"^(unknown-document|document-\d+|unclassified)", re.IGNORECASE)


def is_bad_concept(meta: dict, path: str) -> tuple:
    """Return (is_bad, reason) for a parsed concept's metadata dict."""
    cid = (meta.get("id") or "").strip()
    title = (meta.get("title") or "").strip()
    category = (meta.get("category") or "").strip()
    tags = [str(t) for t in (meta.get("tags") or [])]
    description = (meta.get("description") or "").strip()

    if _BAD_ID_RE.match(cid):
        return True, f"placeholder id '{cid}'"
    if not title or title.lower() in _PLACEHOLDER_TITLES:
        return True, f"placeholder title '{title}'"
    if re.match(r"^document[\s-]+\d+$", title, re.IGNORECASE):
        return True, f"auto-numbered title '{title}'"
    if category in _PLACEHOLDER_CATEGORIES:
        return True, f"placeholder category '{category}'"
    if any(t.lower() in _PLACEHOLDER_TAGS for t in tags):
        return True, f"placeholder tag in {tags}"
    if "metadata extraction failed" in description.lower():
        return True, "failed metadata description"
    return False, ""


def collect_junk(knowledge_dir: str) -> list:
    """Return [(filepath, reason)] for every junk concept in the repository."""
    junk = []
    for dirpath, _dirnames, filenames in os.walk(knowledge_dir):
        if "_quarantine" in dirpath:
            continue
        for name in sorted(filenames):
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            try:
                raw_meta, _body = parse_okf_file(path)
            except Exception as exc:
                junk.append((path, f"unparseable frontmatter ({exc})"))
                continue
            bad, reason = is_bad_concept(raw_meta, path)
            if bad:
                junk.append((path, reason))
    return junk


def main() -> None:
    parser = argparse.ArgumentParser(description="Quarantine junk OKF concepts.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List junk concepts without moving anything",
    )
    parser.add_argument(
        "--knowledge-dir",
        default=settings.KNOWLEDGE_DIR,
        help=f"OKF knowledge repository to scan (default: {settings.KNOWLEDGE_DIR})",
    )
    parser.add_argument(
        "--quarantine-dir",
        default=None,
        help="Where to move junk concepts (default: <knowledge-dir>/_quarantine)",
    )
    args = parser.parse_args()

    knowledge_dir = args.knowledge_dir
    junk = collect_junk(knowledge_dir)

    if not junk:
        print("✅ No junk 'Unknown Document' concepts found — the repository is clean.")
        return

    print(f"⚠️ Found {len(junk)} junk concept(s):")
    for path, reason in junk:
        print(f"   - {path}  ({reason})")

    if args.dry_run:
        print("\n--dry-run: nothing was moved.")
        return

    quarantine = args.quarantine_dir or os.path.join(knowledge_dir, "_quarantine")
    os.makedirs(quarantine, exist_ok=True)

    for path, _reason in junk:
        rel = os.path.relpath(path, knowledge_dir)
        dest = os.path.join(quarantine, rel)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        shutil.move(path, dest)
        print(f"   moved -> {dest}")

    print(f"\n✅ Moved {len(junk)} junk concept(s) to {quarantine}.")
    print("   These are backed up, not deleted. Review and delete them manually if you wish.")
    print("   Next: rebuild the vector index with  python -m scripts.build_index")


if __name__ == "__main__":
    main()git