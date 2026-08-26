---
id: python-compressing-and-decompressing-data-in-memory-https-docs-pyth-266ffa0e
type: concept
title: Compressing and decompressing data in memory[¶](https://docs.python.org/3/library/lzma.html#compressing-and-decompressing-data-in-memory
  "Link to this heading")
description: '*class* lzma.LZMACompressor(*format=FORMAT\_XZ*, *check=-1*, *preset=None*,
  *filters=None*)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/lzma.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Compressing and decompressing data in memory[¶](https://docs.python.org/3/library/lzma.html#compressing-and-decompressing-data-in-memory "Link to this heading")

*class* lzma.LZMACompressor(*format=FORMAT\_XZ*, *check=-1*, *preset=None*, *filters=None*)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor "Link to this definition")
:   Create a compressor object, which can be used to compress data incrementally.

    For a more convenient way of compressing a single chunk of data, see
    [`compress()`](https://docs.python.org/3/library/lzma.html#lzma.compress "lzma.compress").

    The *format* argument specifies what container format should be used.
    Possible values are [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ") (the default),
    [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE") and [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW").

    The *check* argument specifies the type of integrity check to include in the
    compressed data. This check is used when decompressing, to ensure that the
    data has not been corrupted. Possible values are [`CHECK_NONE`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_NONE "lzma.CHECK_NONE"),
    [`CHECK_CRC32`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC32 "lzma.CHECK_CRC32"), [`CHECK_CRC64`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC64 "lzma.CHECK_CRC64") (the default for
    [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ")) and [`CHECK_SHA256`](https://docs.python.org/3/library/lzma.html#lzma.CHECK_SHA256 "lzma.CHECK_SHA256").

    If the specified check is not supported, an [`LZMAError`](https://docs.python.org/3/library/lzma.html#lzma.LZMAError "lzma.LZMAError") is raised.

    The compression settings can be specified either as a preset compression
    level (with the *preset* argument), or in detail as a custom filter chain
    (with the *filters* argument).

    The *preset* argument (if provided) should be an integer between `0` and
    `9` (inclusive), optionally OR-ed with the constant
    [`PRESET_EXTREME`](https://docs.python.org/3/library/lzma.html#lzma.PRESET_EXTREME "lzma.PRESET_EXTREME"). If neither *preset* nor *filters* are given, the
    default behavior is to use [`PRESET_DEFAULT`](https://docs.python.org/3/library/lzma.html#lzma.PRESET_DEFAULT "lzma.PRESET_DEFAULT") (preset level `6`).
    Higher presets produce smaller output, but make the compression process
    slower.

    Note

    In addition to being more CPU-intensive, compression with higher presets
    also requires much more memory (and produces output that needs more memory
    to decompress). With preset `9` for example, the overhead for an
    `LZMACompressor` object can be as high as 800 MiB. For this reason,
    it is generally best to stick with the default preset.

    The *filters* argument (if provided) should be a filter chain specifier.
    See [Specifying custom filter chains](https://docs.python.org/3/library/lzma.html#filter-chain-specs) for details.

    compress(*data*)[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor.compress "Link to this definition")
    :   Compress *data* (a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object), returning a `bytes`
        object containing compressed data for at least part of the input. Some of
        *data* may be buffered internally, for use in later calls to
        `compress()` and [`flush()`](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor.flush "lzma.LZMACompressor.flush"). The returned data should be
        concatenated with the output of any previous calls to `compress()`.

    flush()[¶](https://docs.python.org/3/library/lzma.html#lzma.LZMACompressor.flush "Link to this definition")
    :   Finish the compression process, returning a [`bytes`