---
id: python-safe-on-distinct-objects-https-docs-python-org-3-library-thr-185db8ec
type: concept
title: Safe on distinct objects[¶](https://docs.python.org/3/library/threadsafety.html#safe-on-distinct-objects
  "Link to this heading")
description: A function or operation that is safe to call from multiple threads without
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Safe on distinct objects[¶](https://docs.python.org/3/library/threadsafety.html#safe-on-distinct-objects "Link to this heading")

A function or operation that is safe to call from multiple threads without
external synchronization, as long as each thread operates on a **different**
object. Two threads may call the function at the same time, but they must
not pass the same object (or objects that share underlying state) as
arguments.

Example: a function that modifies fields of a struct using non-atomic
writes. Two threads can each call the function on their own struct
instance safely, but concurrent calls on the *same* instance require
external synchronization.