---
id: log-ingestion-pipeline-status-and-rate-limit-log
type: concept
title: Ingestion Pipeline Status and Rate Limit Log
description: This document represents a JSON status log of an active data ingestion
  and indexing process targeting Linux man pages. It records a temporary rate limit
  error (HTTP 429) encountered while attempting to embed a systemd-environment-d-generator
  page, along with overall job progress and configuration pa
category: log
tags:
- Data Ingestion
- API Rate Limiting
- Linux Man Pages
- Systemd
source:
  name: Ingested document
  url: ''
created_at: '2026-08-11'
updated_at: '2026-08-11'
aliases: []
related: []
document_type: Log
trust_level: Medium
source_file: a42725f4a900.json
---

{
  "completion_tokens_estimate": 118,
  "created_at": 1786477627.587353,
  "current_source": "C \u00a0 \u00a0 \u00a0 \u00a0 [top](https://man7.org/linux/man-pages/man7/30-systemd-environment-d-generator.7.html#top_of_page)",
  "discovered": 60,
  "error": null,
  "failed": 4,
  "fetched": 59,
  "finished_at": null,
  "id": "a42725f4a900",
  "indexed": 0,
  "indexed_documents": 0,
  "message": "\u26a0\ufe0f Embedding rate limit (429) hit for 'linux-man-pages-c-top-https-man7-org-linux-man-pages-man7-30-systemd-environ-deac643f', retrying in 6s (attempt 2/3)",
  "params": {
    "cache_dir": "cache",
    "knowledge_dir": "knowledge",
    "sources": [
      "linux-man-pages"
    ]
  },
  "processed": 88,
  "progress_percent": 90,
  "prompt_tokens_estimate": 374,
  "rate_limit_hits": 8,
  "result": null,
  "stage": "indexing",
  "stage_message": "Rate limited on 'C \u00a0 \u00a0 \u00a0 \u00a0 [top](https://man7.org/linux/man-pages/man7/30-systemd-environment-d-generator.7.html#top_of_page)' \u2014 retrying in 6s",
  "started_at": 1786477627.587923,
  "status": "running",
  "total_documents": 464,
  "total_tokens_estimate": 492,
  "type": "ingest"
}