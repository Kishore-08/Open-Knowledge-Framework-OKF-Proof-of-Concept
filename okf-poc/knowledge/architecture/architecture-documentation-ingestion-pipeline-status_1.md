---
id: architecture-documentation-ingestion-pipeline-status
type: concept
title: Documentation Ingestion Pipeline Status
description: This document details the execution status of an active data ingestion
  pipeline task. The process is currently converting crawled Kubernetes documentation
  into OKF knowledge files, with 50 documents successfully processed at a 69% progress
  rate. It provides metadata on the ingestion parameters, exec
category: architecture
tags:
- data ingestion
- kubernetes
- knowledge base
- pipeline status
source:
  name: Ingested document
  url: ''
created_at: '2026-08-13'
updated_at: '2026-08-13'
aliases: []
related: []
document_type: Architecture
trust_level: Medium
source_file: 936d182c9cf6.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786613446.1796145,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 50,
  "finished_at": null,
  "id": "936d182c9cf6",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Processing crawled documentation",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "kubernetes"
    ]
  },
  "processed": 50,
  "progress_percent": 69,
  "prompt_tokens_estimate": 0,
  "rate_limit_hits": 0,
  "result": null,
  "stage": "converting",
  "stage_message": "Converting cached raw data into OKF knowledge files",
  "started_at": 1786613446.1815956,
  "status": "running",
  "total_documents": 50,
  "total_tokens_estimate": 0,
  "type": "ingest"
}