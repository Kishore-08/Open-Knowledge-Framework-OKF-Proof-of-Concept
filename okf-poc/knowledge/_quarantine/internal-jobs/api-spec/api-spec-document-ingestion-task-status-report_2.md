---
id: api-spec-document-ingestion-task-status-report
type: concept
title: Document Ingestion Task Status Report
description: This document contains a JSON-formatted status report for a completed
  document ingestion process, including metadata such as processing stage, document
  counts, token estimates, and runtime parameters. It indicates that the ingestion
  of Linux man pages finished successfully with three indexed documen
category: api-spec
tags:
- Document Ingestion
- Task Status
- Metadata
- JSON
source:
  name: Ingested document
  url: ''
created_at: '2026-08-12'
updated_at: '2026-08-12'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: d0b3944b3c86.json
---

{
  "completion_tokens_estimate": 119,
  "created_at": 1786489668.6348886,
  "current_source": "",
  "discovered": 60,
  "error": null,
  "failed": 4,
  "fetched": 0,
  "finished_at": 1786489770.961624,
  "id": "d0b3944b3c86",
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
  "processed": 3,
  "progress_percent": 100,
  "prompt_tokens_estimate": 367,
  "rate_limit_hits": 6,
  "result": {
    "indexed_documents": 3,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786489668.6355793,
  "status": "completed",
  "total_documents": 3,
  "total_tokens_estimate": 486,
  "type": "ingest"
}