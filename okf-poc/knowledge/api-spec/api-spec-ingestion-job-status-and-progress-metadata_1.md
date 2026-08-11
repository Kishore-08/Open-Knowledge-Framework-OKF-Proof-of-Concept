---
id: api-spec-ingestion-job-status-and-progress-metadata
type: concept
title: Ingestion Job Status and Progress Metadata
description: This JSON document provides the real-time status and telemetry of an
  active document ingestion and indexing job. It tracks key metrics such as processed
  documents, token estimates, progress percentage, and specific pipeline stages like
  indexing knowledge into Qdrant.
category: api-spec
tags:
- Data Ingestion
- Qdrant
- Indexing
- Metadata
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: d6ed8d808191.json
---

{
  "completion_tokens_estimate": 136,
  "created_at": 1786444835.7079487,
  "current_source": "Feedback",
  "discovered": 60,
  "error": null,
  "failed": 2,
  "fetched": 59,
  "finished_at": null,
  "id": "d6ed8d808191",
  "indexed": 229,
  "indexed_documents": 229,
  "message": "Indexed 229/1495 document(s) \u2014 1 failed",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 65,
  "progress_percent": 91,
  "prompt_tokens_estimate": 367,
  "rate_limit_hits": 7,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786444835.708815,
  "status": "running",
  "total_documents": 1495,
  "total_tokens_estimate": 503,
  "type": "ingest"
}