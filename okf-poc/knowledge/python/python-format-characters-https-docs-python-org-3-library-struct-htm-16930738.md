---
id: python-format-characters-https-docs-python-org-3-library-struct-htm-16930738
type: concept
title: Format Characters[¶](https://docs.python.org/3/library/struct.html#format-characters
  "Link to this heading")
description: Format characters have the following meaning; the conversion between
  C and
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/struct.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Format Characters[¶](https://docs.python.org/3/library/struct.html#format-characters "Link to this heading")

Format characters have the following meaning; the conversion between C and
Python values should be obvious given their types. The ‘Standard size’ column
refers to the size of the packed value in bytes when using standard size; that
is, when the format string starts with one of `'<'`, `'>'`, `'!'` or
`'='`. When using native size, the size of the packed value is
platform-dependent.

| Format | C Type | Python type | Standard size | Notes |
| --- | --- | --- | --- | --- |
| `x` | pad byte | no value |  | (7) |
| `c` | char | bytes of length 1 | 1 |  |
| `b` | signed char | int | 1 | (2) |
| `B` | unsigned char | int | 1 | (2) |
| `?` | \_Bool | bool | 1 | (1) |
| `h` | short | int | 2 | (2) |
| `H` | unsigned short | int | 2 | (2) |
| `i` | int | int | 4 | (2) |
| `I` | unsigned int | int | 4 | (2) |
| `l` | long | int | 4 | (2) |
| `L` | unsigned long | int | 4 | (2) |
| `q` | long long | int | 8 | (2) |
| `Q` | unsigned long long | int | 8 | (2) |
| `n` | `ssize_t` | int |  | (2), (3) |
| `N` | `size_t` | int |  | (2), (3) |
| `e` | \_Float16 | float | 2 | (4), (6) |
| `f` | float | float | 4 | (4) |
| `d` | double | float | 8 | (4) |
| `F` | float complex | complex | 8 | (10) |
| `D` | double complex | complex | 16 | (10) |
| `s` | char[] | bytes |  | (9) |
| `p` | char[] | bytes |  | (8) |
| `P` | void\* | int |  | (2), (5) |

Changed in version 3.3: Added support for the `'n'` and `'N'` formats.

Changed in version 3.6: Added support for the `'e'` format.

Changed in version 3.14: Added support for the `'F'` and `'D'` formats.

See also

The [`array`](https://docs.python.org/3/library/array.html#module-array "array: Space efficient arrays of uniformly typed numeric values.") and [ctypes](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types) modules,
as well as third-party modules like [numpy](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__),
use similar – but slightly different – type codes.

Notes:

1. The `'?'` conversion code corresponds to the \_Bool type
   defined by C standards since C99. In standard mode, it is
   represented by one byte.
2. When attempting to pack a non-integer using any of the integer conversion
   codes, if the non-integer has a [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") method then that method is
   called to convert the argument to an integer before packing.

   Changed in version 3.2: Added use of the [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__") method for non-integers.
3. The `'n'` and `'N'` conversion codes are only available for the native
   size (selected as the default or with the `'@'` byte order character).
   For the standard size, you can use whichever of the other integer formats
   fits your application.
4. For the `'f'`, `'d'` and `'e'` conversion codes, the packed
   representation uses the IEEE 754 binary32, binary64 or binary16 format (for
   `'f'`, `'d'` or `'e'` respectively), regardless of the floating-point
   format used by the platform.
5. The `'P'` format character is only available for the native byte ordering
   (selected as the default or with the `'@'` byte order character). The byte
   order character `'='` chooses to use little- or big-endian ordering based
   on the host system. The struct module does not interpret this as native
   ordering, so the `'P'` format is not available.
6. The IEEE 754 binary16 “half precision” type was introduced in the 2008
   revision of the [IEEE 754 standard](https://en.wikipedia.org/wiki/IEEE_754-2008_revision). It has a sign
   bit, a 5-bit exponent and 11-bit precision (with 10 bits explicitly stored),
   and can represent numbers between approximately `6.1e-05` and `6.5e+04`
   at full precision. This type is not widely supported by C co