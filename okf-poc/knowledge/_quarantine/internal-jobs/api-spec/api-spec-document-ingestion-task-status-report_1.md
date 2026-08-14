---
id: api-spec-document-ingestion-task-status-report
type: concept
title: Document Ingestion Task Status Report
description: This JSON document provides a status report for a completed document
  ingestion task. It includes metrics such as processed document counts, token estimates,
  timestamps, and execution parameters.
category: api-spec
tags:
- document ingestion
- status report
- metrics
- knowledge base
source:
  name: Ingested document
  url: ''
created_at: '2026-08-12'
updated_at: '2026-08-12'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 9e033734d16f.json
---

{
  "completion_tokens_estimate": 130,
  "created_at": 1786493253.3223424,
  "current_source": "",
  "discovered": 0,
  "error": null,
  "failed": 3,
  "fetched": 0,
  "finished_at": 1786493285.281165,
  "id": "9e033734d16f",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Ingestion completed",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": []
  },
  "processed": 3,
  "progress_percent": 100,
  "prompt_tokens_estimate": 387,
  "rate_limit_hits": 6,
  "result": {
    "indexed_documents": 3,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786493253.3239288,
  "status": "completed",
  "total_documents": 3,
  "total_tokens_estimate": 517,
  "type": "ingest"
}