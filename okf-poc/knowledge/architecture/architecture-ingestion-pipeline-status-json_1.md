---
id: architecture-ingestion-pipeline-status-json
type: concept
title: Ingestion Pipeline Status JSON
description: This document contains a JSON-formatted status report for a documentation
  ingestion pipeline processing Linux man pages. It tracks metrics such as progress
  percentage, failed tasks, and source configuration parameters.
category: architecture
tags:
- pipeline status
- ingestion
- documentation processing
- Linux man pages
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Architecture
trust_level: Medium
source_file: c080455c5c93.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786486225.1021855,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "c080455c5c93",
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
  "started_at": 1786486225.1030393,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}