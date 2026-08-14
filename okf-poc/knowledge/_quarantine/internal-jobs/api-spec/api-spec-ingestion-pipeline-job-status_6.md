---
id: api-spec-ingestion-pipeline-job-status
type: concept
title: Ingestion Pipeline Job Status
description: This document represents the JSON status payload for a running knowledge
  ingestion and vector database indexing job. It tracks progress metrics, processed
  document counts, token usage estimates, and pipeline stage information.
category: api-spec
tags:
- Vector Database
- Data Ingestion
- Job Status
- Python
- Qdrant
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 3725aa8fac56.json
---

{
  "completion_tokens_estimate": 134,
  "created_at": 1786397922.2455049,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "3725aa8fac56",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Indexing concepts into the vector database",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "python"
    ]
  },
  "processed": 2,
  "progress_percent": 92,
  "prompt_tokens_estimate": 357,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786397922.2469864,
  "status": "running",
  "total_documents": 2,
  "total_tokens_estimate": 491,
  "type": "ingest"
}