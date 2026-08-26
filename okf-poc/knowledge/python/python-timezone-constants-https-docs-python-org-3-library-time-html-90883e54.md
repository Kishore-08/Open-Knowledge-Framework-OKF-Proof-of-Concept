---
id: python-timezone-constants-https-docs-python-org-3-library-time-html-90883e54
type: concept
title: Timezone Constants[¶](https://docs.python.org/3/library/time.html#timezone-constants
  "Link to this heading")
description: time.altzone[¶](https://docs.python.org/3/library/time.html#time.altzone
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/time.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Timezone Constants[¶](https://docs.python.org/3/library/time.html#timezone-constants "Link to this heading")

time.altzone[¶](https://docs.python.org/3/library/time.html#time.altzone "Link to this definition")
:   The offset of the local DST timezone, in seconds west of UTC, if one is defined.
    This is negative if the local DST timezone is east of UTC (as in Western Europe,
    including the UK). Only use this if `daylight` is nonzero. See note below.

time.daylight[¶](https://docs.python.org/3/library/time.html#time.daylight "Link to this definition")
:   Nonzero if a DST timezone is defined. See note below.

time.timezone[¶](https://docs.python.org/3/library/time.html#time.timezone "Link to this definition")
:   The offset of the local (non-DST) timezone, in seconds west of UTC (negative in
    most of Western Europe, positive in the US, zero in the UK). See note below.

time.tzname[¶](https://docs.python.org/3/library/time.html#time.tzname "Link to this definition")
:   A tuple of two strings: the first is the name of the local non-DST timezone, the
    second is the name of the local DST timezone. If no DST timezone is defined,
    the second string should not be used. See note below.

Note

For the above Timezone constants ([`altzone`](https://docs.python.org/3/library/time.html#time.altzone "time.altzone"), [`daylight`](https://docs.python.org/3/library/time.html#time.daylight "time.daylight"), [`timezone`](https://docs.python.org/3/library/time.html#time.timezone "time.timezone"),
and [`tzname`](https://docs.python.org/3/library/time.html#time.tzname "time.tzname")), the value is determined by the timezone rules in effect
at module load time or the last time [`tzset()`](https://docs.python.org/3/library/time.html#time.tzset "time.tzset") is called and may be incorrect
for times in the past. It is recommended to use the [`tm_gmtoff`](https://docs.python.org/3/library/time.html#time.struct_time.tm_gmtoff "time.struct_time.tm_gmtoff") and
[`tm_zone`](https://docs.python.org/3/library/time.html#time.struct_time.tm_zone "time.struct_time.tm_zone") results from [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime") to obtain timezone information.

See also

Module [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.")
:   More object-oriented interface to dates and times.

Module [`locale`](https://docs.python.org/3/library/locale.html#module-locale "locale: Internationalization services.")
:   Internationalization services. The locale setting affects the interpretation
    of many format specifiers in [`strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime") and [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime").

Module [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")
:   General calendar-related functions. [`timegm()`](https://docs.python.org/3/library/calendar.html#calendar.timegm "calendar.timegm") is the
    inverse of [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime") from this module.

Footnotes