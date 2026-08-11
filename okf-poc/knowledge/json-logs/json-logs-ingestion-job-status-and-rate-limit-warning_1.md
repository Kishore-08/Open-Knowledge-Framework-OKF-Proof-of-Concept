---
id: json-logs-ingestion-job-status-and-rate-limit-warning
type: concept
title: Ingestion Job Status and Rate Limit Warning
description: This document contains the JSON status payload of an active data ingestion
  and indexing pipeline. It shows the progress of processing source documents, specifically
  highlighting that an embedding rate limit (HTTP 429) was encountered while processing
  a Kubernetes-related resource.
category: json-logs
tags:
- Data Ingestion
- Embedding APIs
- Rate Limiting
- Kubernetes Documentation
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: JSON Logs
trust_level: Medium
source_file: 7a614db9e3f4.json
---

{
  "completion_tokens_estimate": 125,
  "created_at": 1786448792.8067577,
  "current_source": "Adding custom resources",
  "discovered": 50,
  "error": null,
  "failed": 10,
  "fetched": 50,
  "finished_at": null,
  "id": "7a614db9e3f4",
  "indexed": 36,
  "indexed_documents": 36,
  "message": "\u26a0\ufe0f Embedding rate limit (429) hit for 'kubernetes-adding-custom-resources-0f516df7', retrying in 3s (attempt 1/3)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "python"
    ]
  },
  "processed": 52,
  "progress_percent": 90,
  "prompt_tokens_estimate": 374,
  "rate_limit_hits": 23,
  "result": null,
  "stage": "indexing",
  "stage_message": "Rate limited on 'Adding custom resources' \u2014 retrying in 3s",
  "started_at": 1786448792.8072796,
  "status": "running",
  "total_documents": 1492,
  "total_tokens_estimate": 499,
  "type": "ingest"
}