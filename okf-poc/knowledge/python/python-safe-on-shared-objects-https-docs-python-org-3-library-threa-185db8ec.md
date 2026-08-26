---
id: python-safe-on-shared-objects-https-docs-python-org-3-library-threa-185db8ec
type: concept
title: Safe on shared objects[¶](https://docs.python.org/3/library/threadsafety.html#safe-on-shared-objects
  "Link to this heading")
description: A function or operation that is safe for concurrent use on the **same**
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Safe on shared objects[¶](https://docs.python.org/3/library/threadsafety.html#safe-on-shared-objects "Link to this heading")

A function or operation that is safe for concurrent use on the **same**
object. The implementation uses internal synchronization (such as
[per-object locks](https://docs.python.org/3/glossary.html#term-per-object-lock) or
[critical sections](https://docs.python.org/3/c-api/synchronization.html#python-critical-section-api)) to protect shared
mutable state, so callers do not need to supply their own locking.

Example: [`PyList_GetItemRef()`](https://docs.python.org/3/c-api/list.html#c.PyList_GetItemRef "PyList_GetItemRef") can be called from multiple threads on the
same [`PyListObject`](https://docs.python.org/3/c-api/list.html#c.PyListObject "PyListObject") - it uses internal synchronization to serialize
access.