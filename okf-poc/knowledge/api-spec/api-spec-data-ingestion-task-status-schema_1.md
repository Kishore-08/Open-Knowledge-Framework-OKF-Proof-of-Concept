---
id: api-spec-data-ingestion-task-status-schema
type: concept
title: Data Ingestion Task Status Schema
description: This document represents a JSON status object for an ongoing data ingestion
  task processing LangChain crawl documentation. It tracks metrics such as processing
  progress, document and token estimates, task parameters, and execution timestamps.
category: api-spec
tags:
- Data Ingestion
- LangChain
- Task Monitoring
- JSON Schema
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: cc17dfd3cdbc.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786373049.7675276,
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "cc17dfd3cdbc",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "langchain"
    ]
  },
  "processed": 0,
  "progress_percent": 0,
  "prompt_tokens_estimate": 0,
  "result": null,
  "started_at": 1786373049.7686336,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}