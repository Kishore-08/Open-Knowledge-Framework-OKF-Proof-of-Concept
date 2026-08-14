---
id: api-spec-ingestion-pipeline-status-log
type: concept
title: Ingestion Pipeline Status Log
description: This document contains a JSON-formatted status log for a documentation
  crawling and ingestion pipeline. It tracks metrics such as processed items, errors,
  progress percentage, and operational parameters for the linux-man-pages source.
category: api-spec
tags:
- data ingestion
- pipeline status
- crawling
- log monitoring
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 4ccdc7412775.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786487763.4953272,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "4ccdc7412775",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 0,
  "progress_percent": 48,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Starting the ingestion pipeline from the cache folder",
  "started_at": 1786487763.498328,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}