---
id: python-power-exponential-and-logarithmic-functions-https-docs-pytho-ccfb7324
type: concept
title: Power, exponential and logarithmic functions[¶](https://docs.python.org/3/library/math.html#power-exponential-and-logarithmic-functions
  "Link to this heading")
description: math.cbrt(*x*)[¶](https://docs.python.org/3/library/math.html#math.cbrt
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/math.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Power, exponential and logarithmic functions[¶](https://docs.python.org/3/library/math.html#power-exponential-and-logarithmic-functions "Link to this heading")

math.cbrt(*x*)[¶](https://docs.python.org/3/library/math.html#math.cbrt "Link to this definition")
:   Return the cube root of *x*.

    Added in version 3.11.

math.exp(*x*)[¶](https://docs.python.org/3/library/math.html#math.exp "Link to this definition")
:   Return *e* raised to the power *x*, where *e* = 2.718281… is the base
    of natural logarithms. This is usually more accurate than `math.e ** x`
    or `pow(math.e, x)`.

math.exp2(*x*)[¶](https://docs.python.org/3/library/math.html#math.exp2 "Link to this definition")
:   Return *2* raised to the power *x*.

    Added in version 3.11.

math.expm1(*x*)[¶](https://docs.python.org/3/library/math.html#math.expm1 "Link to this definition")
:   Return *e* raised to the power *x*, minus 1. Here *e* is the base of natural
    logarithms. For small floats *x*, the subtraction in `exp(x) - 1`
    can result in a [significant loss of precision](https://en.wikipedia.org/wiki/Loss_of_significance); the `expm1()`
    function provides a way to compute this quantity to full precision:

    ```
    >>> from math import exp, expm1
    >>> exp(1e-5) - 1  # gives result accurate to 11 places
    1.0000050000069649e-05
    >>> expm1(1e-5)    # result accurate to full precision
    1.0000050000166668e-05
    ```

    Added in version 3.2.

math.log(*x*[, *base*])[¶](https://docs.python.org/3/library/math.html#math.log "Link to this definition")
:   With one argument, return the natural logarithm of *x* (to base *e*).

    With two arguments, return the logarithm of *x* to the given *base*,
    calculated as `log(x)/log(base)`.

math.log1p(*x*)[¶](https://docs.python.org/3/library/math.html#math.log1p "Link to this definition")
:   Return the natural logarithm of *1+x* (base *e*). The
    result is calculated in a way which is accurate for *x* near zero.

math.log2(*x*)[¶](https://docs.python.org/3/library/math.html#math.log2 "Link to this definition")
:   Return the base-2 logarithm of *x*. This is usually more accurate than
    `log(x, 2)`.

    Added in version 3.3.

    See also

    [`int.bit_length()`](https://docs.python.org/3/library/stdtypes.html#int.bit_length "int.bit_length") returns the number of bits necessary to represent
    an integer in binary, excluding the sign and leading zeros.

math.log10(*x*)[¶](https://docs.python.org/3/library/math.html#math.log10 "Link to this definition")
:   Return the base-10 logarithm of *x*. This is usually more accurate
    than `log(x, 10)`.

math.pow(*x*, *y*)[¶](https://docs.python.org/3/library/math.html#math.pow "Link to this definition")
:   Return *x* raised to the power *y*. Exceptional cases follow
    the IEEE 754 standard as far as possible. In particular,
    `pow(1.0, x)` and `pow(x, 0.0)` always return `1.0`, even
    when *x* is a zero or a NaN. If both *x* and *y* are finite,
    *x* is negative, and *y* is not an integer then `pow(x, y)`
    is undefined, and raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").

    Unlike the built-in `**` operator, `math.pow()` converts both
    its arguments to type [`float`](https://docs.python.org/3/library/functions.html#float "float"). Use `**` or the built-in
    `pow()` function for computing exact integer powers.

    Changed in version 3.11: The special cases `pow(0.0, -inf)` and `pow(-0.0, -inf)` were
    changed to return `inf` instead of raising [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"),
    for consistency with IEEE 754.

math.sqrt(*x*)[¶](https://docs.python.org/3/library/math.html#math.sqrt "Link to this definition")
:   Return the square root of *x*.