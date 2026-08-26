---
id: python-listing-loaded-shared-libraries-https-docs-python-org-3-libr-07786b1c
type: concept
title: Listing loaded shared libraries[¶](https://docs.python.org/3/library/ctypes.html#listing-loaded-shared-libraries
  "Link to this heading")
description: When writing code that relies on code loaded from shared libraries, it
  can be
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Listing loaded shared libraries[¶](https://docs.python.org/3/library/ctypes.html#listing-loaded-shared-libraries "Link to this heading")

When writing code that relies on code loaded from shared libraries, it can be
useful to know which shared libraries have already been loaded into the current
process.

The `ctypes.util` module provides the [`dllist()`](https://docs.python.org/3/library/ctypes.html#ctypes.util.dllist "ctypes.util.dllist") function,
which calls the different APIs provided by the various platforms to help determine
which shared libraries have already been loaded into the current process.

The exact output of this function will be system dependent. On most platforms,
the first entry of this list represents the current process itself, which may
be an empty string.
For example, on glibc-based Linux, the return may look like:

```
>>> from ctypes.util import dllist
>>> dllist()
['', 'linux-vdso.so.1', '/lib/x86_64-linux-gnu/libm.so.6', '/lib/x86_64-linux-gnu/libc.so.6', ... ]
```