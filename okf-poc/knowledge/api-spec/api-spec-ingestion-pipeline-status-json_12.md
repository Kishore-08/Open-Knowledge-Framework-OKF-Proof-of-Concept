---
id: api-spec-ingestion-pipeline-status-json
type: concept
title: Ingestion Pipeline Status JSON
description: This document represents the JSON status output of a knowledge indexing
  pipeline. It tracks progress metrics such as processed documents, stage details,
  token estimates, and vector database integration for Python sources.
category: api-spec
tags:
- Vector Database
- Data Ingestion
- Pipeline Status
- Python Knowledge Base
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
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