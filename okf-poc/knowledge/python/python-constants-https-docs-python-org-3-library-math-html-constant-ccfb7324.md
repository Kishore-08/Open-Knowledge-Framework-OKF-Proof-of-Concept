---
id: python-constants-https-docs-python-org-3-library-math-html-constant-ccfb7324
type: concept
title: Constants[¶](https://docs.python.org/3/library/math.html#constants "Link to
  this heading")
description: math.pi[¶](https://docs.python.org/3/library/math.html#math.pi "Link
  to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/math.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Constants[¶](https://docs.python.org/3/library/math.html#constants "Link to this heading")

math.pi[¶](https://docs.python.org/3/library/math.html#math.pi "Link to this definition")
:   The mathematical constant *π* = 3.141592…, to available precision.

math.e[¶](https://docs.python.org/3/library/math.html#math.e "Link to this definition")
:   The mathematical constant *e* = 2.718281…, to available precision.

math.tau[¶](https://docs.python.org/3/library/math.html#math.tau "Link to this definition")
:   The mathematical constant *τ* = 6.283185…, to available precision.
    Tau is a circle constant equal to 2*π*, the ratio of a circle’s circumference to
    its radius. To learn more about Tau, check out Vi Hart’s video [Pi is (still)
    Wrong](https://vimeo.com/147792667), and start celebrating
    [Tau day](https://tauday.com/) by eating twice as much pie!

    Added in version 3.6.

math.inf[¶](https://docs.python.org/3/library/math.html#math.inf "Link to this definition")
:   A floating-point positive infinity. (For negative infinity, use
    `-math.inf`.) Equivalent to the output of `float('inf')`.

    Added in version 3.5.

math.nan[¶](https://docs.python.org/3/library/math.html#math.nan "Link to this definition")
:   A floating-point “not a number” (NaN) value. Equivalent to the output of
    `float('nan')`. Due to the requirements of the [IEEE-754 standard](https://en.wikipedia.org/wiki/IEEE_754), `math.nan` and `float('nan')` are
    not considered to equal to any other numeric value, including themselves. To check
    whether a number is a NaN, use the [`isnan()`](https://docs.python.org/3/library/math.html#math.isnan "math.isnan") function to test
    for NaNs instead of `is` or `==`.
    Example:

    ```
    >>> import math
    >>> math.nan == math.nan
    False
    >>> float('nan') == float('nan')
    False
    >>> math.isnan(math.nan)
    True
    >>> math.isnan(float('nan'))
    True
    ```

    Added in version 3.5.

    Changed in version 3.11: It is now always available.

**CPython implementation detail:** The `math` module consists mostly of thin wrappers around the platform C
math library functions. Behavior in exceptional cases follows Annex F of
the C99 standard where appropriate. The current implementation will raise
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") for invalid operations like `sqrt(-1.0)` or `log(0.0)`
(where C99 Annex F recommends signaling invalid operation or divide-by-zero),
and [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") for results that overflow (for example,
`exp(1000.0)`). A NaN will not be returned from any of the functions
above unless one or more of the input arguments was a NaN; in that case,
most functions will return a NaN, but (again following C99 Annex F) there
are some exceptions to this rule, for example `pow(float('nan'), 0.0)` or
`hypot(float('nan'), float('inf'))`.

Note that Python makes no effort to distinguish signaling NaNs from
quiet NaNs, and behavior for signaling NaNs remains unspecified.
Typical behavior is to treat all NaNs as though they were quiet.

See also

Module [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.")
:   Complex number versions of many of these functions.