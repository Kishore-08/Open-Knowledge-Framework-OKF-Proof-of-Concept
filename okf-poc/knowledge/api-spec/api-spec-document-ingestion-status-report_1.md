---
id: api-spec-document-ingestion-status-report
type: concept
title: Document Ingestion Status Report
description: This document contains a JSON-formatted execution log and status report
  for a completed document ingestion job. It tracks metrics such as processed documents,
  token estimates, rate limit hits, and indexing success for the linux-man-pages source.
category: api-spec
tags:
- Document Ingestion
- Status Report
- JSON Data
- Job Metrics
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: bfd6658d5e69.json
---

{
  "completion_tokens_estimate": 112,
  "created_at": 1786488318.1957068,
  "current_source": "",
  "discovered": 60,
  "error": null,
  "failed": 3,
  "fetched": 0,
  "finished_at": 1786488405.9402013,
  "id": "bfd6658d5e69",
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
  "prompt_tokens_estimate": 387,
  "rate_limit_hits": 4,
  "result": {
    "indexed_documents": 2,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786488318.196362,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 499,
  "type": "ingest"
}