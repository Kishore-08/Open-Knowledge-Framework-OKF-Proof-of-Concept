---
id: architecture-ingestion-pipeline-job-status-metadata
type: concept
title: Ingestion Pipeline Job Status Metadata
description: This document contains the JSON metadata for an active ingestion pipeline
  process that is converting cached documentation. It details the job's current progress,
  stage status, and source material, specifically referencing the ingestion of Linux
  man pages.
category: architecture
tags:
- Data Ingestion
- Pipeline Status
- Linux Man Pages
- JSON Metadata
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Architecture
trust_level: Medium
source_file: 041ea430e3a3.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786441269.2767766,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "041ea430e3a3",
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
  "started_at": 1786441269.2772355,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}