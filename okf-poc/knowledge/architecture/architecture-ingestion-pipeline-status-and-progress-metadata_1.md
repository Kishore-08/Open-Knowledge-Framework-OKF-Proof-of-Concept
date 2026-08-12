---
id: architecture-ingestion-pipeline-status-and-progress-metadata
type: concept
title: Ingestion Pipeline Status and Progress Metadata
description: This document represents a state or status report of a documentation
  ingestion and processing pipeline. It tracks progress, execution times, stages,
  and various metrics such as processed document counts and token estimates. The current
  run is in the converting stage with 48% progress.
category: architecture
tags:
- Ingestion Pipeline
- Metadata
- Status Tracking
- Data Processing
source:
  name: Ingested document
  url: ''
created_at: '2026-08-12'
updated_at: '2026-08-12'
aliases: []
related: []
document_type: Architecture
trust_level: Medium
source_file: d2a0eb32e885.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786518860.4795687,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "d2a0eb32e885",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": []
  },
  "processed": 0,
  "progress_percent": 48,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Starting the ingestion pipeline from the cache folder",
  "started_at": 1786518860.480264,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}