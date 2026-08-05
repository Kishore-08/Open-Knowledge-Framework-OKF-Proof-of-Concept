#!/usr/bin/env python3
"""
Crawl official documentation sources (Phase 2 - data collection).

Discover pages from sitemap.xml / robots.txt, download them with a polite delay,
and cache the raw HTML under `cache/<source>/`. Source definitions come from
`config/sources.yaml` (or `--source`/`--url` overrides).

Usage:
    python -m scripts.crawl_docs                 # all enabled sources
    python -m scripts.crawl_docs --source kubernetes
    python -m scripts.crawl_docs --url https://kubernetes.io/docs/concepts/workloads/
"""

import argparse
import asyncio
import os
import sys
from typing import List

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import yaml

from app.core.config import settings
from app.ingestion.crawler import DocsCrawler


def load_sources(sources_config: str) -> List[dict]:
    if not os.path.exists(sources_config):
        return []
    with open(sources_config, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data.get("sources", [])


async def crawl_sources(source_name: str | None, url: str | None) -> None:
    sources = load_sources(settings.SOURCES_CONFIG)
    crawler = DocsCrawler(delay=0.5)

    if url:
        # Ad-hoc single-URL crawl (no sitemap discovery).
        name = source_name or "adhoc"
        result = await crawler.crawl_source(name, [url])
        print(f"📥 {name}: fetched={result.fetched} cached={result.cached} failed={result.failed}")
        return

    for source in sources:
        if not source.get("enabled", True):
            print(f"⏭️ Skipping disabled source: {source['name']}")
            continue
        if source_name and source["name"] != source_name:
            continue
        print(f"🔎 Crawling {source['name']} ({source['base_url']})...")
        result = await crawler.crawl(
            source_name=source["name"],
            base_url=source["base_url"],
            sitemap_urls=[source["sitemap_url"]] if source.get("sitemap_url") else None,
            url_filter=source.get("url_filter"),
            max_urls=source.get("max_urls", 500),
        )
        print(
            f"📊 {source['name']}: discovered={len(result.urls)} "
            f"fetched={result.fetched} cached={result.cached} failed={result.failed}"
        )
        if result.errors:
            print("⚠️ Errors:")
            for err in result.errors[:5]:
                print(f"   {err}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Crawl official documentation sources.")
    parser.add_argument("--source", help="Only crawl this source name from sources.yaml")
    parser.add_argument("--url", help="Crawl a single URL directly (bypasses sitemap)")
    args = parser.parse_args()

    asyncio.run(crawl_sources(args.source, args.url))


if __name__ == "__main__":
    main()
