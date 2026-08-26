---
id: python-examples-of-usage-timedelta-https-docs-python-org-3-library--30088197
type: concept
title: 'Examples of usage: `timedelta`[¶](https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta
  "Link to this heading")'
description: 'An additional example of normalization:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Examples of usage: `timedelta`[¶](https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta "Link to this heading")

An additional example of normalization:

```
>>> # Components of another_year add up to exactly 365 days
>>> import datetime as dt
>>> year = dt.timedelta(days=365)
>>> another_year = dt.timedelta(weeks=40, days=84, hours=23,
...                             minutes=50, seconds=600)
>>> year == another_year
True
>>> year.total_seconds()
31536000.0
```

Examples of [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") arithmetic:

```
>>> import datetime as dt
>>> year = dt.timedelta(days=365)
>>> ten_years = 10 * year
>>> ten_years
datetime.timedelta(days=3650)
>>> ten_years.days // 365
10
>>> nine_years = ten_years - year
>>> nine_years
datetime.timedelta(days=3285)
>>> three_years = nine_years // 3
>>> three_years, three_years.days // 365
(datetime.timedelta(days=1095), 3)
```