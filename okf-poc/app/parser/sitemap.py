"""
Sitemap & robots.txt support (Phase 2 - data collection).

Discovers the pages of an official documentation site from its sitemap(s),
optionally filtered by URL patterns (e.g. only /docs/ pages).
"""

import gzip
import io
import re
from typing import List, Optional, Tuple
from urllib.parse import urlparse
from xml.etree import ElementTree

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def parse_robots_txt(robots_text: str) -> List[str]:
    """Extract Sitemap: directives from a robots.txt body."""
    sitemaps = []
    for line in robots_text.splitlines():
        stripped = line.strip()
        if stripped.lower().startswith("sitemap:"):
            url = stripped.split(":", 1)[1].strip()
            if url:
                sitemaps.append(url)
    return sitemaps


def _load_sitemap_document(content: bytes) -> Tuple[List[str], List[str]]:
    """
    Parse a sitemap (or sitemap index) document.
    Returns (page_urls, nested_sitemap_urls).
    """
    # Sitemaps may be gzip-compressed.
    raw = gzip.decompress(content) if content[:2] == b"\x1f\x8b" else content
    try:
        root = ElementTree.fromstring(raw)
    except ElementTree.ParseError:
        return [], []

    pages, nested = [], []
    for child in root:
        tag = child.tag.rsplit("}", 1)[-1]
        if tag == "url":
            loc = child.find(f"{{{SITEMAP_NS}}}loc")
            if loc is not None and loc.text:
                pages.append(loc.text.strip())
        elif tag == "sitemap":
            loc = child.find(f"{{{SITEMAP_NS}}}loc")
            if loc is not None and loc.text:
                nested.append(loc.text.strip())
    return pages, nested


def parse_sitemap_urls(content: bytes, max_urls: int = 5000) -> List[str]:
    """
    Parse a single sitemap document body (or index) and return all page URLs.
    Nested sitemap URLs are NOT fetched here - see discover_urls_from_sitemap.
    """
    pages, _ = _load_sitemap_document(content)
    return pages[:max_urls]


async def discover_urls_from_sitemap(
    sitemap_urls: List[str],
    fetch,
    url_filter: Optional[str] = None,
    max_urls: int = 2000,
) -> List[str]:
    """
    Given one or more sitemap URLs, fetch and flatten them (following nested
    sitemap indexes) and return page URLs, optionally filtered by a substring
    pattern.

    `fetch` is an async callable `async def fetch(url) -> bytes`.
    """
    discovered: List[str] = []
    queue = list(sitemap_urls)
    visited = set()

    while queue and len(discovered) < max_urls:
        sitemap_url = queue.pop(0)
        if sitemap_url in visited:
            continue
        visited.add(sitemap_url)
        try:
            body = await fetch(sitemap_url)
        except Exception as exc:  # noqa: BLE001
            print(f"⚠️ Failed to fetch sitemap {sitemap_url}: {exc}")
            continue
        if not body:
            continue
        pages, nested = _load_sitemap_document(body)
        for page in pages:
            if url_filter and url_filter not in page:
                continue
            if page not in discovered:
                discovered.append(page)
        queue.extend(nested)

    return discovered[:max_urls]


def filter_urls(urls: List[str], patterns: List[str]) -> List[str]:
    """Keep only URLs that match at least one regex pattern."""
    if not patterns:
        return urls
    compiled = [re.compile(p) for p in patterns]
    return [u for u in urls if any(c.search(u) for c in compiled)]
