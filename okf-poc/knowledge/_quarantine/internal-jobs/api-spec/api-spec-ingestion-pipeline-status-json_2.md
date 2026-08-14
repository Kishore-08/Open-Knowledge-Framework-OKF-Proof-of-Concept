---
id: api-spec-ingestion-pipeline-status-json
type: concept
title: Ingestion Pipeline Status JSON
description: This document contains a JSON-formatted status report for a documentation
  ingestion pipeline. It tracks processing metrics such as token estimates, failed
  documents, progress percentage, and operational stages for the linux-man-pages source.
category: api-spec
tags:
- Ingestion Pipeline
- Documentation Processing
- Status Tracking
- JSON Data
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: d0b3944b3c86.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786489668.6348886,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "d0b3944b3c86",
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
  "started_at": 1786489668.6355793,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}