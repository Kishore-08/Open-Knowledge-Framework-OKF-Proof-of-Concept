---
id: api-spec-knowledge-ingestion-job-status-report
type: concept
title: Knowledge Ingestion Job Status Report
description: This document is a system execution log detailing the successful completion
  of a knowledge ingestion process. It records the indexing of two Kubernetes documents,
  storing them in OKF format with zero errors.
category: api-spec
tags:
- Data Ingestion
- Kubernetes
- Indexing
- System Logs
source:
  name: Ingested document
  url: ''
created_at: '2026-08-13'
updated_at: '2026-08-13'
aliases: []
related: []
document_type: API Spec
trust_level: High
source_file: 5f0d78e692b7.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786606162.3259244,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 2,
  "fetched": 0,
  "finished_at": 1786606250.2879932,
  "id": "5f0d78e692b7",
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
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": {
    "indexed_documents": 2,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786606162.3287606,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 0,
  "type": "ingest"
}