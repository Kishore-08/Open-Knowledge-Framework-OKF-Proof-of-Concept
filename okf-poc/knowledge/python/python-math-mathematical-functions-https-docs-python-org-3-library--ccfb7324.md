---
id: python-math-mathematical-functions-https-docs-python-org-3-library--ccfb7324
type: concept
title: '`math` — Mathematical functions[¶](https://docs.python.org/3/library/math.html#m'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/math.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `math` — Mathematical functions[¶](https://docs.python.org/3/library/math.html#module-math "Link to this heading")

---

This module provides access to common mathematical functions and constants,
including those defined by the C standard.

These functions cannot be used with complex numbers; use the functions of the
same name from the [`cmath`](https://docs.python.org/3/library/cmath.html#module-cmath "cmath: Mathematical functions for complex numbers.") module if you require support for complex
numbers. The distinction between functions which support complex numbers and
those which don’t is made since most users do not want to learn quite as much
mathematics as required to understand complex numbers. Receiving an exception
instead of a complex result allows earlier detection of the unexpected complex
number used as a parameter, so that the programmer can determine how and why it
was generated in the first place.

The following functions are provided by this module. Except when explicitly
noted otherwise, all return values are floats.

|  |  |
| --- | --- |
| **Number-theoretic functions** | |
| [`comb(n, k)`](https://docs.python.org/3/library/math.html#math.comb "math.comb") | Number of ways to choose *k* items from *n* items without repetition and without order |
| [`factorial(n)`](https://docs.python.org/3/library/math.html#math.factorial "math.factorial") | *n* factorial |
| [`gcd(*integers)`](https://docs.python.org/3/library/math.html#math.gcd "math.gcd") | Greatest common divisor of the integer arguments |
| [`isqrt(n)`](https://docs.python.org/3/library/math.html#math.isqrt "math.isqrt") | Integer square root of a nonnegative integer *n* |
| [`lcm(*integers)`](https://docs.python.org/3/library/math.html#math.lcm "math.lcm") | Least common multiple of the integer arguments |
| [`perm(n, k)`](https://docs.python.org/3/library/math.html#math.perm "math.perm") | Number of ways to choose *k* items from *n* items without repetition and with order |
| **Floating point arithmetic** | |
| [`ceil(x)`](https://docs.python.org/3/library/math.html#math.ceil "math.ceil") | Ceiling of *x*, the smallest integer greater than or equal to *x* |
| [`fabs(x)`](https://docs.python.org/3/library/math.html#math.fabs "math.fabs") | Absolute value of *x* |
| [`floor(x)`](https://docs.python.org/3/library/math.html#math.floor "math.floor") | Floor of *x*, the largest integer less than or equal to *x* |
| [`fma(x, y, z)`](https://docs.python.org/3/library/math.html#math.fma "math.fma") | Fused multiply-add operation: `(x * y) + z` |
| [`fmod(x, y)`](https://docs.python.org/3/library/math.html#math.fmod "math.fmod") | Remainder of division `x / y` |
| [`modf(x)`](https://docs.python.org/3/library/math.html#math.modf "math.modf") | Fractional and integer parts of *x* |
| [`remainder(x, y)`](https://docs.python.org/3/library/math.html#math.remainder "math.remainder") | Remainder of *x* with respect to *y* |
| [`trunc(x)`](https://docs.python.org/3/library/math.html#math.trunc "math.trunc") | Integer part of *x* |
| **Floating point manipulation functions** | |
| [`copysign(x, y)`](https://docs.python.org/3/library/math.html#math.copysign "math.copysign") | Magnitude (absolute value) of *x* with the sign of *y* |
| [`frexp(x)`](https://docs.python.org/3/library/math.html#math.frexp "math.frexp") | Mantissa and exponent of *x* |
| [`isclose(a, b, rel_tol, abs_tol)`](https://docs.python.org/3/library/math.html#math.isclose "math.isclose") | Check if the values *a* and *b* are close to each other |
| [`isfinite(x)`](https://docs.python.org/3/library/math.html#math.isfinite "math.isfinite") | Check if *x* is neither an infinity nor a NaN |
| [`isinf(x)`](https://docs.python.org/3/library/math.html#math.isinf "math.isinf") | Check if *x* is a positive or negative infinity |
| [`isnan(x)`](https://docs.python.org/3/library/math.html#math.isnan "math.isnan") | Check if *x* is a NaN (not a number) |
| [`ldexp(x, i)`](https://docs.python.org/3/library/math