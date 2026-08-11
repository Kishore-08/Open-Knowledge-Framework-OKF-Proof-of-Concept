---
id: api-spec-ingestion-and-vector-database-indexing-status
type: concept
title: Ingestion and Vector Database Indexing Status
description: This document represents the execution state of an ingestion process
  indexing Kubernetes knowledge concepts into a Qdrant vector database. It details
  various execution metrics, including processing progress, token estimates, and the
  active running status of the indexing stage.
category: api-spec
tags:
- Vector Database
- Data Ingestion
- Qdrant
- Kubernetes
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: 2c74974e7374.json
---

{
  "completion_tokens_estimate": 118,
  "created_at": 1786398962.3954916,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "2c74974e7374",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Indexing concepts into the vector database",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "kubernetes"
    ]
  },
  "processed": 2,
  "progress_percent": 92,
  "prompt_tokens_estimate": 359,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786398962.3985777,
  "status": "running",
  "total_documents": 2,
  "total_tokens_estimate": 477,
  "type": "ingest"
}