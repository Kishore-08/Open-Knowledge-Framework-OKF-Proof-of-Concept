---
id: python-special-functions-https-docs-python-org-3-library-math-html--ccfb7324
type: concept
title: Special functions[¶](https://docs.python.org/3/library/math.html#special-functions
  "Link to this heading")
description: math.erf(*x*)[¶](https://docs.python.org/3/library/math.html#math.erf
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/math.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Special functions[¶](https://docs.python.org/3/library/math.html#special-functions "Link to this heading")

math.erf(*x*)[¶](https://docs.python.org/3/library/math.html#math.erf "Link to this definition")
:   Return the [error function](https://en.wikipedia.org/wiki/Error_function) at
    *x*.

    The `erf()` function can be used to compute traditional statistical
    functions such as the [cumulative standard normal distribution](https://en.wikipedia.org/wiki/Cumulative_distribution_function):

    ```
    def phi(x):
        'Cumulative distribution function for the standard normal distribution'
        return (1.0 + erf(x / sqrt(2.0))) / 2.0
    ```

    Added in version 3.2.

math.erfc(*x*)[¶](https://docs.python.org/3/library/math.html#math.erfc "Link to this definition")
:   Return the complementary error function at *x*. The [complementary error
    function](https://en.wikipedia.org/wiki/Error_function) is defined as
    `1.0 - erf(x)`. It is used for large values of *x* where a subtraction
    from one would cause a [loss of significance](https://en.wikipedia.org/wiki/Loss_of_significance).

    Added in version 3.2.

math.gamma(*x*)[¶](https://docs.python.org/3/library/math.html#math.gamma "Link to this definition")
:   Return the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function) at
    *x*.

    Added in version 3.2.

math.lgamma(*x*)[¶](https://docs.python.org/3/library/math.html#math.lgamma "Link to this definition")
:   Return the natural logarithm of the absolute value of the Gamma
    function at *x*.

    Added in version 3.2.