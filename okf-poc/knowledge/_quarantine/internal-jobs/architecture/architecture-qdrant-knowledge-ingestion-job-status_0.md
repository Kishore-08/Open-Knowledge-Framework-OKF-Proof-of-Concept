---
id: architecture-qdrant-knowledge-ingestion-job-status
type: concept
title: Qdrant Knowledge Ingestion Job Status
description: This document is a system status log detailing the progress of an active
  knowledge ingestion and indexing pipeline. It shows that 386 out of 597 Kubernetes-related
  documents have been successfully indexed into Qdrant, reaching 95% progress. The
  log includes performance metrics such as token estimate
category: architecture
tags:
- Knowledge Ingestion
- Qdrant
- Kubernetes
- Vector Search
- Data Indexing
source:
  name: Ingested document
  url: ''
created_at: '2026-08-14'
updated_at: '2026-08-14'
aliases: []
related: []
document_type: Architecture
trust_level: High
source_file: 936d182c9cf6.json
---

{
  "completion_tokens_estimate": 144,
  "created_at": 1786613446.1796145,
  "current_source": "Declarative vs imperative",
  "discovered": 100,
  "error": null,
  "failed": 0,
  "fetched": 50,
  "finished_at": null,
  "id": "936d182c9cf6",
  "indexed": 386,
  "indexed_documents": 386,
  "message": "Indexed 386/597 document(s)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "kubernetes"
    ]
  },
  "processed": 52,
  "progress_percent": 95,
  "prompt_tokens_estimate": 366,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786613446.1815956,
  "status": "running",
  "total_documents": 597,
  "total_tokens_estimate": 510,
  "type": "ingest"
}