---
id: api-spec-ingestion-pipeline-status-and-progress-metadata
type: concept
title: Ingestion Pipeline Status and Progress Metadata
description: This document represents a JSON status payload for a documentation ingestion
  pipeline. It details the current stage of converting cached raw Kubernetes data
  into knowledge files, including progress metrics such as processed documents and
  active run parameters.
category: api-spec
tags:
- Data Ingestion
- Kubernetes Documentation
- Pipeline Monitoring
- Knowledge Processing
source:
  name: Ingested document
  url: ''
created_at: '2026-08-12'
updated_at: '2026-08-12'
aliases: []
related: []
document_type: API Spec
trust_level: Medium
source_file: 295ad44bd020.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786530689.7185838,
  "current_source": "",
  "discovered": 50,
  "error": null,
  "failed": 0,
  "fetched": 50,
  "finished_at": null,
  "id": "295ad44bd020",
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
  "started_at": 1786530689.7196329,
  "status": "running",
  "total_documents": 50,
  "total_tokens_estimate": 0,
  "type": "ingest"
}