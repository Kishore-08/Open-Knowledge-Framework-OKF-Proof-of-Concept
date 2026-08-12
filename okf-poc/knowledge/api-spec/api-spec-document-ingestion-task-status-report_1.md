---
id: api-spec-document-ingestion-task-status-report
type: concept
title: Document Ingestion Task Status Report
description: This document provides a JSON-formatted status report of a completed
  document ingestion process, specifically detailing metrics such as processed documents,
  token estimates, and stage progression. It highlights the successful indexing of
  Linux man pages into the knowledge base.
category: api-spec
tags:
- document ingestion
- status report
- knowledge base
- Linux man pages
- metrics
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: c080455c5c93.json
---

{
  "completion_tokens_estimate": 135,
  "created_at": 1786486225.1021855,
  "current_source": "",
  "discovered": 60,
  "error": null,
  "failed": 3,
  "fetched": 0,
  "finished_at": 1786486316.541245,
  "id": "c080455c5c93",
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
  "prompt_tokens_estimate": 462,
  "rate_limit_hits": 4,
  "result": {
    "indexed_documents": 2,
    "status": "success"
  },
  "stage": "completed",
  "stage_message": "Ingestion completed \u2014 knowledge is stored in OKF format and indexed",
  "started_at": 1786486225.1030393,
  "status": "completed",
  "total_documents": 2,
  "total_tokens_estimate": 597,
  "type": "ingest"
}