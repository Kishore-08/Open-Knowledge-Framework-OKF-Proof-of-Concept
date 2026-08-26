---
id: python-summation-and-product-functions-https-docs-python-org-3-libr-ccfb7324
type: concept
title: Summation and product functions[¶](https://docs.python.org/3/library/math.html#summation-and-product-functions
  "Link to this heading")
description: math.dist(*p*, *q*)[¶](https://docs.python.org/3/library/math.html#math.dist
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/math.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Summation and product functions[¶](https://docs.python.org/3/library/math.html#summation-and-product-functions "Link to this heading")

math.dist(*p*, *q*)[¶](https://docs.python.org/3/library/math.html#math.dist "Link to this definition")
:   Return the Euclidean distance between two points *p* and *q*, each
    given as a sequence (or iterable) of coordinates. The two points
    must have the same dimension.

    Roughly equivalent to:

    ```
    sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    ```

    Added in version 3.8.

math.fsum(*iterable*)[¶](https://docs.python.org/3/library/math.html#math.fsum "Link to this definition")
:   Return an accurate floating-point sum of values in the iterable. Avoids
    loss of precision by tracking multiple intermediate partial sums.

    The algorithm’s accuracy depends on IEEE-754 arithmetic guarantees and the
    typical case where the rounding mode is half-even. On some non-Windows
    builds, the underlying C library uses extended precision addition and may
    occasionally double-round an intermediate sum causing it to be off in its
    least significant bit.

    For further discussion and two alternative approaches, see the [ASPN cookbook
    recipes for accurate floating-point summation](https://code.activestate.com/recipes/393090-binary-floating-point-summation-accurate-to-full-p/).

math.hypot(*\*coordinates*)[¶](https://docs.python.org/3/library/math.html#math.hypot "Link to this definition")
:   Return the Euclidean norm, `sqrt(sum(x**2 for x in coordinates))`.
    This is the length of the vector from the origin to the point
    given by the coordinates.

    For a two dimensional point `(x, y)`, this is equivalent to computing
    the hypotenuse of a right triangle using the Pythagorean theorem,
    `sqrt(x*x + y*y)`.

    Changed in version 3.8: Added support for n-dimensional points. Formerly, only the two
    dimensional case was supported.

    Changed in version 3.10: Improved the algorithm’s accuracy so that the maximum error is
    under 1 ulp (unit in the last place). More typically, the result
    is almost always correctly rounded to within 1/2 ulp.

math.prod(*iterable*, *\**, *start=1*)[¶](https://docs.python.org/3/library/math.html#math.prod "Link to this definition")
:   Calculate the product of all the elements in the input *iterable*.
    The default *start* value for the product is `1`.

    When the iterable is empty, return the start value. This function is
    intended specifically for use with numeric values and may reject
    non-numeric types.

    Added in version 3.8.

math.sumprod(*p*, *q*)[¶](https://docs.python.org/3/library/math.html#math.sumprod "Link to this definition")
:   Return the sum of products of values from two iterables *p* and *q*.

    Raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the inputs do not have the same length.

    Roughly equivalent to:

    ```
    sum(map(operator.mul, p, q, strict=True))
    ```

    For float and mixed int/float inputs, the intermediate products
    and sums are computed with extended precision.

    Added in version 3.12.