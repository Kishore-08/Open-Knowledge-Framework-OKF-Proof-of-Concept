---
id: python-timedelta-objects-https-docs-python-org-3-library-datetime-h-30088197
type: concept
title: '`timedelta` objects[¶](https://docs.python.org/3/library/datetime.html#timedelta-objects
  "Link to this heading")'
description: A [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta
  "datetime.timedelta") object represents a duration, the difference between two
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## `timedelta` objects[¶](https://docs.python.org/3/library/datetime.html#timedelta-objects "Link to this heading")

A [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object represents a duration, the difference between two
[`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") or [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") instances.

*class* datetime.timedelta(*days=0*, *seconds=0*, *microseconds=0*, *milliseconds=0*, *minutes=0*, *hours=0*, *weeks=0*)[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta "Link to this definition")
:   All arguments are optional and default to 0. Arguments may be integers
    or floats, and may be positive or negative.

    Only *days*, *seconds* and *microseconds* are stored internally.
    Arguments are converted to those units:

    - A millisecond is converted to 1000 microseconds.
    - A minute is converted to 60 seconds.
    - An hour is converted to 3600 seconds.
    - A week is converted to 7 days.

    and days, seconds and microseconds are then normalized so that the
    representation is unique, with

    - `0 <= microseconds < 1000000`
    - `0 <= seconds < 3600*24` (the number of seconds in one day)
    - `-999999999 <= days <= 999999999`

    The following example illustrates how any arguments besides
    *days*, *seconds* and *microseconds* are “merged” and normalized into those
    three resulting attributes:

    ```
    >>> import datetime as dt
    >>> delta = dt.timedelta(
    ...     days=50,
    ...     seconds=27,
    ...     microseconds=10,
    ...     milliseconds=29000,
    ...     minutes=5,
    ...     hours=8,
    ...     weeks=2
    ... )
    >>> # Only days, seconds, and microseconds remain
    >>> delta
    datetime.timedelta(days=64, seconds=29156, microseconds=10)
    ```

    Tip

    `import datetime as dt` instead of `import datetime` or
    `from datetime import datetime` to avoid confusion between the module
    and the class. See [How I Import Python’s datetime Module](https://adamj.eu/tech/2019/09/12/how-i-import-pythons-datetime-module/).

    If any argument is a float and there are fractional microseconds,
    the fractional microseconds left over from all arguments are
    combined and their sum is rounded to the nearest microsecond using
    round-half-to-even tiebreaker. If no argument is a float, the
    conversion and normalization processes are exact (no information is
    lost).

    If the normalized value of days lies outside the indicated range,
    [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") is raised.

    Note that normalization of negative values may be surprising at first. For
    example:

    ```
    >>> import datetime as dt
    >>> d = dt.timedelta(microseconds=-1)
    >>> (d.days, d.seconds, d.microseconds)
    (-1, 86399, 999999)
    ```

    Since the string representation of `timedelta` objects can be confusing,
    use the following recipe to produce a more readable format:

    ```
    >>> def pretty_timedelta(td):
    ...     if td.days >= 0:
    ...         return str(td)
    ...     return f'-({-td!s})'
    ...
    >>> d = timedelta(hours=-1)
    >>> str(d)  # not human-friendly
    '-1 day, 23:00:00'
    >>> pretty_timedelta(d)
    '-(1:00:00)'
    ```

Class attributes:

timedelta.min[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.min "Link to this definition")
:   The most negative [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object, `timedelta(-999999999)`.

timedelta.max[¶](https://docs.python.org/3/library/datetime.html#datetime.timedelta.max "Link to this definition")
:   The most positive [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta") object, `timedelta(days=9999999