---
id: python-date-objects-https-docs-python-org-3-library-datetime-html-d-30088197
type: concept
title: '`date` objects[¶](https://docs.python.org/3/library/datetime.html#date-objects
  "Link to this heading")'
description: A [`date`](https://docs.python.org/3/library/datetime.html#datetime.date
  "datetime.date") object represents a date (year, month and day) in an idealized
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## `date` objects[¶](https://docs.python.org/3/library/datetime.html#date-objects "Link to this heading")

A [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object represents a date (year, month and day) in an idealized
calendar, the current Gregorian calendar indefinitely extended in both
directions.

January 1 of year 1 is called day number 1, January 2 of year 1 is
called day number 2, and so on. [[2]](https://docs.python.org/3/library/datetime.html#id5)

*class* datetime.date(*year*, *month*, *day*)[¶](https://docs.python.org/3/library/datetime.html#datetime.date "Link to this definition")
:   All arguments are required. Arguments must be integers, in the following
    ranges:

    - `MINYEAR <= year <= MAXYEAR`
    - `1 <= month <= 12`
    - `1 <= day <= number of days in the given month and year`

    If an argument outside those ranges is given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

Other constructors, all class methods:

*classmethod* date.today()[¶](https://docs.python.org/3/library/datetime.html#datetime.date.today "Link to this definition")
:   Return the current local date.

    This is equivalent to `date.fromtimestamp(time.time())`.

*classmethod* date.fromtimestamp(*timestamp*)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.fromtimestamp "Link to this definition")
:   Return the local date corresponding to the POSIX *timestamp*, such as is
    returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time").

    This may raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError"), if the timestamp is out
    of the range of values supported by the platform C `localtime()`
    function, and [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") on `localtime()` failure.
    It’s common for this to be restricted to years from 1970 through 2038. Note
    that on non-POSIX systems that include leap seconds in their notion of a
    timestamp, leap seconds are ignored by `fromtimestamp()`.

    Changed in version 3.3: Raise [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") instead of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if the timestamp
    is out of the range of values supported by the platform C
    `localtime()` function. Raise [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") instead of
    `ValueError` on `localtime()` failure.

*classmethod* date.fromordinal(*ordinal*)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.fromordinal "Link to this definition")
:   Return the date corresponding to the proleptic Gregorian *ordinal*, where
    January 1 of year 1 has ordinal 1.

    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised unless `1 <= ordinal <=
    date.max.toordinal()`. For any date `d`,
    `date.fromordinal(d.toordinal()) == d`.

*classmethod* date.fromisoformat(*date\_string*)[¶](https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat "Link to this definition")
:   Return a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") corresponding to a *date\_string* given in any valid
    ISO 8601 format, with the following exceptions:

    1. Reduced precision dates are not currently supported (`YYYY-MM`,
       `YYYY`).
    2. Extended date representations are not currently supported
       (`±YYYYYY-MM-DD`).
    3. Ordinal dates are not currently supported (`YYYY-OOO`).

    Examples:

    ```
    >>> import datetime as dt
    >>> dt.date.fromisoformat('2019-12-04')
    datetime.date(2019, 12, 4)
    >>> dt.date.fromisoformat('20191204')
    datetime.date(2019, 12, 4)
    >>> dt.date.fromisoformat('2021-W01-1')
    datetime.date(2021, 1, 4)