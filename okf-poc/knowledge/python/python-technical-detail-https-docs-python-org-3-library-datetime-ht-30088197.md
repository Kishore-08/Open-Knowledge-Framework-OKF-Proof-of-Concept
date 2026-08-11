---
id: python-technical-detail-https-docs-python-org-3-library-datetime-ht-30088197
type: concept
title: Technical detail[¶](https://docs.python.org/3/library/datetime.html#technical-detail
  "Link to this heading")
description: 'Broadly speaking, `d.strftime(fmt)` acts like the [`time`](https://docs.python.org/3/library/time.html#module-time
  "time: Time access and conversions.") module’s'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Technical detail[¶](https://docs.python.org/3/library/datetime.html#technical-detail "Link to this heading")

Broadly speaking, `d.strftime(fmt)` acts like the [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") module’s
`time.strftime(fmt, d.timetuple())` although not all objects support a
[`timetuple()`](https://docs.python.org/3/library/datetime.html#datetime.date.timetuple "datetime.date.timetuple") method.

For the [`datetime.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") and [`date.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strptime "datetime.date.strptime") class methods,
the default value is `1900-01-01T00:00:00.000`: any components not specified
in the format string will be pulled from the default value.

Note

Format strings without separators can be ambiguous for parsing. For
example, with `%Y%m%d`, the string `2026111` may be parsed either as
`2026-11-01` or as `2026-01-11`.
Use separators to ensure the input is parsed as intended.

Note

When used to parse partial dates lacking a year, [`datetime.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime")
and [`date.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strptime "datetime.date.strptime") will raise when encountering February 29 because
the default year of 1900 is *not* a leap year. Always add a default leap
year to partial date strings before parsing.

```
>>> import datetime as dt
>>> value = "2/29"
>>> dt.datetime.strptime(value, "%m/%d")
Traceback (most recent call last):
...
ValueError: day 29 must be in range 1..28 for month 2 in year 1900
>>> dt.datetime.strptime(f"1904 {value}", "%Y %m/%d")
datetime.datetime(1904, 2, 29, 0, 0)
```

Using `datetime.strptime(date_string, format)` is equivalent to:

```
datetime(*(time.strptime(date_string, format)[0:6]))
```

except when the format includes sub-second components or time zone offset
information, which are supported in `datetime.strptime` but are discarded by
`time.strptime`.

For [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects, the format codes for year, month, and day should not
be used, as `time` objects have no such values. If they’re used anyway,
1900 is substituted for the year, and 1 for the month and day.

For [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects, the format codes for hours, minutes, seconds, and
microseconds should not be used, as `date` objects have no such
values. If they’re used anyway, 0 is substituted for them.

For the same reason, handling of format strings containing Unicode code points
that can’t be represented in the charset of the current locale is also
platform-dependent. On some platforms such code points are preserved intact in
the output, while on others `strftime` may raise [`UnicodeError`](https://docs.python.org/3/library/exceptions.html#UnicodeError "UnicodeError") or return
an empty string instead.

Notes:

1. Because the format depends on the current locale, care should be taken when
   making assumptions about the output value. Field orderings will vary (for
   example, “month/day/year” versus “day/month/year”), and the output may
   contain non-ASCII characters.
2. The [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") method can parse years in the full [1, 9999] range, but
   years < 1000 must be zero-filled to 4-digit width.

   Changed in version 3.2: In previous versions, [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime") method was restricted to
   years >= 1900.

   Changed in version 3.3: In version 3.2, [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.