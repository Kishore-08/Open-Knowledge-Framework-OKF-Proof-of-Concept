---
id: python-binary-sequence-types-bytes-https-docs-python-org-3-library--5e0bc1d7
type: concept
title: Binary Sequence Types — [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes
  "bytes"), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray
  "bytearray"), [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview
  "memoryview")[¶](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview
  "Link to this heading")
description: The core built-in types for manipulating binary data are [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes
  "bytes") and
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Binary Sequence Types — [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"), [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray"), [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview")[¶](https://docs.python.org/3/library/stdtypes.html#binary-sequence-types-bytes-bytearray-memoryview "Link to this heading")

The core built-in types for manipulating binary data are [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and
[`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray"). They are supported by [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview "memoryview") which uses
the [buffer protocol](https://docs.python.org/3/c-api/buffer.html#bufferobjects) to access the memory of other
binary objects without needing to make a copy.

The [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") module supports efficient storage of basic data types like
32-bit integers and IEEE754 double-precision floating values.