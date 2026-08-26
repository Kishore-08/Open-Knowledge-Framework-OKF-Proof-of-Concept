---
id: python-bz2-support-for-bzip2-compression-https-docs-python-org-3-li-6a582c87
type: concept
title: '`bz2` — Support for **bzip2** compression[¶](https://docs.python.org/3/library/b'
description: '**Source code:** [Lib/bz2.py](https://github.com/python/cpython/tree/3.14/Lib/bz2.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/bz2.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `bz2` — Support for **bzip2** compression[¶](https://docs.python.org/3/library/bz2.html#module-bz2 "Link to this heading")

**Source code:** [Lib/bz2.py](https://github.com/python/cpython/tree/3.14/Lib/bz2.py)

---

This module provides a comprehensive interface for compressing and
decompressing data using the bzip2 compression algorithm.

The `bz2` module contains:

- The [`open()`](https://docs.python.org/3/library/bz2.html#bz2.open "bz2.open") function and [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File") class for reading and
  writing compressed files.
- The [`BZ2Compressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor "bz2.BZ2Compressor") and [`BZ2Decompressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor "bz2.BZ2Decompressor") classes for
  incremental (de)compression.
- The [`compress()`](https://docs.python.org/3/library/bz2.html#bz2.compress "bz2.compress") and [`decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress") functions for one-shot
  (de)compression.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).