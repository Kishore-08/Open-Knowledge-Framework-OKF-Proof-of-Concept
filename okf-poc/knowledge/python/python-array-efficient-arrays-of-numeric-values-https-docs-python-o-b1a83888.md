---
id: python-array-efficient-arrays-of-numeric-values-https-docs-python-o-b1a83888
type: concept
title: '`array` — Efficient arrays of numeric values[¶](https://docs.python.org/3/librar'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/array.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `array` — Efficient arrays of numeric values[¶](https://docs.python.org/3/library/array.html#module-array "Link to this heading")

---

This module defines an object type which can compactly represent an array of
basic values: characters, integers, floating-point numbers. Arrays are mutable [sequence](https://docs.python.org/3/glossary.html#term-sequence)
types and behave very much like lists, except that the type of objects stored in
them is constrained. The type is specified at object creation time by using a
*type code*, which is a single character. The following type codes are
defined:

| Type code | C Type | Python Type | Minimum size in bytes | Notes |
| --- | --- | --- | --- | --- |
| `'b'` | signed char | int | 1 |  |
| `'B'` | unsigned char | int | 1 |  |
| `'u'` | wchar\_t | Unicode character | 2 | (1) |
| `'w'` | Py\_UCS4 | Unicode character | 4 | (2) |
| `'h'` | signed short | int | 2 |  |
| `'H'` | unsigned short | int | 2 |  |
| `'i'` | signed int | int | 2 |  |
| `'I'` | unsigned int | int | 2 |  |
| `'l'` | signed long | int | 4 |  |
| `'L'` | unsigned long | int | 4 |  |
| `'q'` | signed long long | int | 8 |  |
| `'Q'` | unsigned long long | int | 8 |  |
| `'f'` | float | float | 4 |  |
| `'d'` | double | float | 8 |  |

Notes:

1. It can be 16 bits or 32 bits depending on the platform.

   Changed in version 3.9: `array('u')` now uses `wchar_t` as C type instead of deprecated
   `Py_UNICODE`. This change doesn’t affect its behavior because
   `Py_UNICODE` is alias of `wchar_t` since Python 3.3.

   Deprecated since version 3.3, will be removed in version 3.16: Please migrate to `'w'` typecode.
2. Added in version 3.13.

See also

The [ctypes](https://docs.python.org/3/library/ctypes.html#ctypes-fundamental-data-types) and
[struct](https://docs.python.org/3/library/struct.html#format-characters) modules,
as well as third-party modules like [numpy](https://numpy.org/doc/stable/reference/arrays.interface.html#object.__array_interface__),
use similar – but slightly different – type codes.

The actual representation of values is determined by the machine architecture
(strictly speaking, by the C implementation). The actual size can be accessed
through the [`array.itemsize`](https://docs.python.org/3/library/array.html#array.array.itemsize "array.array.itemsize") attribute.

The module defines the following item:

array.typecodes[¶](https://docs.python.org/3/library/array.html#array.typecodes "Link to this definition")
:   A string with all available type codes.

The module defines the following type:

*class* array.array(*typecode*[, *initializer*])[¶](https://docs.python.org/3/library/array.html#array.array "Link to this definition")
:   A new array whose items are restricted by *typecode*, and initialized
    from the optional *initializer* value, which must be a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
    or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") object, a Unicode string, or iterable over elements
    of the appropriate type.

    If given a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") or [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") object, the initializer
    is passed to the new array’s [`frombytes()`](https://docs.python.org/3/library/array.html#array.array.frombytes "array.array.frombytes") method;
    if given a Unicode string, the initializer is passed to the
    [`fromunicode()`](https://docs.python.org/3/library/array.html#array.array.fromunicode "array.array.fromunicode") method;
    otherwise, the initializer’s iterator is passed to the [`extend()`](https://docs.python.org/3/library/array.html#array.array.extend "array.array.extend") method
    to add initial items to the array.

    Array objects support the ordinary [mutable](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) [sequence](https://docs.python.org/3/glossary.html#term-sequen