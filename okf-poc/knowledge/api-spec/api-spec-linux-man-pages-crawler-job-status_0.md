---
id: api-spec-linux-man-pages-crawler-job-status
type: concept
title: Linux Man Pages Crawler Job Status
description: This document contains a JSON status payload for a running background
  ingestion job crawling the linux-man-pages documentation source. It tracks metrics
  such as discovered, fetched, indexed, and failed documents along with progress percentage
  and stage details.
category: api-spec
tags:
- Linux
- Documentation Crawling
- Job Status
- Ingestion Pipeline
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 9a02035ae979.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786488448.4795587,
  "current_source": "linux-man-pages",
  "discovered": 60,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "9a02035ae979",
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
  "started_at": 1786488448.480441,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}