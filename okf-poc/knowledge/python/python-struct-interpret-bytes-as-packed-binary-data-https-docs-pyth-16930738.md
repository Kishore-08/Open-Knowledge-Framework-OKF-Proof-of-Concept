---
id: python-struct-interpret-bytes-as-packed-binary-data-https-docs-pyth-16930738
type: concept
title: '`struct` — Interpret bytes as packed binary data[¶](https://docs.python.org/3/li'
description: '**Source code:** [Lib/struct.py](https://github.com/python/cpython/tree/3.14/Lib/struct.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/struct.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `struct` — Interpret bytes as packed binary data[¶](https://docs.python.org/3/library/struct.html#struct-interpret-bytes-as-packed-binary-data "Link to this heading")

**Source code:** [Lib/struct.py](https://github.com/python/cpython/tree/3.14/Lib/struct.py)

---

This module converts between Python values and C structs represented
as Python [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects. Compact [format strings](https://docs.python.org/3/library/struct.html#struct-format-strings)
describe the intended conversions to/from Python values.
The module’s functions and objects can be used for two largely
distinct applications, data exchange with external sources (files or
network connections), or data transfer between the Python application
and the C layer.

Note

When no prefix character is given, native mode is the default. It
packs or unpacks data based on the platform and compiler on which
the Python interpreter was built.
The result of packing a given C struct includes pad bytes which
maintain proper alignment for the C types involved; similarly,
alignment is taken into account when unpacking. In contrast, when
communicating data between external sources, the programmer is
responsible for defining byte ordering and padding between elements.
See [Byte Order, Size, and Alignment](https://docs.python.org/3/library/struct.html#struct-alignment) for details.

Several `struct` functions (and methods of [`Struct`](https://docs.python.org/3/library/struct.html#struct.Struct "struct.Struct")) take a *buffer*
argument. This refers to objects that implement the [Buffer Protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects) and
provide either a readable or read-writable buffer. The most common types used
for that purpose are [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray"), but many other types
that can be viewed as an array of bytes implement the buffer protocol, so that
they can be read/filled without additional copying from a `bytes` object.