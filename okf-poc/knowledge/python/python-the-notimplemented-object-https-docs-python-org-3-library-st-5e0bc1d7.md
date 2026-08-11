---
id: python-the-notimplemented-object-https-docs-python-org-3-library-st-5e0bc1d7
type: concept
title: The NotImplemented Object[¶](https://docs.python.org/3/library/stdtypes.html#the-notimplemented-object
  "Link to this heading")
description: This object is returned from comparisons and binary operations when they
  are
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### The NotImplemented Object[¶](https://docs.python.org/3/library/stdtypes.html#the-notimplemented-object "Link to this heading")

This object is returned from comparisons and binary operations when they are
asked to operate on types they don’t support. See [Comparisons](https://docs.python.org/3/reference/expressions.html#comparisons) for more
information. There is exactly one [`NotImplemented`](https://docs.python.org/3/library/constants.html#NotImplemented "NotImplemented") object.
`type(NotImplemented)()` produces the singleton instance.

It is written as `NotImplemented`.