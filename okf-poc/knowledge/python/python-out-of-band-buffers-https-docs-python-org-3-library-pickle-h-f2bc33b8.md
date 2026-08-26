---
id: python-out-of-band-buffers-https-docs-python-org-3-library-pickle-h-f2bc33b8
type: concept
title: Out-of-band Buffers[¶](https://docs.python.org/3/library/pickle.html#out-of-band-buffers
  "Link to this heading")
description: Added in version 3.8.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Out-of-band Buffers[¶](https://docs.python.org/3/library/pickle.html#out-of-band-buffers "Link to this heading")

Added in version 3.8.

In some contexts, the `pickle` module is used to transfer massive amounts
of data. Therefore, it can be important to minimize the number of memory
copies, to preserve performance and resource consumption. However, normal
operation of the `pickle` module, as it transforms a graph-like structure
of objects into a sequential stream of bytes, intrinsically involves copying
data to and from the pickle stream.

This constraint can be eschewed if both the *provider* (the implementation
of the object types to be transferred) and the *consumer* (the implementation
of the communications system) support the out-of-band transfer facilities
provided by pickle protocol 5 and higher.