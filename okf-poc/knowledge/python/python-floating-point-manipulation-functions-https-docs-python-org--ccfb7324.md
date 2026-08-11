---
id: python-floating-point-manipulation-functions-https-docs-python-org--ccfb7324
type: concept
title: Floating point manipulation functions[¶](https://docs.python.org/3/library/math.html#floating-point-manipulation-functions
  "Link to this heading")
description: math.copysign(*x*, *y*)[¶](https://docs.python.org/3/library/math.html#math.copysign
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/math.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Floating point manipulation functions[¶](https://docs.python.org/3/library/math.html#floating-point-manipulation-functions "Link to this heading")

math.copysign(*x*, *y*)[¶](https://docs.python.org/3/library/math.html#math.copysign "Link to this definition")
:   Return a float with the magnitude (absolute value) of *x* but the sign of
    *y*. On platforms that support signed zeros, `copysign(1.0, -0.0)`
    returns *-1.0*.

math.frexp(*x*)[¶](https://docs.python.org/3/library/math.html#math.frexp "Link to this definition")
:   Return the mantissa and exponent of *x* as the pair `(m, e)`.
    If *x* is a finite nonzero number, then *m* is a float with
    `0.5 <= abs(m) < 1.0` and an integer *e* is such that
    `x == m * 2**e` exactly. Else, return `(x, 0)`.
    This is used to “pick apart” the internal representation of
    a float in a portable way.

    Note that `frexp()` has a different call/return pattern
    than its C equivalents: it takes a single argument and return a pair of
    values, rather than returning its second return value through an ‘output
    parameter’ (there is no such thing in Python).

math.isclose(*a*, *b*, *\**, *rel\_tol=1e-09*, *abs\_tol=0.0*)[¶](https://docs.python.org/3/library/math.html#math.isclose "Link to this definition")
:   Return `True` if the values *a* and *b* are close to each other and
    `False` otherwise.

    Whether or not two values are considered close is determined according to
    given absolute and relative tolerances. If no errors occur, the result will
    be: `abs(a-b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`.

    *rel\_tol* is the relative tolerance – it is the maximum allowed difference
    between *a* and *b*, relative to the larger absolute value of *a* or *b*.
    For example, to set a tolerance of 5%, pass `rel_tol=0.05`. The default
    tolerance is `1e-09`, which assures that the two values are the same
    within about 9 decimal digits. *rel\_tol* must be nonnegative and less
    than `1.0`.

    *abs\_tol* is the absolute tolerance; it defaults to `0.0` and it must be
    nonnegative. When comparing `x` to `0.0`, `isclose(x, 0)` is computed
    as `abs(x) <= rel_tol  * abs(x)`, which is `False` for any nonzero `x` and
    *rel\_tol* less than `1.0`. So add an appropriate positive *abs\_tol* argument
    to the call.

    The IEEE 754 special values of `NaN`, `inf`, and `-inf` will be
    handled according to IEEE rules. Specifically, `NaN` is not considered
    close to any other value, including `NaN`. `inf` and `-inf` are only
    considered close to themselves.

    Added in version 3.5.

    See also

    [**PEP 485**](https://peps.python.org/pep-0485/) – A function for testing approximate equality

math.isfinite(*x*)[¶](https://docs.python.org/3/library/math.html#math.isfinite "Link to this definition")
:   Return `True` if *x* is neither an infinity nor a NaN, and
    `False` otherwise. (Note that `0.0` *is* considered finite.)

    Added in version 3.2.

math.isinf(*x*)[¶](https://docs.python.org/3/library/math.html#math.isinf "Link to this definition")
:   Return `True` if *x* is a positive or negative infinity, and
    `False` otherwise.

math.isnan(*x*)[¶](https://docs.python.org/3/library/math.html#math.isnan "Link to this definition")
:   Return `True` if *x* is a NaN (not a number), and `False` otherwise.

math.ldexp(*x*, *i*)[¶](https://docs.python.org/3/library/math.html#math.ldexp "Link to this definition")
:   Return `x * (2**i)`. This is essentially the inverse of function
    [`frexp()`](https://docs.python.org/3/library/math.html#math.frexp "math.frexp").

math.nextafter(*x*, *y*, *steps=1*)[¶](https://docs.python.org/3/library/math.html#math.nextafter "Link to this definition")
:   Return the floating-point value *steps* steps after *x* towards *y*.

    If *x* is equal to *y*, return *y*, unless *steps* is zero.

    Examples:

    - `math.nextafter(x, math.inf)` goes up: towards positive infinity.
    - `math.nextafter(x, -m