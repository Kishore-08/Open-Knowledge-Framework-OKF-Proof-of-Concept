---
id: python-zlib-compression-compatible-with-gzip-https-docs-python-org--1730b898
type: concept
title: '`zlib` — Compression compatible with **gzip**[¶](https://docs.python.org/3/libra'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `zlib` — Compression compatible with **gzip**[¶](https://docs.python.org/3/library/zlib.html#module-zlib "Link to this heading")

---

For applications that require data compression, the functions in this module
allow compression and decompression, using the [zlib library](https://www.zlib.net).

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).

zlib’s functions have many options and often need to be used in a particular
order. This documentation doesn’t attempt to cover all of the permutations;
consult the [zlib manual](https://www.zlib.net/manual.html) for authoritative
information.

For reading and writing `.gz` files see the [`gzip`](https://docs.python.org/3/library/gzip.html#module-gzip "gzip: Interfaces for gzip compression and decompression using file objects.") module.

The available exception and functions in this module are:

*exception* zlib.error[¶](https://docs.python.org/3/library/zlib.html#zlib.error "Link to this definition")
:   Exception raised on compression and decompression errors.

zlib.adler32(*data*[, *value*])[¶](https://docs.python.org/3/library/zlib.html#zlib.adler32 "Link to this definition")
:   Computes an Adler-32 checksum of *data*. (An Adler-32 checksum is almost as
    reliable as a CRC32 but can be computed much more quickly.) The result
    is an unsigned 32-bit integer. If *value* is present, it is used as
    the starting value of the checksum; otherwise, a default value of 1
    is used. Passing in *value* allows computing a running checksum over the
    concatenation of several inputs. The algorithm is not cryptographically
    strong, and should not be used for authentication or digital signatures. Since
    the algorithm is designed for use as a checksum algorithm, it is not suitable
    for use as a general hash algorithm.

    Changed in version 3.0: The result is always unsigned.

zlib.compress(*data*, */*, *level=Z\_DEFAULT\_COMPRESSION*, *wbits=MAX\_WBITS*)[¶](https://docs.python.org/3/library/zlib.html#zlib.compress "Link to this definition")
:   Compresses the bytes in *data*, returning a bytes object containing compressed data.
    *level* is an integer from `0` to `9` or `-1` controlling the level of compression;
    See [`Z_BEST_SPEED`](https://docs.python.org/3/library/zlib.html#zlib.Z_BEST_SPEED "zlib.Z_BEST_SPEED") (`1`), [`Z_BEST_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_BEST_COMPRESSION "zlib.Z_BEST_COMPRESSION") (`9`),
    [`Z_NO_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_NO_COMPRESSION "zlib.Z_NO_COMPRESSION") (`0`), and the default,
    [`Z_DEFAULT_COMPRESSION`](https://docs.python.org/3/library/zlib.html#zlib.Z_DEFAULT_COMPRESSION "zlib.Z_DEFAULT_COMPRESSION") (`-1`) for more information about these values.

    The *wbits* argument controls the size of the history buffer (or the
    “window size”) used when compressing data, and whether a header and
    trailer is included in the output. It can take several ranges of values,
    defaulting to `15` ([`MAX_WBITS`](https://docs.python.org/3/library/zlib.html#zlib.MAX_WBITS "zlib.MAX_WBITS")):

    - +9 to +15: The base-two logarithm of the window size, which
      therefore ranges between 512 and 32768. Larger values produce
      better compression at the expense of greater memory usage. The
      resulting output will include a zlib-specific header and trailer.
    - −9 to −15: Uses the absolute value of *wbits* as the
      window size logarithm, while producing a raw output stream with no
      header or trailing checksum.
    - +25 to +31 = 16 + (9 to 15): Uses the low 4 bits of the value as the
      window size logarithm, while including a basic **gz