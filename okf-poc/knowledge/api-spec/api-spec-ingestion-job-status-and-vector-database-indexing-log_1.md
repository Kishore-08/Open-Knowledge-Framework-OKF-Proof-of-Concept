---
id: api-spec-ingestion-job-status-and-vector-database-indexing-log
type: concept
title: Ingestion Job Status and Vector Database Indexing Log
description: This document represents the execution status and configuration of an
  ongoing data ingestion job. It details the indexing of Python-related knowledge
  concepts into a Qdrant vector database, including progress metrics, token estimations,
  and system stage updates.
category: api-spec
tags:
- Vector Database
- Data Ingestion
- Qdrant
- Metadata Log
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: High
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