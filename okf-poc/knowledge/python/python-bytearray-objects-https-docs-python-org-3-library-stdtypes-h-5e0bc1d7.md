---
id: python-bytearray-objects-https-docs-python-org-3-library-stdtypes-h-5e0bc1d7
type: concept
title: Bytearray Objects[¶](https://docs.python.org/3/library/stdtypes.html#bytearray-objects
  "Link to this heading")
description: '[`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray
  "bytearray") objects are a mutable counterpart to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes
  "bytes")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Bytearray Objects[¶](https://docs.python.org/3/library/stdtypes.html#bytearray-objects "Link to this heading")

[`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") objects are a mutable counterpart to [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")
objects.

*class* bytearray(*source=b''*)[¶](https://docs.python.org/3/library/stdtypes.html#bytearray "Link to this definition")

*class* bytearray(*source*, *encoding*, *errors='strict'*)
:   There is no dedicated literal syntax for bytearray objects, instead
    they are always created by calling the constructor:

    - Creating an empty instance: `bytearray()`
    - Creating a zero-filled instance with a given length: `bytearray(10)`
    - From an iterable of integers: `bytearray(range(20))`
    - Copying existing binary data via the buffer protocol: `bytearray(b'Hi!')`

    As bytearray objects are mutable, they support the
    [mutable](https://docs.python.org/3/library/stdtypes.html#typesseq-mutable) sequence operations in addition to the
    common bytes and bytearray operations described in [Bytes and Bytearray Operations](https://docs.python.org/3/library/stdtypes.html#bytes-methods).

    Also see the [bytearray](https://docs.python.org/3/library/functions.html#func-bytearray) built-in.

    Since 2 hexadecimal digits correspond precisely to a single byte, hexadecimal
    numbers are a commonly used format for describing binary data. Accordingly,
    the bytearray type has an additional class method to read data in that format:

    *classmethod* fromhex(*string*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#bytearray.fromhex "Link to this definition")
    :   This `bytearray` class method returns a bytearray object, decoding
        the given string object. The string must contain two hexadecimal digits
        per byte, with ASCII whitespace being ignored.

        ```
        >>> bytearray.fromhex('2Ef0 F1f2  ')
        bytearray(b'.\xf0\xf1\xf2')
        ```

        Changed in version 3.7: `bytearray.fromhex()` now skips all ASCII whitespace in the string,
        not just spaces.

        Changed in version 3.14: `bytearray.fromhex()` now accepts ASCII [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and
        [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) as input.

    A reverse conversion function exists to transform a bytearray object into its
    hexadecimal representation.

    hex(*\**, *bytes\_per\_sep=1*)[¶](https://docs.python.org/3/library/stdtypes.html#bytearray.hex "Link to this definition")

    hex(*sep*, *bytes\_per\_sep=1*)
    :   Return a string object containing two hexadecimal digits for each
        byte in the instance.

        ```
        >>> bytearray(b'\xf0\xf1\xf2').hex()
        'f0f1f2'
        ```

        Added in version 3.5.

        Changed in version 3.8: Similar to [`bytes.hex()`](https://docs.python.org/3/library/stdtypes.html#bytes.hex "bytes.hex"), `bytearray.hex()` now supports
        optional *sep* and *bytes\_per\_sep* parameters to insert separators
        between bytes in the hex output.

    resize(*size*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#bytearray.resize "Link to this definition")
    :   Resize the `bytearray` to contain *size* bytes. *size* must be
        greater than or equal to 0.

        If the `bytearray` needs to shrink, bytes beyond *size* are truncated.

        If the `bytearray` needs to grow, all new bytes, those beyond *size*,
        will be set to null bytes.

        This is equivalent to:

        ```
        >>> def resize(ba, size):
        ...     if len(ba) > size:
        ...         del ba[size:]
        ...     else:
        ...         ba += b'\0' * (size - len(ba))
        ```

        Examples:

        ```
        >>> shrink = bytearray(b'abc')
        >>> shrink.resize(1)
        >>> (shrink, len(shrink))
        (bytearray(b'a'),