---
id: python-classification-functions-https-docs-python-org-3-library-cma-307d0f07
type: concept
title: Classification functions[¶](https://docs.python.org/3/library/cmath.html#classification-functions
  "Link to this heading")
description: cmath.isfinite(*z*)[¶](https://docs.python.org/3/library/cmath.html#cmath.isfinite
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/cmath.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Classification functions[¶](https://docs.python.org/3/library/cmath.html#classification-functions "Link to this heading")

cmath.isfinite(*z*)[¶](https://docs.python.org/3/library/cmath.html#cmath.isfinite "Link to this definition")
:   Return `True` if both the real and imaginary parts of *z* are finite, and
    `False` otherwise.

    Added in version 3.2.

cmath.isinf(*z*)[¶](https://docs.python.org/3/library/cmath.html#cmath.isinf "Link to this definition")
:   Return `True` if either the real or the imaginary part of *z* is an
    infinity, and `False` otherwise.

cmath.isnan(*z*)[¶](https://docs.python.org/3/library/cmath.html#cmath.isnan "Link to this definition")
:   Return `True` if either the real or the imaginary part of *z* is a NaN,
    and `False` otherwise.

cmath.isclose(*a*, *b*, *\**, *rel\_tol=1e-09*, *abs\_tol=0.0*)[¶](https://docs.python.org/3/library/cmath.html#cmath.isclose "Link to this definition")
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
    as `abs(x) <= rel_tol  * abs(x)`, which is `False` for any `x` and
    rel\_tol less than `1.0`. So add an appropriate positive abs\_tol argument
    to the call.

    The IEEE 754 special values of `NaN`, `inf`, and `-inf` will be
    handled according to IEEE rules. Specifically, `NaN` is not considered
    close to any other value, including `NaN`. `inf` and `-inf` are only
    considered close to themselves.

    Added in version 3.5.

    See also

    [**PEP 485**](https://peps.python.org/pep-0485/) – A function for testing approximate equality