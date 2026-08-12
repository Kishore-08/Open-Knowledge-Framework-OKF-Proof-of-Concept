---
id: api-spec-document-ingestion-status-json
type: concept
title: Document Ingestion Status JSON
description: This document contains a JSON-formatted status report for a document
  indexing pipeline. It tracks metrics such as processed documents, failed counts,
  progress percentage, and current execution stages for a knowledge base import.
category: api-spec
tags:
- Document Indexing
- Pipeline Status
- JSON Data
- Knowledge Base
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 21aa420c3c19.json
---

{
  "completion_tokens_estimate": 153,
  "created_at": 1786440705.2595544,
  "current_source": "Networking and security",
  "discovered": 60,
  "error": null,
  "failed": 1,
  "fetched": 0,
  "finished_at": null,
  "id": "21aa420c3c19",
  "indexed": 332,
  "indexed_documents": 332,
  "message": "Indexed 332/1119 document(s)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 2,
  "progress_percent": 92,
  "prompt_tokens_estimate": 415,
  "rate_limit_hits": 10,
  "result": null,
  "stage": "indexing",
  "stage_message": "Indexing OKF knowledge into Qdrant",
  "started_at": 1786440705.2610922,
  "status": "running",
  "total_documents": 1119,
  "total_tokens_estimate": 568,
  "type": "ingest"
}