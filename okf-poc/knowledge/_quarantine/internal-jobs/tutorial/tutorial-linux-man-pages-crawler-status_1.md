---
id: tutorial-linux-man-pages-crawler-status
type: concept
title: Linux Man Pages Crawler Status
description: This document represents the runtime status and metadata for a documentation
  crawling job targeting the linux-man-pages source. It tracks progress metrics such
  as discovered documents, failed requests, and current execution stages.
category: tutorial
tags:
- Linux
- Documentation
- Web Crawling
- Job Status
source:
  name: Ingested document
  url: ''
created_at: '2026-08-12'
updated_at: '2026-08-12'
aliases: []
related: []
document_type: Tutorial
trust_level: Medium
source_file: c63e466fa779.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786490549.7365599,
  "current_source": "linux-man-pages",
  "discovered": 60,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "c63e466fa779",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Crawling source linux-man-pages",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 0,
  "progress_percent": 10,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "downloading",
  "stage_message": "Downloading linux-man-pages documentation from the official website",
  "started_at": 1786490549.7374005,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}