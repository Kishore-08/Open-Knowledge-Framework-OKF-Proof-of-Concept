---
id: api-spec-knowledge-base-ingestion-job-status-report
type: concept
title: Knowledge Base Ingestion Job Status Report
description: This document is a JSON log detailing the successful completion of a
  knowledge base ingestion job. It tracks metrics such as token estimates, processing
  progress, and indexing results for Kubernetes-related sources. The ingestion process
  completed successfully, indexing two documents into the system
category: api-spec
tags:
- Knowledge Ingestion
- Data Indexing
- Kubernetes
- System Log
source:
  name: Ingested document
  url: ''
created_at: '2026-08-13'
updated_at: '2026-08-13'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: 22b120d814cc.json
---

{
  "completion_tokens_estimate": 106,
  "created_at": 1786608253.8161826,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 2,
  "fetched": 0,
  "finished_at": 1786608361.5974991,
  "id": "22b120d814cc",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Ingestion completed",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "kubernetes"
    ]
  },
  "processed": 2,
  "progress_percent": 100,
  "prompt_tokens_estimate": 384,
  "rate_limit_hits": 0,
  "result": {
    "indexed_documents": 2,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786608253.8176494,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 490,
  "type": "ingest"
}