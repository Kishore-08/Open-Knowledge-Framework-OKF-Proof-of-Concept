---
id: python-number-theoretic-functions-https-docs-python-org-3-library-m-ccfb7324
type: concept
title: Number-theoretic functions[¶](https://docs.python.org/3/library/math.html#number-theoretic-functions
  "Link to this heading")
description: math.comb(*n*, *k*)[¶](https://docs.python.org/3/library/math.html#math.comb
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/math.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Number-theoretic functions[¶](https://docs.python.org/3/library/math.html#number-theoretic-functions "Link to this heading")

math.comb(*n*, *k*)[¶](https://docs.python.org/3/library/math.html#math.comb "Link to this definition")
:   Return the number of ways to choose *k* items from *n* items without repetition
    and without order.

    Evaluates to `n! / (k! * (n - k)!)` when `k <= n` and evaluates
    to zero when `k > n`.

    Also called the binomial coefficient because it is equivalent
    to the coefficient of k-th term in polynomial expansion of
    `(1 + x)ⁿ`.

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if either of the arguments are not integers.
    Raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if either of the arguments are negative.

    Added in version 3.8.

math.factorial(*n*)[¶](https://docs.python.org/3/library/math.html#math.factorial "Link to this definition")
:   Return factorial of the nonnegative integer *n*.

    Changed in version 3.10: Floats with integral values (like `5.0`) are no longer accepted.

math.gcd(*\*integers*)[¶](https://docs.python.org/3/library/math.html#math.gcd "Link to this definition")
:   Return the greatest common divisor of the specified integer arguments.
    If any of the arguments is nonzero, then the returned value is the largest
    positive integer that is a divisor of all arguments. If all arguments
    are zero, then the returned value is `0`. `gcd()` without arguments
    returns `0`.

    Added in version 3.5.

    Changed in version 3.9: Added support for an arbitrary number of arguments. Formerly, only two
    arguments were supported.

math.isqrt(*n*)[¶](https://docs.python.org/3/library/math.html#math.isqrt "Link to this definition")
:   Return the integer square root of the nonnegative integer *n*. This is the
    floor of the exact square root of *n*, or equivalently the greatest integer
    *a* such that *a*² ≤ *n*.

    For some applications, it may be more convenient to have the least integer
    *a* such that *n* ≤ *a*², or in other words the ceiling of
    the exact square root of *n*. For positive *n*, this can be computed using
    `a = 1 + isqrt(n - 1)`.

    Added in version 3.8.

math.lcm(*\*integers*)[¶](https://docs.python.org/3/library/math.html#math.lcm "Link to this definition")
:   Return the least common multiple of the specified integer arguments.
    If all arguments are nonzero, then the returned value is the smallest
    positive integer that is a multiple of all arguments. If any of the arguments
    is zero, then the returned value is `0`. `lcm()` without arguments
    returns `1`.

    Added in version 3.9.

math.perm(*n*, *k=None*)[¶](https://docs.python.org/3/library/math.html#math.perm "Link to this definition")
:   Return the number of ways to choose *k* items from *n* items
    without repetition and with order.

    Evaluates to `n! / (n - k)!` when `k <= n` and evaluates
    to zero when `k > n`.

    If *k* is not specified or is `None`, then *k* defaults to *n*
    and the function returns `n!`.

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if either of the arguments are not integers.
    Raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if either of the arguments are negative.

    Added in version 3.8.