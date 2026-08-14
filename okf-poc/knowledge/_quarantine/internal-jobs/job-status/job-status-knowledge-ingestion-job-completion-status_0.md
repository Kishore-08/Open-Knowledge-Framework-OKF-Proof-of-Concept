---
id: job-status-knowledge-ingestion-job-completion-status
type: concept
title: Knowledge Ingestion Job Completion Status
description: This document is a JSON status report detailing the successful completion
  of a document ingestion and indexing process. It shows that two documents from a
  Kubernetes source were processed, indexed, and stored in OKF format. The report
  includes execution metrics such as timestamps, token estimates, a
category: job-status
tags:
- Data Ingestion
- Indexing
- Kubernetes
- OKF Format
source:
  name: Ingested document
  url: ''
created_at: '2026-08-13'
updated_at: '2026-08-13'
aliases: []
related: []
document_type: Job Status
trust_level: Medium
source_file: 178018d46240.json
---

{
  "completion_tokens_estimate": 113,
  "created_at": 1786612864.5457616,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": 1786612937.085337,
  "id": "178018d46240",
  "indexed": 2,
  "indexed_documents": 2,
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
  "prompt_tokens_estimate": 365,
  "rate_limit_hits": 0,
  "result": {
    "indexed_documents": 2,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786612864.549672,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 478,
  "type": "ingest"
}