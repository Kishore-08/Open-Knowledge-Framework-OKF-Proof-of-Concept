---
id: api-spec-ingestion-job-status-schema
type: concept
title: Ingestion Job Status Schema
description: This document represents the JSON schema and execution status of a data
  ingestion and indexing job. It tracks progress, token estimates, and stages of loading
  python knowledge sources into a Qdrant vector database.
category: api-spec
tags:
- Vector Database
- Data Ingestion
- Qdrant
- JSON Schema
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: ed40f48635bd.json
---

{
  "completion_tokens_estimate": 123,
  "created_at": 1786389303.4160883,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "ed40f48635bd",
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
  "processed": 1,
  "progress_percent": 92,
  "prompt_tokens_estimate": 358,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786389303.4172792,
  "status": "running",
  "total_documents": 1,
  "total_tokens_estimate": 481,
  "type": "ingest"
}