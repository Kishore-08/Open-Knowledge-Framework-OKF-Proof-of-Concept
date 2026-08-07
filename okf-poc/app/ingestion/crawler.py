"""
Web crawler (Phase 2 - data collection).

Discovers pages from official documentation via sitemap.xml / robots.txt, fetches
them with caching, and stores the raw HTML under `cache/<source>/<url-hash>.html`.
The crawler is deliberately sitemap-driven so it only touches pages the site
explicitly publishes.
"""

import asyncio
import hashlib
import os
import re
import time
import json
from dataclasses import dataclass, field
from typing import List, Optional

import httpx

from app.core.config import settings
from app.parser.sitemap import parse_robots_txt, discover_urls_from_sitemap


@dataclass
class CrawlResult:
    """Outcome of crawling a single source."""

    source_name: str
    fetched: int = 0
    changed: int = 0
    unchanged: int = 0
    deleted: int = 0
    failed: int = 0
    urls: List[str] = field(default_factory=list)
    changed_urls: List[str] = field(default_factory=list)
    deleted_urls: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


def _url_hash(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]

def _state_path(source: str, raw_dir: str) -> str:
    """Return the synchronization state file for a documentation source."""
    state_dir = os.path.join(raw_dir, ".state")
    os.makedirs(state_dir, exist_ok=True)
    return os.path.join(state_dir, f"{_safe_name(source)}.json")


def raw_path(source: str, url: str) -> str:
    """Local path for the cached raw HTML of a URL."""
    root = os.path.join(settings.CACHE_DIR, _safe_name(source))
    os.makedirs(root, exist_ok=True)
    return os.path.join(root, f"{_url_hash(url)}.html")


def _safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9-_]+", "-", name).strip("-").lower() or "source"

def load_sources() -> dict:
    """Load enabled documentation sources from the application configuration."""
    if not os.path.exists(settings.SOURCES_CONFIG):
        return {}

    import yaml

    with open(settings.SOURCES_CONFIG, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    return data

def _load_state(source: str, raw_dir: str) -> Dict[str, dict]:
    """Load persisted synchronization state for a documentation source."""
    path = _state_path(source, raw_dir)

    if not os.path.exists(path):
        return {}

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            return {}

        return data.get("pages", {})

    except (OSError, json.JSONDecodeError) as exc:
        print(f"⚠️ Could not load crawler state {path}: {exc}")
        return {}

def _save_state(source: str, raw_dir: str, pages: Dict[str, dict]) -> None:
    """Persist synchronization state atomically."""
    path = _state_path(source, raw_dir)
    temp_path = f"{path}.tmp"

    payload = {
        "version": 1,
        "source": source,
        "pages": pages,
    }

    with open(temp_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, sort_keys=True)

    os.replace(temp_path, path)

def _content_hash(content: bytes) -> str:
    """Return the SHA-256 hash of downloaded document content."""
    return hashlib.sha256(content).hexdigest()

class DocsCrawler:
    """Sitemap-driven crawler with on-disk caching and polite rate limiting."""

    def __init__(self, *, timeout: float = 30.0, delay: float = 0.5, user_agent: str = "OKF-Crawler/1.0"):
        self.timeout = timeout
        self.delay = delay
        self.user_agent = user_agent
        self._last_request = 0.0

    async def _fetch(self, url: str) -> bytes:
        await asyncio.sleep(max(0.0, self._last_request + self.delay - time.monotonic()))
        self._last_request = time.monotonic()
        async with httpx.AsyncClient(
            timeout=self.timeout,
            follow_redirects=True,
            headers={"User-Agent": self.user_agent, "Accept": "text/html,*/*;q=0.8"},
        ) as client:
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.content

    async def _fetch_robots(self, base_url: str) -> List[str]:
        """Read robots.txt and return the Sitemap: URLs listed there."""
        robots_url = base_url.rstrip("/") + "/robots.txt"
        try:
            body = await self._fetch(robots_url)
        except Exception as exc:  # noqa: BLE001 - no robots.txt is fine
            print(f"ℹ️ No robots.txt at {robots_url}: {exc}")
            return []
        return parse_robots_txt(body.decode("utf-8", errors="ignore"))

    async def discover(
        self,
        base_url: str,
        sitemap_urls: Optional[List[str]] = None,
        url_filter: Optional[str] = None,
        max_urls: int = 500,
    ) -> List[str]:
        """
        Discover documentation URLs for a source. If `sitemap_urls` is not given,
        tries robots.txt first, then the conventional /sitemap.xml location.
        """
        sitemaps = sitemap_urls or await self._fetch_robots(base_url)
        if not sitemaps:
            sitemaps = [base_url.rstrip("/") + "/sitemap.xml"]
        return await discover_urls_from_sitemap(sitemaps, self._fetch, url_filter=url_filter, max_urls=max_urls)

    async def crawl_source(
        self,
        source_name: str,
        urls: List[str],
        raw_dir: str,
        ) -> CrawlResult:
        """
        Fetch discovered documentation pages and synchronize their raw files.

        Determines page state using:
        1. HTTP ETag / Last-Modified when available.
        2. SHA-256 content hash as the authoritative fallback.

        Returns only changed and deleted URLs for downstream processing.
        """
        result = CrawlResult(
            source_name=source_name,
            urls=urls,
        )

        previous_state = _load_state(source_name, raw_dir)
        current_state: Dict[str, dict] = {}

        discovered_urls = set(urls)

        for url in urls:
            target = raw_path(source_name, url, raw_dir)
            previous = previous_state.get(url, {})

            conditional_headers = {}

            if previous.get("etag"):
                conditional_headers["If-None-Match"] = previous["etag"]

            if previous.get("last_modified"):
                conditional_headers["If-Modified-Since"] = previous["last_modified"]

            try:
                response = await self._fetch_with_metadata(
                    url,
                    headers=conditional_headers,
                )

                if response["status_code"] == 304:
                    current_state[url] = {
                        **previous,
                        "raw_file": os.path.relpath(
                            target,
                            raw_dir,
                        ),
                    }

                    result.unchanged += 1
                    continue

                content = response["content"]

                if not content:
                    raise ValueError("Downloaded document is empty.")

                content_hash = _content_hash(content)
                previous_hash = previous.get("content_hash")

                is_new = not previous
                is_changed = (
                    previous_hash is not None
                    and previous_hash != content_hash
                )

                # If a state file is missing but the raw file exists, treat the
                # downloaded content as new state rather than trusting the file.
                if is_new:
                    result.fetched += 1
                    result.changed += 1
                    result.changed_urls.append(url)

                elif is_changed:
                    result.fetched += 1
                    result.changed += 1
                    result.changed_urls.append(url)

                else:
                    result.unchanged += 1

                if is_new or is_changed:
                    with open(target, "wb") as f:
                        f.write(content)

                current_state[url] = {
                    "raw_file": os.path.relpath(target, raw_dir),
                    "content_hash": content_hash,
                    "etag": response.get("etag"),
                    "last_modified": response.get("last_modified"),
                }

            except Exception as exc:
                result.failed += 1
                result.errors.append(f"{url}: {exc}")

                # Preserve previous state when a temporary network failure occurs.
                if previous:
                    current_state[url] = previous

        # Anything present in the previous state but absent from the current
        # sitemap is considered deleted from the official documentation.
        for url, previous in previous_state.items():
            if url in discovered_urls:
                continue

            result.deleted += 1
            result.deleted_urls.append(url)

            raw_file = previous.get("raw_file")

            if raw_file:
                path = os.path.join(raw_dir, raw_file)

                try:
                    if os.path.exists(path):
                        os.remove(path)
                except OSError as exc:
                    result.errors.append(
                        f"{url}: failed to remove raw file {path}: {exc}"
                    )

        _save_state(
            source_name,
            raw_dir,
            current_state,
        )

        return result

    async def crawl(
        self,
        source_name: str,
        base_url: str,
        *,
        sitemap_urls: Optional[List[str]] = None,
        url_filter: Optional[str] = None,
        max_urls: int = 500,
        urls: Optional[List[str]] = None,
        raw_dir: Optional[str] = None,
    ) -> CrawlResult:
        """Discover + synchronize a documentation source end to end."""
        if raw_dir is None:
            raw_dir = settings.RAW_DATA_DIR

        if urls is None:
            urls = await self.discover(
                base_url,
                sitemap_urls,
                url_filter,
                max_urls,
            )

        return await self.crawl_source(
            source_name,
            urls,
            raw_dir,
        )

async def crawl_configured_sources(    raw_dir: Optional[str] = None,) -> dict:
    """
    Crawl all enabled documentation sources configured in sources.yaml.

    Raw downloaded documents are stored under settings.RAW_DATA_DIR.
    """
    config = load_sources()

    sources = config.get("sources", [])
    crawler_config = config.get("crawler", {})

    crawler = DocsCrawler(
        delay=float(crawler_config.get("delay", 0.5)),
        timeout=float(crawler_config.get("timeout", 30)),
        user_agent=crawler_config.get(
            "user_agent",
            "OKF-Crawler/1.0",
        ),
    )

    max_urls = int(
        crawler_config.get(
            "max_urls_per_source",
            500,
        )
    )

    totals = {
        "sources": 0,
        "discovered": 0,
        "fetched": 0,
        "changed": 0,
        "unchanged": 0,
        "deleted": 0,
        "failed": 0,
        "changed_urls": [],
        "deleted_urls": [],
    }

    for source in sources:
        if not source.get("enabled", True):
            continue

        name = source["name"]

        print(
            f"🔎 Crawling official documentation: "
            f"{name} ({source['base_url']})"
        )

        result = await crawler.crawl(
            source_name=name,
            base_url=source["base_url"],
            sitemap_urls=(
                [source["sitemap_url"]]
                if source.get("sitemap_url")
                else None
            ),
            url_filter=source.get("url_filter"),
            max_urls=max_urls,
            raw_dir=raw_dir,
        )

        totals["sources"] += 1
        totals["discovered"] += len(result.urls)
        totals["fetched"] += result.fetched
        totals["changed"] += result.changed
        totals["unchanged"] += result.unchanged
        totals["deleted"] += result.deleted
        totals["failed"] += result.failed

        totals["changed_urls"].extend(result.changed_urls)
        totals["deleted_urls"].extend(result.deleted_urls)

        print(
            f"📊 {name}: "
            f"discovered={len(result.urls)} "
            f"changed={result.changed} "
            f"unchanged={result.unchanged} "
            f"deleted={result.deleted} "
            f"failed={result.failed}"
        )

        for error in result.errors[:5]:
            print(f"⚠️ {error}")

    return totals

async def _fetch_with_metadata(
    self,
    url: str,
    headers: Optional[Dict[str, str]] = None,
):
    """Fetch a URL and return status, content and cache validators."""
    await asyncio.sleep(
        max(
            0.0,
            self._last_request + self.delay - time.monotonic(),
        )
    )

    self._last_request = time.monotonic()

    request_headers = {
        "User-Agent": self.user_agent,
        "Accept": "text/html,*/*;q=0.8",
    }

    if headers:
        request_headers.update(headers)

    async with httpx.AsyncClient(
        timeout=self.timeout,
        follow_redirects=True,
        headers=request_headers,
    ) as client:
        response = await client.get(url)

        if response.status_code == 304:
            return {
                "status_code": 304,
                "content": b"",
                "etag": response.headers.get("ETag"),
                "last_modified": response.headers.get("Last-Modified"),
            }

        response.raise_for_status()

        return {
            "status_code": response.status_code,
            "content": response.content,
            "etag": response.headers.get("ETag"),
            "last_modified": response.headers.get("Last-Modified"),
        }