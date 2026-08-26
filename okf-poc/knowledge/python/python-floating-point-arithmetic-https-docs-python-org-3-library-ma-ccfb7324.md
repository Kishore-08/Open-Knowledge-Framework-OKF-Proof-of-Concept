---
id: python-floating-point-arithmetic-https-docs-python-org-3-library-ma-ccfb7324
type: concept
title: Floating point arithmetic[¶](https://docs.python.org/3/library/math.html#floating-point-arithmetic
  "Link to this heading")
description: math.ceil(*x*)[¶](https://docs.python.org/3/library/math.html#math.ceil
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/math.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Floating point arithmetic[¶](https://docs.python.org/3/library/math.html#floating-point-arithmetic "Link to this heading")

math.ceil(*x*)[¶](https://docs.python.org/3/library/math.html#math.ceil "Link to this definition")
:   Return the ceiling of *x*, the smallest integer greater than or equal to *x*.
    If *x* is not a float, delegates to [`x.__ceil__`](https://docs.python.org/3/reference/datamodel.html#object.__ceil__ "object.__ceil__"),
    which should return an [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral") value.

math.fabs(*x*)[¶](https://docs.python.org/3/library/math.html#math.fabs "Link to this definition")
:   Return the absolute value of *x*.

math.floor(*x*)[¶](https://docs.python.org/3/library/math.html#math.floor "Link to this definition")
:   Return the floor of *x*, the largest integer less than or equal to *x*. If
    *x* is not a float, delegates to [`x.__floor__`](https://docs.python.org/3/reference/datamodel.html#object.__floor__ "object.__floor__"), which
    should return an [`Integral`](https://docs.python.org/3/library/numbers.html#numbers.Integral "numbers.Integral") value.

math.fma(*x*, *y*, *z*)[¶](https://docs.python.org/3/library/math.html#math.fma "Link to this definition")
:   Fused multiply-add operation. Return `(x * y) + z`, computed as though with
    infinite precision and range followed by a single round to the `float`
    format. This operation often provides better accuracy than the direct
    expression `(x * y) + z`.

    This function follows the specification of the fusedMultiplyAdd operation
    described in the IEEE 754 standard. The standard leaves one case
    implementation-defined, namely the result of `fma(0, inf, nan)`
    and `fma(inf, 0, nan)`. In these cases, `math.fma` returns a NaN,
    and does not raise any exception.

    Added in version 3.13.

math.fmod(*x*, *y*)[¶](https://docs.python.org/3/library/math.html#math.fmod "Link to this definition")
:   Return the floating-point remainder of `x / y`,
    as defined by the platform C library function `fmod(x, y)`. Note that the
    Python expression `x % y` may not return the same result. The intent of the C
    standard is that `fmod(x, y)` be exactly (mathematically; to infinite
    precision) equal to `x - n*y` for some integer *n* such that the result has
    the same sign as *x* and magnitude less than `abs(y)`. Python’s `x % y`
    returns a result with the sign of *y* instead, and may not be exactly computable
    for float arguments. For example, `fmod(-1e-100, 1e100)` is `-1e-100`, but
    the result of Python’s `-1e-100 % 1e100` is `1e100-1e-100`, which cannot be
    represented exactly as a float, and rounds to the surprising `1e100`. For
    this reason, function `fmod()` is generally preferred when working with
    floats, while Python’s `x % y` is preferred when working with integers.

math.modf(*x*)[¶](https://docs.python.org/3/library/math.html#math.modf "Link to this definition")
:   Return the fractional and integer parts of *x*. Both results carry the sign
    of *x* and are floats.

    Note that `modf()` has a different call/return pattern
    than its C equivalents: it takes a single argument and return a pair of
    values, rather than returning its second return value through an ‘output
    parameter’ (there is no such thing in Python).

math.remainder(*x*, *y*)[¶](https://docs.python.org/3/library/math.html#math.remainder "Link to this definition")
:   Return the IEEE 754-style remainder of *x* with respect to *y*. For
    finite *x* and finite nonzero *y*, this is the difference `x - n*y`,
    where `n` is the closest integer to the exact value of the quotient `x /
    y`. If `x / y` is exactly halfway between two consecutive integers, the
    nearest *even* integer is used for `n`. The remainder `r = remainder(x,
    y)` thus always satisfies `abs(r) <= 0.5 * abs(y)`.

    Special cases follow IEEE 754: in particular, `remainder(x, math.i