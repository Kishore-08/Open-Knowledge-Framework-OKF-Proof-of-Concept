# Documentation

This directory contains durable design documentation for the OKF proof of
concept. Setup, usage, API routes, and evaluation instructions live in the
project [README](../README.md).

## Documents

- [Architecture](ARCHITECTURE.md) — system boundaries, data flow, storage,
  background jobs, retrieval, and failure behavior.
- [OKF and RAG frameworks](comparative_study.md) — the role of portable OKF
  documents relative to orchestration libraries such as LlamaIndex and
  LangChain.

Implementation histories, issue-resolution logs, and feature summaries are
intentionally not kept here. Git history, commit messages, tests, and issue
tracking are better sources for time-specific implementation details.

## Maintenance

- Update architecture documentation in the same change that alters a system
  boundary, persistent store, or end-to-end flow.
- Keep commands and endpoint inventories in the root README to avoid parallel
  copies becoming inconsistent.
- Use descriptive filenames and never create documents whose names differ only
  by letter case.
- Describe current behavior; do not turn this directory into a changelog.
