---
id: python-the-compression-package-https-docs-python-org-3-library-comp-1591d58d
type: concept
title: The `compression` package[¶](https://docs.python.org/3/library/compression.html#
description: Added in version 3.14.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/compression.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# The `compression` package[¶](https://docs.python.org/3/library/compression.html#module-compression "Link to this heading")

Added in version 3.14.

The `compression` package contains the canonical compression modules
containing interfaces to several different compression algorithms. Some of
these modules have historically been available as separate modules; those will
continue to be available under their original names for compatibility reasons,
and will not be removed without a deprecation cycle. The use of modules in
`compression` is encouraged where practical.

- `compression.bz2` – Re-exports [`bz2`](https://docs.python.org/3/library/bz2.html#module-bz2 "bz2: Interfaces for bzip2 compression and decompression.")
- `compression.gzip` – Re-exports [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.")
- `compression.lzma` – Re-exports [`lzma`](https://docs.python.org/3/library/lzma.html#module-lzma "lzma: A Python wrapper for the liblzma compression library.")
- `compression.zlib` – Re-exports [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")
- [`compression.zstd`](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "compression.zstd: Low-level interface to compression and decompression routines in the zstd library.") – Wrapper for the Zstandard compression library