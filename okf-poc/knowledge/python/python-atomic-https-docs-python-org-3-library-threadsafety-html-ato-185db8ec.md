---
id: python-atomic-https-docs-python-org-3-library-threadsafety-html-ato-185db8ec
type: concept
title: Atomic[¶](https://docs.python.org/3/library/threadsafety.html#atomic "Link
  to this heading")
description: A function or operation that appears [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation)
  with
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Atomic[¶](https://docs.python.org/3/library/threadsafety.html#atomic "Link to this heading")

A function or operation that appears [atomic](https://docs.python.org/3/glossary.html#term-atomic-operation) with
respect to other threads - it executes instantaneously from the perspective
of other threads. This is the strongest form of thread safety.

Example: [`PyMutex_IsLocked()`](https://docs.python.org/3/c-api/synchronization.html#c.PyMutex_IsLocked "PyMutex_IsLocked") performs an atomic read of the mutex
state and can be called from any thread at any time.