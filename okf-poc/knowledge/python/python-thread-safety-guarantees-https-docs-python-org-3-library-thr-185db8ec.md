---
id: python-thread-safety-guarantees-https-docs-python-org-3-library-thr-185db8ec
type: concept
title: Thread Safety Guarantees[¶](https://docs.python.org/3/library/threadsafety.html#
description: This page documents thread-safety guarantees for built-in types in Python’s
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/threadsafety.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# Thread Safety Guarantees[¶](https://docs.python.org/3/library/threadsafety.html#thread-safety-guarantees "Link to this heading")

This page documents thread-safety guarantees for built-in types in Python’s
free-threaded build. The guarantees described here apply when using Python with
the [GIL](https://docs.python.org/3/glossary.html#term-GIL) disabled (free-threaded mode). When the GIL is enabled, most
operations are implicitly serialized.

For general guidance on writing thread-safe code in free-threaded Python, see
[Python support for free threading](https://docs.python.org/3/howto/free-threading-python.html#freethreading-python-howto).