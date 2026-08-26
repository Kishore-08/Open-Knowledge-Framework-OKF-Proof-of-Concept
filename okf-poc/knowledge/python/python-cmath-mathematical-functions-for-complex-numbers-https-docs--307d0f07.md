---
id: python-cmath-mathematical-functions-for-complex-numbers-https-docs--307d0f07
type: concept
title: '`cmath` — Mathematical functions for complex numbers[¶](https://docs.python.org/'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/cmath.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `cmath` — Mathematical functions for complex numbers[¶](https://docs.python.org/3/library/cmath.html#module-cmath "Link to this heading")

---

This module provides access to mathematical functions for complex numbers. The
functions in this module accept integers, floating-point numbers or complex
numbers as arguments. They will also accept any Python object that has either a
[`__complex__()`](https://docs.python.org/3/reference/datamodel.html#object.__complex__ "object.__complex__") or a [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__") method: these methods are used to
convert the object to a complex or floating-point number, respectively, and
the function is then applied to the result of the conversion.

Note

For functions involving branch cuts, we have the problem of deciding how to
define those functions on the cut itself. Following Kahan’s “Branch cuts for
complex elementary functions” paper, as well as Annex G of C99 and later C
standards, we use the sign of zero to distinguish one side of the branch cut
from the other: for a branch cut along (a portion of) the real axis we look
at the sign of the imaginary part, while for a branch cut along the
imaginary axis we look at the sign of the real part.

For example, the [`cmath.sqrt()`](https://docs.python.org/3/library/cmath.html#cmath.sqrt "cmath.sqrt") function has a branch cut along the
negative real axis. An argument of `-2-0j` is treated as
though it lies *below* the branch cut, and so gives a result on the negative
imaginary axis:

```
>>> cmath.sqrt(-2-0j)
-1.4142135623730951j
```

But an argument of `-2+0j` is treated as though it lies above
the branch cut:

```
>>> cmath.sqrt(-2+0j)
1.4142135623730951j
```

|  |  |
| --- | --- |
| **Conversions to and from polar coordinates** | |
| [`phase(z)`](https://docs.python.org/3/library/cmath.html#cmath.phase "cmath.phase") | Return the phase of *z* |
| [`polar(z)`](https://docs.python.org/3/library/cmath.html#cmath.polar "cmath.polar") | Return the representation of *z* in polar coordinates |
| [`rect(r, phi)`](https://docs.python.org/3/library/cmath.html#cmath.rect "cmath.rect") | Return the complex number *z* with polar coordinates *r* and *phi* |
| **Power and logarithmic functions** | |
| [`exp(z)`](https://docs.python.org/3/library/cmath.html#cmath.exp "cmath.exp") | Return *e* raised to the power *z* |
| [`log(z[, base])`](https://docs.python.org/3/library/cmath.html#cmath.log "cmath.log") | Return the logarithm of *z* to the given *base* (*e* by default) |
| [`log10(z)`](https://docs.python.org/3/library/cmath.html#cmath.log10 "cmath.log10") | Return the base-10 logarithm of *z* |
| [`sqrt(z)`](https://docs.python.org/3/library/cmath.html#cmath.sqrt "cmath.sqrt") | Return the square root of *z* |
| **Trigonometric functions** | |
| [`acos(z)`](https://docs.python.org/3/library/cmath.html#cmath.acos "cmath.acos") | Return the arc cosine of *z* |
| [`asin(z)`](https://docs.python.org/3/library/cmath.html#cmath.asin "cmath.asin") | Return the arc sine of *z* |
| [`atan(z)`](https://docs.python.org/3/library/cmath.html#cmath.atan "cmath.atan") | Return the arc tangent of *z* |
| [`cos(z)`](https://docs.python.org/3/library/cmath.html#cmath.cos "cmath.cos") | Return the cosine of *z* |
| [`sin(z)`](https://docs.python.org/3/library/cmath.html#cmath.sin "cmath.sin") | Return the sine of *z* |
| [`tan(z)`](https://docs.python.org/3/library/cmath.html#cmath.tan "cmath.tan") | Return the tangent of *z* |
| **Hyperbolic functions** | |
| [`acosh(z)`](https://docs.python.org/3/library/cmath.html#cmath.acosh "cmath.acosh") | Return the inverse hyperbolic cosine of *z* |
| [`asinh(z)`](https://docs.python.org/3/library/cmath.html#cmath.asinh "cmath.asinh") | Return the inverse hyperbolic sine of *z* |
| [`atanh(z)`](https://docs.python.org/3/library/cmath.html#cmath.atanh "cmath.atanh") | Return the inverse hyperbolic tangent of *z* |
| [`cosh(z)`](https://docs.python.org/