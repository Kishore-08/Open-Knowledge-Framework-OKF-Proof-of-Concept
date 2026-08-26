---
id: python-compression-zstd-compression-compatible-with-the-zstandard-f-66f34da3
type: concept
title: '`compression.zstd` — Compression compatible with the Zstandard format[¶](https:/'
description: Added in version 3.14.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/compression.zstd.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `compression.zstd` — Compression compatible with the Zstandard format[¶](https://docs.python.org/3/library/compression.zstd.html#module-compression.zstd "Link to this heading")

Added in version 3.14.

**Source code:** [Lib/compression/zstd/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/compression/zstd/__init__.py)

---

This module provides classes and functions for compressing and decompressing
data using the Zstandard (or *zstd*) compression algorithm. The
[zstd manual](https://facebook.github.io/zstd/doc/api_manual_latest.html)
describes Zstandard as “a fast lossless compression algorithm, targeting
real-time compression scenarios at zlib-level and better compression ratios.”
Also included is a file interface that supports reading and writing the
contents of `.zst` files created by the **zstd** utility, as well as
raw zstd compressed streams.

The `compression.zstd` module contains:

- The [`open()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.open "compression.zstd.open") function and [`ZstdFile`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdFile "compression.zstd.ZstdFile") class for reading and
  writing compressed files.
- The [`ZstdCompressor`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor "compression.zstd.ZstdCompressor") and [`ZstdDecompressor`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDecompressor "compression.zstd.ZstdDecompressor") classes for
  incremental (de)compression.
- The [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress "compression.zstd.compress") and [`decompress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.decompress "compression.zstd.decompress") functions for one-shot
  (de)compression.
- The [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict") and [`finalize_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.finalize_dict "compression.zstd.finalize_dict") functions and the
  [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict") class to train and manage Zstandard dictionaries.
- The [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter"), [`DecompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "compression.zstd.DecompressionParameter"), and
  [`Strategy`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.Strategy "compression.zstd.Strategy") classes for setting advanced (de)compression parameters.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).