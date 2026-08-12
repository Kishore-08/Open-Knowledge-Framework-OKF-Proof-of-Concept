---
id: langchain-ingestion-job-status-log
type: concept
title: LangChain Ingestion Job Status Log
description: This document contains a JSON-formatted execution status log for a document
  ingestion task involving LangChain knowledge sources. It tracks progress metrics,
  token estimations, timestamps, and completion states for saving an OKF file.
category: langchain
tags:
- LangChain
- Data Ingestion
- JSON Status Log
- Token Estimation
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: LangChain
trust_level: Medium
source_file: 50166fdd1bbd.json
---

{
  "completion_tokens_estimate": 120,
  "created_at": 1786383302.5742543,
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "50166fdd1bbd",
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
  "prompt_tokens_estimate": 327,
  "result": null,
  "started_at": 1786383302.580074,
  "status": "running",
  "total_documents": 1,
  "total_tokens_estimate": 447,
  "type": "ingest"
}