---
id: api-spec-ingestion-and-vector-indexing-status-job
type: concept
title: Ingestion and Vector Indexing Status Job
description: This document represents a JSON status payload for a running data ingestion
  and indexing job. It tracks the progress of importing Python-related knowledge concepts
  into a Qdrant vector database, showing status metrics such as processing progress,
  token estimates, and current execution stage.
category: api-spec
tags:
- Vector Database
- Data Ingestion
- Qdrant
- RAG Pipeline
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
source_file: 71f69579c023.json
---

{
  "completion_tokens_estimate": 114,
  "created_at": 1786395270.190593,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "71f69579c023",
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
  "prompt_tokens_estimate": 358,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786395270.1922722,
  "status": "running",
  "total_documents": 2,
  "total_tokens_estimate": 472,
  "type": "ingest"
}