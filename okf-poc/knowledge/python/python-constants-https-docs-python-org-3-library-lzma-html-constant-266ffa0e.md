---
id: python-constants-https-docs-python-org-3-library-lzma-html-constant-266ffa0e
type: concept
title: Constants[¶](https://docs.python.org/3/library/lzma.html#constants "Link to
  this heading")
description: The following module-level constants are provided for use as the *format*,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/lzma.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Constants[¶](https://docs.python.org/3/library/lzma.html#constants "Link to this heading")

The following module-level constants are provided for use as the *format*,
*check*, *preset* and *filters* arguments of the classes and functions above.

Container formats:

lzma.FORMAT\_XZ[¶](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "Link to this definition")
:   The `.xz` container format.

lzma.FORMAT\_ALONE[¶](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "Link to this definition")
:   The legacy `.lzma` container format. This format is more limited than
    `.xz` – it does not support integrity checks or multiple filters.

lzma.FORMAT\_RAW[¶](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "Link to this definition")
:   A raw data stream, not using any container format. This format specifier
    does not support integrity checks, and requires that you always specify a
    custom filter chain (for both compression and decompression). Additionally,
    data compressed in this manner cannot be decompressed using
    [`FORMAT_AUTO`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_AUTO "lzma.FORMAT_AUTO").

lzma.FORMAT\_AUTO[¶](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_AUTO "Link to this definition")
:   Used for decompression only. The container format is detected
    automatically, so that both `.xz` and `.lzma` files can be decompressed.

Integrity checks:

lzma.CHECK\_NONE[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_NONE "Link to this definition")
:   No integrity check. This is the default (and the only acceptable value) for
    [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE") and [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW").

lzma.CHECK\_CRC32[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC32 "Link to this definition")
:   A 32-bit Cyclic Redundancy Check.

lzma.CHECK\_CRC64[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_CRC64 "Link to this definition")
:   A 64-bit Cyclic Redundancy Check. This is the default for
    [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ").

lzma.CHECK\_SHA256[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_SHA256 "Link to this definition")
:   A 256-bit Secure Hash Algorithm.

lzma.CHECK\_UNKNOWN[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_UNKNOWN "Link to this definition")
:   The integrity check used by a stream could not yet be determined. This may
    be the value of the [`LZMADecompressor.check`](https://docs.python.org/3/library/lzma.html#lzma.LZMADecompressor.check "lzma.LZMADecompressor.check") attribute until enough of
    the input has been decoded.

lzma.CHECK\_ID\_MAX[¶](https://docs.python.org/3/library/lzma.html#lzma.CHECK_ID_MAX "Link to this definition")
:   The largest supported integrity-check ID.

Compression presets:

lzma.PRESET\_DEFAULT[¶](https://docs.python.org/3/library/lzma.html#lzma.PRESET_DEFAULT "Link to this definition")
:   The default compression preset, equivalent to preset level `6`.

lzma.PRESET\_EXTREME[¶](https://docs.python.org/3/library/lzma.html#lzma.PRESET_EXTREME "Link to this definition")
:   A flag that may be bitwise OR-ed with a preset level (`0` to `9`) to
    select a slower but more thorough variant of that preset.

Filter IDs and options:

lzma.FILTER\_LZMA1[¶](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA1 "Link to this definition")

lzma.FILTER\_LZMA2[¶](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA2 "Link to this definition")
:   The LZMA1 and LZMA2 compression filters. [`FILTER_LZMA1`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA1 "lzma.FILTER_LZMA1") is for use
    with [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE"), while [`FILTER_LZMA2`](https://docs.python.org/3/library/lzma.htm