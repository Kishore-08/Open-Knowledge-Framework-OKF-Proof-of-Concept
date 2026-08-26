---
id: python-datetime-objects-https-docs-python-org-3-library-datetime-ht-30088197
type: concept
title: '`datetime` objects[¶](https://docs.python.org/3/library/datetime.html#datetime-objects
  "Link to this heading")'
description: A [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime
  "datetime.datetime") object is a single object containing all the information
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## `datetime` objects[¶](https://docs.python.org/3/library/datetime.html#datetime-objects "Link to this heading")

A [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object is a single object containing all the information
from a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object and a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object.

Like a [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") object, [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") assumes the current Gregorian
calendar extended in both directions; like a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object,
`datetime` assumes there are exactly 3600\*24 seconds in every day.

Constructor:

*class* datetime.datetime(*year*, *month*, *day*, *hour=0*, *minute=0*, *second=0*, *microsecond=0*, *tzinfo=None*, *\**, *fold=0*)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime "Link to this definition")
:   The *year*, *month* and *day* arguments are required. *tzinfo* may be `None`, or an
    instance of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass. The remaining arguments must be integers
    in the following ranges:

    - `MINYEAR <= year <= MAXYEAR`,
    - `1 <= month <= 12`,
    - `1 <= day <= number of days in the given month and year`,
    - `0 <= hour < 24`,
    - `0 <= minute < 60`,
    - `0 <= second < 60`,
    - `0 <= microsecond < 1000000`,
    - `fold in [0, 1]`.

    If an argument outside those ranges is given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

    Changed in version 3.6: Added the *fold* parameter.

Other constructors, all class methods:

*classmethod* datetime.today()[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.today "Link to this definition")
:   Return the current local date and time, with [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.datetime.tzinfo "datetime.datetime.tzinfo") `None`.

    Equivalent to:

    ```
    datetime.fromtimestamp(time.time())
    ```

    See also [`now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now"), [`fromtimestamp()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromtimestamp "datetime.datetime.fromtimestamp").

    This method is functionally equivalent to [`now()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "datetime.datetime.now"), but without a
    `tz` parameter.

*classmethod* datetime.now(*tz=None*)[¶](https://docs.python.org/3/library/datetime.html#datetime.datetime.now "Link to this definition")
:   Return the current local date and time.

    If optional argument *tz* is `None`
    or not specified, this is like [`today()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.today "datetime.datetime.today"), but, if possible, supplies more
    precision than can be gotten from going through a [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time") timestamp
    (for example, this may be possible on platforms supplying the C
    `gettimeofday()` function).

    If *tz* is not `None`, it must be an instance of a [`tzinfo`](https://docs.python.org/3/library/datetime.html#datetime.tzinfo "datetime.tzinfo") subclass,
    and the current date and time are converted to *tz*’s time zone.

    This function is preferred over [`today()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.today "datetime.datetime.today") and [`utcnow()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow "datetime.datetime.utcnow").

    Note

    Subsequent calls to `datetime.now()` may return the same