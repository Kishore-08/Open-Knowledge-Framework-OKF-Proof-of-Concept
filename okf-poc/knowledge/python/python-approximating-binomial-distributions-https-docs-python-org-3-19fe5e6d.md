---
id: python-approximating-binomial-distributions-https-docs-python-org-3-19fe5e6d
type: concept
title: Approximating binomial distributions[¶](https://docs.python.org/3/library/statistics.html#approximating-binomial-distributions
  "Link to this heading")
description: Normal distributions can be used to approximate [Binomial
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/statistics.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Approximating binomial distributions[¶](https://docs.python.org/3/library/statistics.html#approximating-binomial-distributions "Link to this heading")

Normal distributions can be used to approximate [Binomial
distributions](https://mathworld.wolfram.com/BinomialDistribution.html)
when the sample size is large and when the probability of a successful
trial is near 50%.

For example, an open source conference has 750 attendees and two rooms with a
500 person capacity. There is a talk about Python and another about Ruby.
In previous conferences, 65% of the attendees preferred to listen to Python
talks. Assuming the population preferences haven’t changed, what is the
probability that the Python room will stay within its capacity limits?

```
>>> n = 750             # Sample size
>>> p = 0.65            # Preference for Python
>>> q = 1.0 - p         # Preference for Ruby
>>> k = 500             # Room capacity

>>> # Approximation using the cumulative normal distribution
>>> from math import sqrt
>>> round(NormalDist(mu=n*p, sigma=sqrt(n*p*q)).cdf(k + 0.5), 4)
0.8402

>>> # Exact solution using the cumulative binomial distribution
>>> from math import comb, fsum
>>> round(fsum(comb(n, r) * p**r * q**(n-r) for r in range(k+1)), 4)
0.8402

>>> # Approximation using a simulation
>>> from random import seed, binomialvariate
>>> seed(8675309)
>>> mean(binomialvariate(n, p) <= k for i in range(10_000))
0.8406
```