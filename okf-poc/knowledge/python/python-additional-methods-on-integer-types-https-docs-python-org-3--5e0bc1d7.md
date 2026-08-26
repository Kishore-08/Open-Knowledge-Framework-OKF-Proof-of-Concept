---
id: python-additional-methods-on-integer-types-https-docs-python-org-3--5e0bc1d7
type: concept
title: Additional Methods on Integer Types[¶](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types
  "Link to this heading")
description: The int type implements the [`numbers.Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral
  "numbers.Integral") [abstract base
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Additional Methods on Integer Types[¶](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-integer-types "Link to this heading")

The int type implements the [`numbers.Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral") [abstract base
class](https://docs.python.org/3/glossary.html#term-abstract-base-class). In addition, it provides a few more methods:

int.bit\_length()[¶](https://docs.python.org/3/library/stdtypes.html#int.bit_length "Link to this definition")
:   Return the number of bits necessary to represent an integer in binary,
    excluding the sign and leading zeros:

    ```
    >>> n = -37
    >>> bin(n)
    '-0b100101'
    >>> n.bit_length()
    6
    ```

    More precisely, if `x` is nonzero, then `x.bit_length()` is the
    unique positive integer `k` such that `2**(k-1) <= abs(x) < 2**k`.
    Equivalently, when `abs(x)` is small enough to have a correctly
    rounded logarithm, then `k = 1 + int(log(abs(x), 2))`.
    If `x` is zero, then `x.bit_length()` returns `0`.

    Equivalent to:

    ```
    def bit_length(self):
        s = bin(self)       # binary representation:  bin(-37) --> '-0b100101'
        s = s.lstrip('-0b') # remove leading zeros and minus sign
        return len(s)       # len('100101') --> 6
    ```

    Added in version 3.1.

int.bit\_count()[¶](https://docs.python.org/3/library/stdtypes.html#int.bit_count "Link to this definition")
:   Return the number of ones in the binary representation of the absolute
    value of the integer. This is also known as the population count.
    Example:

    ```
    >>> n = 19
    >>> bin(n)
    '0b10011'
    >>> n.bit_count()
    3
    >>> (-n).bit_count()
    3
    ```

    Equivalent to:

    ```
    def bit_count(self):
        return bin(self).count("1")
    ```

    Added in version 3.10.

int.to\_bytes(*length=1*, *byteorder='big'*, *\**, *signed=False*)[¶](https://docs.python.org/3/library/stdtypes.html#int.to_bytes "Link to this definition")
:   Return an array of bytes representing an integer.

    ```
    >>> (1024).to_bytes(2, byteorder='big')
    b'\x04\x00'
    >>> (1024).to_bytes(10, byteorder='big')
    b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
    >>> (-1024).to_bytes(10, byteorder='big', signed=True)
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
    >>> x = 1000
    >>> x.to_bytes((x.bit_length() + 7) // 8, byteorder='little')
    b'\xe8\x03'
    ```

    The integer is represented using *length* bytes, and defaults to 1. An
    [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") is raised if the integer is not representable with
    the given number of bytes.

    The *byteorder* argument determines the byte order used to represent the
    integer, and defaults to `"big"`. If *byteorder* is
    `"big"`, the most significant byte is at the beginning of the byte
    array. If *byteorder* is `"little"`, the most significant byte is at
    the end of the byte array.

    The *signed* argument determines whether two’s complement is used to
    represent the integer. If *signed* is `False` and a negative integer is
    given, an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") is raised. The default value for *signed*
    is `False`.

    The default values can be used to conveniently turn an integer into a
    single byte object:

    ```
    >>> (65).to_bytes()
    b'A'
    ```

    However, when using the default arguments, don’t try
    to convert a value greater than 255 or you’ll get an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError").

    Equivalent to:

    ```
    def to_bytes(n, length=1, byteorder='big', signed=False):
        if byteorder == 'little':
            order = range(length)
        elif byteorder == 'big':
            order = reversed(range(length))
        else:
            raise ValueError("byteorder must