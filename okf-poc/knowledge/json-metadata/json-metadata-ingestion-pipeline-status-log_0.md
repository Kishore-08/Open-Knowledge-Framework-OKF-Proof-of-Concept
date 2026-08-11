---
id: json-metadata-ingestion-pipeline-status-log
type: concept
title: Ingestion Pipeline Status Log
description: This document represents a JSON status log tracking the execution of
  a documentation ingestion pipeline. It details the active processing stage of converting
  crawled Linux man-pages from a cache directory, showing a progress level of 48%
  with a running status.
category: json-metadata
tags:
- Data Ingestion
- Pipeline Status
- Linux Man Pages
- Metadata Analysis
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: JSON Metadata
trust_level: Medium
source_file: 7d2fcff8ddf6.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786445226.8790944,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "7d2fcff8ddf6",
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
  "started_at": 1786445226.8796117,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}