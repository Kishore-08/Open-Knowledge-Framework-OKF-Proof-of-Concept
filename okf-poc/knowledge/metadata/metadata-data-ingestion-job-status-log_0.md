---
id: metadata-data-ingestion-job-status-log
type: concept
title: Data Ingestion Job Status Log
description: This document represents a JSON status log for an active data ingestion
  process targeting LangChain documentation. It tracks execution metadata, including
  start times, processing progress, and configuration parameters such as directory
  paths and data sources.
category: metadata
tags:
- Data Ingestion
- LangChain
- Job Monitoring
- JSON Metadata
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: Metadata
trust_level: Medium
source_file: 50166fdd1bbd.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786383302.5742543,
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "50166fdd1bbd",
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
  "started_at": 1786383302.580074,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}