---
id: langchain-ingestion-job-status-report
type: concept
title: LangChain Ingestion Job Status Report
description: This document contains a JSON-formatted status report for a running data
  ingestion job involving LangChain knowledge sources. It tracks progress metrics,
  token estimates, timestamps, and execution states for the processing task.
category: langchain
tags:
- LangChain
- Data Ingestion
- Job Status
- Token Estimation
- Pipeline Monitoring
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: LangChain
trust_level: Medium
source_file: 59dad85a98af.json
---

{
  "completion_tokens_estimate": 111,
  "created_at": 1786377672.3422098,
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "59dad85a98af",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "Saving OKF file 1/1",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "langchain"
    ]
  },
  "processed": 1,
  "progress_percent": 100,
  "prompt_tokens_estimate": 328,
  "result": null,
  "started_at": 1786377672.3456647,
  "status": "running",
  "total_documents": 1,
  "total_tokens_estimate": 439,
  "type": "ingest"
}