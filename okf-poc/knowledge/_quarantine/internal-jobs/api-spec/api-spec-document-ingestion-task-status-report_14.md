---
id: api-spec-document-ingestion-task-status-report
type: concept
title: Document Ingestion Task Status Report
description: This document contains a JSON-formatted status report for a completed
  data ingestion process involving Linux man pages. It details execution metrics such
  as token estimates, processing times, error counts, and indexing status.
category: api-spec
tags:
- data ingestion
- status report
- Linux man pages
- indexing
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 7aeb256218c8.json
---

{
  "completion_tokens_estimate": 122,
  "created_at": 1786474593.2895262,
  "current_source": "",
  "discovered": 60,
  "error": null,
  "failed": 3,
  "fetched": 0,
  "finished_at": 1786474682.2946875,
  "id": "7aeb256218c8",
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
  "started_at": 1786474593.291029,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 488,
  "type": "ingest"
}