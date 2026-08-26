---
id: python-incompatible-https-docs-python-org-3-library-threadsafety-ht-185db8ec
type: concept
title: Incompatible[¶](https://docs.python.org/3/library/threadsafety.html#incompatible
  "Link to this heading")
description: A function or operation that cannot be made safe for concurrent use even
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Incompatible[¶](https://docs.python.org/3/library/threadsafety.html#incompatible "Link to this heading")

A function or operation that cannot be made safe for concurrent use even
with external synchronization. Incompatible code typically accesses
global state in an unsynchronized way and must only be called from a single
thread throughout the program’s lifetime.

Example: a function that modifies process-wide state such as signal handlers
or environment variables, where concurrent calls from any threads, even with
external locking, can conflict with the runtime or other libraries.