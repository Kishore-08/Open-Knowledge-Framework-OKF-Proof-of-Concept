---
id: api-spec-ingestion-and-indexing-job-status-schema
type: concept
title: Ingestion and Indexing Job Status Schema
description: This document represents a JSON status payload for a running knowledge
  ingestion job. It details the progress of indexing 'linux-man-pages' into a Qdrant
  vector database, including document counts, token estimates, and current execution
  stages.
category: api-spec
tags:
- Data Ingestion
- Qdrant
- Vector Search
- Job Monitoring
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: 041ea430e3a3.json
---

{
  "completion_tokens_estimate": 124,
  "created_at": 1786441269.2767766,
  "current_source": "Deprecated annotation",
  "discovered": 60,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "041ea430e3a3",
  "indexed": 140,
  "indexed_documents": 140,
  "message": "Indexed 140/1121 document(s)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 2,
  "progress_percent": 91,
  "prompt_tokens_estimate": 367,
  "rate_limit_hits": 3,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786441269.2772355,
  "status": "running",
  "total_documents": 1121,
  "total_tokens_estimate": 491,
  "type": "ingest"
}