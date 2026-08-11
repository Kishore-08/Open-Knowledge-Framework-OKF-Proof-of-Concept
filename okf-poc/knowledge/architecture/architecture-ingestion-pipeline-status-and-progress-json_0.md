---
id: architecture-ingestion-pipeline-status-and-progress-json
type: concept
title: Ingestion Pipeline Status and Progress JSON
description: This document contains a JSON status object representing the progress
  of a documentation ingestion pipeline. It tracks execution parameters, current stage,
  timestamp records, and processing statistics showing the pipeline is currently in
  the converting stage.
category: architecture
tags:
- Ingestion Pipeline
- Data Processing
- Metadata
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
source_file: 3725aa8fac56.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786397922.2455049,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "3725aa8fac56",
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
  "started_at": 1786397922.2469864,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}