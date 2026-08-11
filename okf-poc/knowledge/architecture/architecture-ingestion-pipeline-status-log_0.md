---
id: architecture-ingestion-pipeline-status-log
type: concept
title: Ingestion Pipeline Status Log
description: This document represents a JSON status log tracking the progress of a
  documentation ingestion pipeline. It details the current stage of 'converting' crawled
  Python documentation from a cache directory into a knowledge directory, showing
  a progress of 48%.
category: architecture
tags:
- Ingestion Pipeline
- Data Crawling
- Python Documentation
- System Status
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: Architecture
trust_level: Medium
source_file: ed40f48635bd.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786389303.4160883,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "ed40f48635bd",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "python"
    ]
  },
  "processed": 0,
  "progress_percent": 48,
  "prompt_tokens_estimate": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Starting the ingestion pipeline from the cache folder",
  "started_at": 1786389303.4172792,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}