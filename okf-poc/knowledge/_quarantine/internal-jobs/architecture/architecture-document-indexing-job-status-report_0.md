---
id: architecture-document-indexing-job-status-report
type: concept
title: Document Indexing Job Status Report
description: This document provides a JSON-formatted status report for an ongoing
  document indexing process, specifically tracking progress, token estimates, and
  error metrics for the linux-man-pages source. It shows that the job is currently
  running, having successfully indexed 140 out of 1121 total documents.
category: architecture
tags:
- Document Indexing
- Job Status
- Vector Database
- Qdrant
- Metrics
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Architecture
trust_level: Medium
source_file: 041ea430e3a3.json
---

{
  "completion_tokens_estimate": 124,
  "created_at": 1786441269.2767766,
  "current_source": "Deprecated annotation",
  "discovered": 60,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "041ea430e3a3",
  "indexed": 140,
  "indexed_documents": 140,
  "message": "Indexed 140/1121 document(s)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 2,
  "progress_percent": 91,
  "prompt_tokens_estimate": 367,
  "rate_limit_hits": 3,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786441269.2772355,
  "status": "running",
  "total_documents": 1121,
  "total_tokens_estimate": 491,
  "type": "ingest"
}