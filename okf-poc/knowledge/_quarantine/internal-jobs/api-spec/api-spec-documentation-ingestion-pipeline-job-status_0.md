---
id: api-spec-documentation-ingestion-pipeline-job-status
type: concept
title: Documentation Ingestion Pipeline Job Status
description: A JSON status payload representing an active documentation ingestion
  pipeline task. The task is currently in the 'converting' stage, processing crawled
  Kubernetes documentation from a cache directory into a knowledge directory.
category: api-spec
tags:
- Data Ingestion
- Kubernetes
- Pipeline Status
- JSON
source:
  name: Ingested document
  url: ''
created_at: '2026-08-13'
updated_at: '2026-08-13'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: 178018d46240.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786612864.5457616,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "178018d46240",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "kubernetes"
    ]
  },
  "processed": 0,
  "progress_percent": 48,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Starting the ingestion pipeline from the cache folder",
  "started_at": 1786612864.549672,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}