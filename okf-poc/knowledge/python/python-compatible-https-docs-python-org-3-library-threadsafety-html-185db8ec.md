---
id: python-compatible-https-docs-python-org-3-library-threadsafety-html-185db8ec
type: concept
title: Compatible[¶](https://docs.python.org/3/library/threadsafety.html#compatible
  "Link to this heading")
description: A function or operation that is safe to call from multiple threads
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Compatible[¶](https://docs.python.org/3/library/threadsafety.html#compatible "Link to this heading")

A function or operation that is safe to call from multiple threads
*provided* the caller supplies appropriate external synchronization, for
example by holding a [lock](https://docs.python.org/3/glossary.html#term-lock) for the duration of each call. Without
such synchronization, concurrent calls may produce [race conditions](https://docs.python.org/3/glossary.html#term-race-condition) or [data races](https://docs.python.org/3/glossary.html#term-data-race).

Example: a function that reads from or writes to an object whose internal
state is not protected by a lock. Callers must ensure that no two threads
access the same object at the same time.