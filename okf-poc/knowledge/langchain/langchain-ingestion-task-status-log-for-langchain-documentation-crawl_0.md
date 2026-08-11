---
id: langchain-ingestion-task-status-log-for-langchain-documentation-crawl
type: concept
title: Ingestion Task Status Log for LangChain Documentation Crawl
description: This document represents a system execution log for a running 'ingest'
  task. It details the status, parameters, and progress of processing crawled LangChain
  documentation into a knowledge directory.
category: langchain
tags:
- data ingestion
- web crawling
- system logs
- metadata
source:
  name: Ingested document
  url: ''
created_at: '2026-08-10'
updated_at: '2026-08-10'
aliases: []
related: []
document_type: LangChain
trust_level: Medium
source_file: 59dad85a98af.json
---

{
  "completion_tokens_estimate": 0,
  "created_at": 1786377672.3422098,
  "discovered": 0,
  "error": null,
  "failed": 0,
  "fetched": 0,
  "finished_at": null,
  "id": "59dad85a98af",
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
  "started_at": 1786377672.3456647,
  "status": "running",
  "total_documents": 0,
  "total_tokens_estimate": 0,
  "type": "ingest"
}