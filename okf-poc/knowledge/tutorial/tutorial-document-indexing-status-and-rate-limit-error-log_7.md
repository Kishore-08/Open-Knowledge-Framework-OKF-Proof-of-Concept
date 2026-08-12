---
id: tutorial-document-indexing-status-and-rate-limit-error-log
type: concept
title: Document Indexing Status and Rate Limit Error Log
description: This document contains a JSON-formatted status report for an ongoing
  document ingestion and indexing pipeline. It records metrics such as processed documents,
  progress percentage, and an encountered API rate limit error resulting in a retry
  state.
category: tutorial
tags:
- API Rate Limiting
- Data Ingestion
- Document Indexing
- Pipeline Status
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Tutorial
trust_level: Medium
source_file: 4bc298bcf43e.json
---

{
  "completion_tokens_estimate": 112,
  "created_at": 1786474974.524976,
  "current_source": "Code",
  "discovered": 29,
  "error": null,
  "failed": 29,
  "fetched": 29,
  "finished_at": null,
  "id": "4bc298bcf43e",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "\u26a0\ufe0f Embedding rate limit (429) hit for 'apache-airflow-code-a85da58d', retrying in 6s (attempt 2/3)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "apache-airflow"
    ]
  },
  "processed": 31,
  "progress_percent": 90,
  "prompt_tokens_estimate": 387,
  "rate_limit_hits": 60,
  "result": null,
  "stage": "indexing",
  "stage_message": "Rate limited on 'Code' \u2014 retrying in 6s",
  "started_at": 1786474974.5254433,
  "status": "running",
  "total_documents": 235,
  "total_tokens_estimate": 499,
  "type": "ingest"
}