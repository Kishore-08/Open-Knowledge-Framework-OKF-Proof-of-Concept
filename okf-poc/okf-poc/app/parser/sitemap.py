"""
Sitemap & robots.txt support (Phase 2 - data collection).

Discovers the pages of an official documentation site from its sitemap(s),
optionally filtered by URL patterns (e.g. only /docs/ pages).
"""

import gzip
import html
import io
import re
from typing import List, Optional, Tuple
from urllib.parse import urljoin, urlparse
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


async def discover_urls_from_sitemap(
    sitemap_urls: List[str],
    fetch,
    url_filter: Optional[str] = None,
    max_urls: int = 2000,
    base_url: Optional[str] = None,
    exclude_filters: Optional[List[str]] = None,
) -> List[str]:
    """
    Given one or more sitemap URLs, fetch and flatten them (following nested
    sitemap indexes) and return page URLs, optionally filtered by a substring
    pattern.

    `fetch` is an async callable `async def fetch(url) -> bytes`.
    """
    excludes = exclude_filters or []
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
            if not urlparse(page).scheme:
                page = urljoin(base_url or sitemap_url, page)
            page = page.split("#", 1)[0]
            if url_filter and url_filter not in page:
                continue
            if any(ex in page for ex in excludes):
                continue
            if page not in discovered:
                discovered.append(page)
        # Resolve relative sitemap entries (e.g. airflow.apache.org) against the
        # base URL so nested index URLs are absolute before being fetched.
        for nested_url in nested:
            if not urlparse(nested_url).scheme:
                nested_url = urljoin(base_url or sitemap_url, nested_url)
            queue.append(nested_url)

    return discovered[:max_urls]


async def discover_urls_from_html_index(
    index_url: str,
    fetch,
    url_filter: Optional[str] = None,
    max_urls: int = 2000,
    exclude_filters: Optional[List[str]] = None,
) -> List[str]:
    """
    Discover documentation URLs from a plain HTML index page (used by sources
    without a usable sitemap, e.g. man7.org man-page listing pages).

    All ``href`` attributes are collected, resolved to absolute URLs against
    the index page itself, de-duplicated and optionally filtered.
    """
    excludes = exclude_filters or []
    try:
        body = await fetch(index_url)
    except Exception as exc:  # noqa: BLE001
        print(f"⚠️ Failed to fetch index page {index_url}: {exc}")
        return []
    if not body:
        return []

    text = body.decode("utf-8", errors="ignore")
    hrefs = re.findall(r'href=[\'"]?([^\'" >]+)', text)

    discovered: List[str] = []
    seen: set = set()
    for href in hrefs:
        resolved = urljoin(index_url, html.unescape(href))
        if not resolved.startswith(("http://", "https://")):
            continue
        if url_filter and url_filter not in resolved:
            continue
        if any(ex in resolved for ex in excludes):
            continue
        # Strip the fragment so anchor links ("page.html#section") collapse
        # onto the same document instead of producing duplicate cache entries.
        resolved = resolved.split("#", 1)[0]
        if resolved in seen:
            continue
        seen.add(resolved)
        discovered.append(resolved)
        if len(discovered) >= max_urls:
            break

    return discovered[:max_urls]
