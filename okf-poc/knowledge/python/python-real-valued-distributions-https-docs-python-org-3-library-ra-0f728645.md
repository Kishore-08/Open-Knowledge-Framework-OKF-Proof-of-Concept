---
id: python-real-valued-distributions-https-docs-python-org-3-library-ra-0f728645
type: concept
title: Real-valued distributions[¶](https://docs.python.org/3/library/random.html#real-valued-distributions
  "Link to this heading")
description: The following functions generate specific real-valued distributions.
  Function
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Real-valued distributions[¶](https://docs.python.org/3/library/random.html#real-valued-distributions "Link to this heading")

The following functions generate specific real-valued distributions. Function
parameters are named after the corresponding variables in the distribution’s
equation, as used in common mathematical practice; most of these equations can
be found in any statistics text.

random.random()[¶](https://docs.python.org/3/library/random.html#random.random "Link to this definition")
:   Return the next random floating-point number in the range `0.0 <= X < 1.0`

random.uniform(*a*, *b*)[¶](https://docs.python.org/3/library/random.html#random.uniform "Link to this definition")
:   Return a random floating-point number *N* such that `a <= N <= b` for
    `a <= b` and `b <= N <= a` for `b < a`.

    The end-point value `b` may or may not be included in the range
    depending on floating-point rounding in the expression
    `a + (b-a) * random()`.

random.triangular(*low*, *high*, *mode*)[¶](https://docs.python.org/3/library/random.html#random.triangular "Link to this definition")
:   Return a random floating-point number *N* such that `low <= N <= high` and
    with the specified *mode* between those bounds. The *low* and *high* bounds
    default to zero and one. The *mode* argument defaults to the midpoint
    between the bounds, giving a symmetric distribution.

random.betavariate(*alpha*, *beta*)[¶](https://docs.python.org/3/library/random.html#random.betavariate "Link to this definition")
:   Beta distribution. Conditions on the parameters are `alpha > 0` and
    `beta > 0`. Returned values range between 0 and 1.

random.expovariate(*lambd=1.0*)[¶](https://docs.python.org/3/library/random.html#random.expovariate "Link to this definition")
:   Exponential distribution. *lambd* is 1.0 divided by the desired
    mean. It should be nonzero. (The parameter would be called
    “lambda”, but that is a reserved word in Python.) Returned values
    range from 0 to positive infinity if *lambd* is positive, and from
    negative infinity to 0 if *lambd* is negative.

    Changed in version 3.12: Added the default value for `lambd`.

random.gammavariate(*alpha*, *beta*)[¶](https://docs.python.org/3/library/random.html#random.gammavariate "Link to this definition")
:   Gamma distribution. (*Not* the gamma function!) The shape and
    scale parameters, *alpha* and *beta*, must have positive values.
    (Calling conventions vary and some sources define ‘beta’
    as the inverse of the scale).

    The probability distribution function is:

    ```
              x ** (alpha - 1) * math.exp(-x / beta)
    pdf(x) =  --------------------------------------
                math.gamma(alpha) * beta ** alpha
    ```

random.gauss(*mu=0.0*, *sigma=1.0*)[¶](https://docs.python.org/3/library/random.html#random.gauss "Link to this definition")
:   Normal distribution, also called the Gaussian distribution.
    *mu* is the mean,
    and *sigma* is the standard deviation. This is slightly faster than
    the [`normalvariate()`](https://docs.python.org/3/library/random.html#random.normalvariate "random.normalvariate") function defined below.

    Multithreading note: When two threads call this function
    simultaneously, it is possible that they will receive the
    same return value. This can be avoided in three ways.
    1) Have each thread use a different instance of the random
    number generator. 2) Put locks around all calls. 3) Use the
    slower, but thread-safe [`normalvariate()`](https://docs.python.org/3/library/random.html#random.normalvariate "random.normalvariate") function instead.

    Changed in version 3.11: *mu* and *sigma* now have default arguments.

random.lognormvariate(*mu*, *sigma*)[¶](https://docs.python.org/3/library/random.html#random.lognormvariate "Link to this definition")
:   Log normal distribution. If you take the natural logarithm of this
    distribution, you’ll get a normal distribution with mean *mu*