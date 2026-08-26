---
id: python-monte-carlo-inputs-for-simulations-https-docs-python-org-3-l-19fe5e6d
type: concept
title: Monte Carlo inputs for simulations[¶](https://docs.python.org/3/library/statistics.html#monte-carlo-inputs-for-simulations
  "Link to this heading")
description: To estimate the distribution for a model that isn’t easy to solve
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/statistics.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Monte Carlo inputs for simulations[¶](https://docs.python.org/3/library/statistics.html#monte-carlo-inputs-for-simulations "Link to this heading")

To estimate the distribution for a model that isn’t easy to solve
analytically, [`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist") can generate input samples for a [Monte
Carlo simulation](https://en.wikipedia.org/wiki/Monte_Carlo_method):

```
>>> def model(x, y, z):
...     return (3*x + 7*x*y - 5*y) / (11 * z)
...
>>> n = 100_000
>>> X = NormalDist(10, 2.5).samples(n, seed=3652260728)
>>> Y = NormalDist(15, 1.75).samples(n, seed=4582495471)
>>> Z = NormalDist(50, 1.25).samples(n, seed=6582483453)
>>> quantiles(map(model, X, Y, Z))
[1.4591308524824727, 1.8035946855390597, 2.175091447274739]
```