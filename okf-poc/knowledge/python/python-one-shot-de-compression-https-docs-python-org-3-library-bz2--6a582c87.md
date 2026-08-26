---
id: python-one-shot-de-compression-https-docs-python-org-3-library-bz2--6a582c87
type: concept
title: One-shot (de)compression[¶](https://docs.python.org/3/library/bz2.html#one-shot-de-compression
  "Link to this heading")
description: bz2.compress(*data*, *compresslevel=9*)[¶](https://docs.python.org/3/library/bz2.html#bz2.compress
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/bz2.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## One-shot (de)compression[¶](https://docs.python.org/3/library/bz2.html#one-shot-de-compression "Link to this heading")

bz2.compress(*data*, *compresslevel=9*)[¶](https://docs.python.org/3/library/bz2.html#bz2.compress "Link to this definition")
:   Compress *data*, a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).

    *compresslevel*, if given, must be an integer between `1` and `9`. The
    default is `9`.

    For incremental compression, use a [`BZ2Compressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor "bz2.BZ2Compressor") instead.

bz2.decompress(*data*)[¶](https://docs.python.org/3/library/bz2.html#bz2.decompress "Link to this definition")
:   Decompress *data*, a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).

    If *data* is the concatenation of multiple compressed streams, decompress
    all of the streams.

    For incremental decompression, use a [`BZ2Decompressor`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor "bz2.BZ2Decompressor") instead.

    Changed in version 3.3: Support for multi-stream inputs was added.