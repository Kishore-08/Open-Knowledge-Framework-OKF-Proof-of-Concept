---
id: api-spec-ingestion-job-status-and-progress-metadata
type: concept
title: Ingestion Job Status and Progress Metadata
description: This document contains execution metadata and progress metrics for a
  documentation ingestion job. It details the status of 50 crawled Python documents
  being processed, including timestamps, file counts, and cache directories.
category: api-spec
tags:
- Data Ingestion
- Metadata
- Python Documentation
- Job Status
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: 5a752c3d5912.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786383801.6818833,
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 50,
  "finished_at": null,
  "id": "5a752c3d5912",
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
  "processed": 50,
  "progress_percent": 100,
  "prompt_tokens_estimate": 0,
  "result": null,
  "started_at": 1786383801.6828582,
  "status": "running",
  "total_documents": 50,
  "total_tokens_estimate": 0,
  "type": "ingest"
}