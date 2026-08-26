---
id: python-incremental-de-compression-https-docs-python-org-3-library-b-6a582c87
type: concept
title: Incremental (de)compression[¶](https://docs.python.org/3/library/bz2.html#incremental-de-compression
  "Link to this heading")
description: '*class* bz2.BZ2Compressor(*compresslevel=9*)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/bz2.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Incremental (de)compression[¶](https://docs.python.org/3/library/bz2.html#incremental-de-compression "Link to this heading")

*class* bz2.BZ2Compressor(*compresslevel=9*)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor "Link to this definition")
:   Create a new compressor object. This object may be used to compress data
    incrementally. For one-shot compression, use the [`compress()`](https://docs.python.org/3/library/bz2.html#bz2.compress "bz2.compress") function
    instead.

    *compresslevel*, if given, must be an integer between `1` and `9`. The
    default is `9`.

    compress(*data*)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor.compress "Link to this definition")
    :   Provide data to the compressor object. Returns a chunk of compressed data
        if possible, or an empty byte string otherwise.

        When you have finished providing data to the compressor, call the
        [`flush()`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor.flush "bz2.BZ2Compressor.flush") method to finish the compression process.

    flush()[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Compressor.flush "Link to this definition")
    :   Finish the compression process. Returns the compressed data left in
        internal buffers.

        The compressor object may not be used after this method has been called.

*class* bz2.BZ2Decompressor[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor "Link to this definition")
:   Create a new decompressor object. This object may be used to decompress data
    incrementally. For one-shot compression, use the [`decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress") function
    instead.

    Note

    This class does not transparently handle inputs containing multiple
    compressed streams, unlike [`decompress()`](https://docs.python.org/3/library/bz2.html#bz2.decompress "bz2.decompress") and [`BZ2File`](https://docs.python.org/3/library/bz2.html#bz2.BZ2File "bz2.BZ2File"). If
    you need to decompress a multi-stream input with `BZ2Decompressor`,
    you must use a new decompressor for each stream.

    decompress(*data*, *max\_length=-1*)[¶](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.decompress "Link to this definition")
    :   Decompress *data* (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)), returning
        uncompressed data as bytes. Some of *data* may be buffered
        internally, for use in later calls to `decompress()`. The
        returned data should be concatenated with the output of any
        previous calls to `decompress()`.

        If *max\_length* is nonnegative, returns at most *max\_length*
        bytes of decompressed data. If this limit is reached and further
        output can be produced, the [`needs_input`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.needs_input "bz2.BZ2Decompressor.needs_input") attribute will
        be set to `False`. In this case, the next call to
        `decompress()` may provide *data* as `b''` to obtain
        more of the output.

        If all of the input data was decompressed and returned (either
        because this was less than *max\_length* bytes, or because
        *max\_length* was negative), the [`needs_input`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.needs_input "bz2.BZ2Decompressor.needs_input") attribute
        will be set to `True`.

        Attempting to decompress data after the end of stream is reached
        raises an [`EOFError`](https://docs.python.org/3/library/exceptions.html#EOFError "EOFError"). Any data found after the end of the
        stream is ignored and saved in the [`unused_data`](https://docs.python.org/3/library/bz2.html#bz2.BZ2Decompressor.unused_data "bz2.BZ2Decompressor.unused_data") attribute.

        Changed in version 3.5: Added the *max\_length* parameter.

    eof[¶](https://docs.python