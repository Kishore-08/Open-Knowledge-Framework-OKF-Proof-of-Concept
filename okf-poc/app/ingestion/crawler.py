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
    cached: int = 0
    failed: int = 0
    urls: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)


def _url_hash(url: str) -> str:
    return hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]


def cache_path(source: str, url: str) -> str:
    """Local path for the cached raw HTML of a URL."""
    root = os.path.join(settings.CACHE_DIR, _safe_name(source))
    os.makedirs(root, exist_ok=True)
    return os.path.join(root, f"{_url_hash(url)}.html")


def _safe_name(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9-_]+", "-", name).strip("-").lower() or "source"


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

    async def crawl_source(self, source_name: str, urls: List[str]) -> CrawlResult:
        """
        Fetch each discovered URL and store raw HTML in the cache.
        Reuses cached pages when present (cache-aside pattern).
        """
        result = CrawlResult(source_name=source_name, urls=urls)
        for url in urls:
            target = cache_path(source_name, url)
            if os.path.exists(target) and os.path.getsize(target) > 0:
                result.cached += 1
                continue
            try:
                content = await self._fetch(url)
                with open(target, "wb") as f:
                    f.write(content)
                result.fetched += 1
            except Exception as exc:  # noqa: BLE001 - tolerate individual page failures
                result.failed += 1
                result.errors.append(f"{url}: {exc}")
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
    ) -> CrawlResult:
        """Discover + fetch a documentation source end to end."""
        if urls is None:
            urls = await self.discover(base_url, sitemap_urls, url_filter, max_urls)
        return await self.crawl_source(source_name, urls)
