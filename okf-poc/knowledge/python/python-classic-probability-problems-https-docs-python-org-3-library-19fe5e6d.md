---
id: python-classic-probability-problems-https-docs-python-org-3-library-19fe5e6d
type: concept
title: Classic probability problems[¶](https://docs.python.org/3/library/statistics.html#classic-probability-problems
  "Link to this heading")
description: '[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist
  "statistics.NormalDist") readily solves classic probability problems.'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/statistics.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Classic probability problems[¶](https://docs.python.org/3/library/statistics.html#classic-probability-problems "Link to this heading")

[`NormalDist`](https://docs.python.org/3/library/statistics.html#statistics.NormalDist "statistics.NormalDist") readily solves classic probability problems.

For example, given [historical data for SAT exams](https://nces.ed.gov/programs/digest/d17/tables/dt17_226.40.asp) showing
that scores are normally distributed with a mean of 1060 and a standard
deviation of 195, determine the percentage of students with test scores
between 1100 and 1200, after rounding to the nearest whole number:

```
>>> sat = NormalDist(1060, 195)
>>> fraction = sat.cdf(1200 + 0.5) - sat.cdf(1100 - 0.5)
>>> round(fraction * 100.0, 1)
18.4
```

Find the [quartiles](https://en.wikipedia.org/wiki/Quartile) and [deciles](https://en.wikipedia.org/wiki/Decile) for the SAT scores:

```
>>> list(map(round, sat.quantiles()))
[928, 1060, 1192]
>>> list(map(round, sat.quantiles(n=10)))
[810, 896, 958, 1011, 1060, 1109, 1162, 1224, 1310]
```