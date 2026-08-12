---
id: api-spec-document-ingestion-task-status
type: concept
title: Document Ingestion Task Status
description: This document contains a JSON-formatted status report for a completed
  document ingestion process, including metadata such as processing timestamps, token
  estimates, source directories, and success metrics for the linux-man-pages source.
category: api-spec
tags:
- Document Ingestion
- Metadata
- JSON
- Status Report
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 4ccdc7412775.json
---

{
  "completion_tokens_estimate": 114,
  "created_at": 1786487763.4953272,
  "current_source": "",
  "discovered": 60,
  "error": null,
  "failed": 3,
  "fetched": 0,
  "finished_at": 1786487851.4492192,
  "id": "4ccdc7412775",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Ingestion completed",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 2,
  "progress_percent": 100,
  "prompt_tokens_estimate": 366,
  "rate_limit_hits": 4,
  "result": {
    "indexed_documents": 2,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786487763.498328,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 480,
  "type": "ingest"
}