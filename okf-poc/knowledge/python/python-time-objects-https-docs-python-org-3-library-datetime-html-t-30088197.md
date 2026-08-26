---
id: python-time-objects-https-docs-python-org-3-library-datetime-html-t-30088197
type: concept
title: '`time` objects[¶](https://docs.python.org/3/library/datetime.html#time-objects
  "Link to this heading")'
description: A [`time`](https://docs.python.org/3/library/datetime.html#datetime.time
  "datetime.time") object represents a (local) time of day, independent of any particular
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## `time` objects[¶](https://docs.python.org/3/library/datetime.html#time-objects "Link to this heading")

A [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object represents a (local) time of day, independent of any particular
day, and subject to adjustment via a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") object.

*class* datetime.time(*hour=0*, *minute=0*, *second=0*, *microsecond=0*, *tzinfo=None*, *\**, *fold=0*)[¶](https://docs.python.org/3/library/datetime.html#datetime.time "Link to this definition")
:   All arguments are optional. *tzinfo* may be `None`, or an instance of a
    [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass. The remaining arguments must be integers in the
    following ranges:

    - `0 <= hour < 24`,
    - `0 <= minute < 60`,
    - `0 <= second < 60`,
    - `0 <= microsecond < 1000000`,
    - `fold in [0, 1]`.

    If an argument outside those ranges is given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. All
    default to 0 except *tzinfo*, which defaults to `None`.

Class attributes:

time.min[¶](https://docs.python.org/3/library/datetime.html#datetime.time.min "Link to this definition")
:   The earliest representable [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time"), `time(0, 0, 0, 0)`.

time.max[¶](https://docs.python.org/3/library/datetime.html#datetime.time.max "Link to this definition")
:   The latest representable [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time"), `time(23, 59, 59, 999999)`.

time.resolution[¶](https://docs.python.org/3/library/datetime.html#datetime.time.resolution "Link to this definition")
:   The smallest possible difference between non-equal [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects,
    `timedelta(microseconds=1)`, although note that arithmetic on
    `time` objects is not supported.

Instance attributes (read-only):

time.hour[¶](https://docs.python.org/3/library/datetime.html#datetime.time.hour "Link to this definition")
:   In `range(24)`.

time.minute[¶](https://docs.python.org/3/library/datetime.html#datetime.time.minute "Link to this definition")
:   In `range(60)`.

time.second[¶](https://docs.python.org/3/library/datetime.html#datetime.time.second "Link to this definition")
:   In `range(60)`.

time.microsecond[¶](https://docs.python.org/3/library/datetime.html#datetime.time.microsecond "Link to this definition")
:   In `range(1000000)`.

time.tzinfo[¶](https://docs.python.org/3/library/datetime.html#datetime.time.tzinfo "Link to this definition")
:   The object passed as the tzinfo argument to the [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") constructor, or
    `None` if none was passed.

time.fold[¶](https://docs.python.org/3/library/datetime.html#datetime.time.fold "Link to this definition")
:   In `[0, 1]`. Used to disambiguate wall times during a repeated interval. (A
    repeated interval occurs when clocks are rolled back at the end of daylight saving
    time or when the UTC offset for the current zone is decreased for political reasons.)
    The values 0 and 1 represent, respectively, the earlier and later of the two
    moments with the same wall time representation.

    Added in version 3.6.

[`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects support equality and order comparisons,
where `a` is considered less than `b` when `a` precedes `b` in time.

Naive and aware `time` objects are never equal.
Order comparison between naive and aware `time` objects raises
[`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

If both comparands are aware, and have the same [`tzinfo`](https://docs.python.org/3/library/