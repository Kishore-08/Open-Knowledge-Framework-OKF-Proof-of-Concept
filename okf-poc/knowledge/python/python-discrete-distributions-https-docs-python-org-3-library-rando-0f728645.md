---
id: python-discrete-distributions-https-docs-python-org-3-library-rando-0f728645
type: concept
title: Discrete distributions[¶](https://docs.python.org/3/library/random.html#discrete-distributions
  "Link to this heading")
description: The following function generates a discrete distribution.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Discrete distributions[¶](https://docs.python.org/3/library/random.html#discrete-distributions "Link to this heading")

The following function generates a discrete distribution.

random.binomialvariate(*n=1*, *p=0.5*)[¶](https://docs.python.org/3/library/random.html#random.binomialvariate "Link to this definition")
:   [Binomial distribution](https://mathworld.wolfram.com/BinomialDistribution.html).
    Return the number of successes for *n* independent trials with the
    probability of success in each trial being *p*:

    Mathematically equivalent to:

    ```
    sum(random() < p for i in range(n))
    ```

    The number of trials *n* should be a non-negative integer.
    The probability of success *p* should be between `0.0 <= p <= 1.0`.
    The result is an integer in the range `0 <= X <= n`.

    Added in version 3.12.