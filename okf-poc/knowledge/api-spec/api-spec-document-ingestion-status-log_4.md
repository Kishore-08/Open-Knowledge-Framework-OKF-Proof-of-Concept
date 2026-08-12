---
id: api-spec-document-ingestion-status-log
type: concept
title: Document Ingestion Status Log
description: This document contains a JSON-formatted status report of a document crawling
  and ingestion process. It tracks metrics such as discovered, fetched, indexed, and
  processed documents along with timestamps and configuration parameters.
category: api-spec
tags:
- document ingestion
- status monitoring
- crawling metrics
- knowledge base
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 25cabf949028.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786369169.1582313,
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "25cabf949028",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Formatting crawled HTML into OKF knowledge",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge"
  },
  "processed": 38,
  "progress_percent": 76,
  "prompt_tokens_estimate": 0,
  "result": null,
  "started_at": 1786369169.1599154,
  "status": "running",
  "total_documents": 50,
  "total_tokens_estimate": 0,
  "type": "ingest"
}