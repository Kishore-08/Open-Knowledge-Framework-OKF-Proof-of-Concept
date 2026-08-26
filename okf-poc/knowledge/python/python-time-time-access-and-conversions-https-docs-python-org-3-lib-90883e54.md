---
id: python-time-time-access-and-conversions-https-docs-python-org-3-lib-90883e54
type: concept
title: '`time` — Time access and conversions[¶](https://docs.python.org/3/library/time.h'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/time.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `time` — Time access and conversions[¶](https://docs.python.org/3/library/time.html#module-time "Link to this heading")

---

This module provides various time-related functions. For related
functionality, see also the [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.") and [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.") modules.

Although this module is always available,
not all functions are available on all platforms. Most of the functions
defined in this module call platform C library functions with the same name. It
may sometimes be helpful to consult the platform documentation, because the
semantics of these functions varies among platforms.

An explanation of some terminology and conventions is in order.

- The *epoch* is the point where the time starts, the return value of
  `time.gmtime(0)`. It is January 1, 1970, 00:00:00 (UTC) on all platforms.

- The term *seconds since the epoch* refers to the total number
  of elapsed seconds since the epoch, typically excluding
  [leap seconds](https://en.wikipedia.org/wiki/Leap_second). Leap seconds are excluded from this total on all
  POSIX-compliant platforms.

- The functions in this module may not handle dates and times before the [epoch](https://docs.python.org/3/library/time.html#epoch) or
  far in the future. The cut-off point in the future is determined by the C
  library; for 32-bit systems, it is typically in 2038.

- Function [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime") can parse 2-digit years when given `%y` format
  code. When 2-digit years are parsed, they are converted according to the POSIX
  and ISO C standards: values 69–99 are mapped to 1969–1999, and values 0–68
  are mapped to 2000–2068.

- UTC is [Coordinated Universal Time](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) and superseded [Greenwich Mean Time](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) or
  GMT as the basis of international timekeeping. The acronym UTC is not a
  mistake but conforms to an earlier, language-agnostic naming scheme for time
  standards such as UT0, UT1, and UT2.

- DST is Daylight Saving Time, an adjustment of the timezone by (usually) one
  hour during part of the year. DST rules are magic (determined by local law) and
  can change from year to year. The C library has a table containing the local
  rules (often it is read from a system file for flexibility) and is the only
  source of True Wisdom in this respect.
- The precision of the various real-time functions may be less than suggested by
  the units in which their value or argument is expressed. E.g. on most Unix
  systems, the clock “ticks” only 50 or 100 times a second.
- On the other hand, the precision of [`time()`](https://docs.python.org/3/library/time.html#time.time "time.time") and [`sleep()`](https://docs.python.org/3/library/time.html#time.sleep "time.sleep") is better
  than their Unix equivalents: times are expressed as floating-point numbers,
  `time()` returns the most accurate time available (using Unix
  `gettimeofday()` where available), and `sleep()` will accept a time
  with a nonzero fraction (Unix `select()` is used to implement this, where
  available).
- The time value as returned by [`gmtime()`](https://docs.python.org/3/library/time.html#time.gmtime "time.gmtime"), [`localtime()`](https://docs.python.org/3/library/time.html#time.localtime "time.localtime"), and
  [`strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime"), and accepted by [`asctime()`](https://docs.python.org/3/library/time.html#time.asctime "time.asctime"), [`mktime()`](https://docs.python.org/3/library/time.html#time.mktime "time.mktime") and
  [`strftime()`](https://docs.python.org/3/library/time.html#time.strftime "time.strftime"), is a seq