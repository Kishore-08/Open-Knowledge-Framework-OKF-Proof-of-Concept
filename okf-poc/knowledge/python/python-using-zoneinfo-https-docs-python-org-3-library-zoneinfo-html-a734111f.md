---
id: python-using-zoneinfo-https-docs-python-org-3-library-zoneinfo-html-a734111f
type: concept
title: Using `ZoneInfo`[¶](https://docs.python.org/3/library/zoneinfo.html#using-zoneinfo
  "Link to this heading")
description: '[`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo
  "zoneinfo.ZoneInfo") is a concrete implementation of the [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.h'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Using `ZoneInfo`[¶](https://docs.python.org/3/library/zoneinfo.html#using-zoneinfo "Link to this heading")

[`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") is a concrete implementation of the [`datetime.tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo")
abstract base class, and is intended to be attached to `tzinfo`, either via
the constructor, the [`datetime.replace`](https://docs.python.org/3/library/datetime.html#datetime.datetime.replace "datetime.datetime.replace")
method or [`datetime.astimezone`](https://docs.python.org/3/library/datetime.html#datetime.datetime.astimezone "datetime.datetime.astimezone"):

```
>>> from zoneinfo import ZoneInfo
>>> import datetime as dt

>>> when = dt.datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(when)
2020-10-31 12:00:00-07:00

>>> when.tzname()
'PDT'
```

Datetimes constructed in this way are compatible with datetime arithmetic and
handle daylight saving time transitions with no further intervention:

```
>>> when_add = when + dt.timedelta(days=1)

>>> print(when_add)
2020-11-01 12:00:00-08:00

>>> when_add.tzname()
'PST'
```

These time zones also support the [`fold`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fold "datetime.datetime.fold") attribute
introduced in [**PEP 495**](https://peps.python.org/pep-0495/). During offset transitions which induce ambiguous
times (such as a daylight saving time to standard time transition), the offset
from *before* the transition is used when `fold=0`, and the offset *after*
the transition is used when `fold=1`, for example:

```
>>> when = dt.datetime(2020, 11, 1, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(when)
2020-11-01 01:00:00-07:00

>>> print(when.replace(fold=1))
2020-11-01 01:00:00-08:00
```

When converting from another time zone, the fold will be set to the correct
value:

```
>>> LOS_ANGELES = ZoneInfo("America/Los_Angeles")
>>> when_utc = dt.datetime(2020, 11, 1, 8, tzinfo=dt.timezone.utc)

>>> # Before the PDT -> PST transition
>>> print(when_utc.astimezone(LOS_ANGELES))
2020-11-01 01:00:00-07:00

>>> # After the PDT -> PST transition
>>> print((when_utc + dt.timedelta(hours=1)).astimezone(LOS_ANGELES))
2020-11-01 01:00:00-08:00
```