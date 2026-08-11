---
id: python-calendar-general-calendar-related-functions-https-docs-pytho-4f676e16
type: concept
title: '`calendar` — General calendar-related functions[¶](https://docs.python.org/3/lib'
description: '**Source code:** [Lib/calendar.py](https://github.com/python/cpython/tree/3.14/Lib/calendar.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/calendar.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `calendar` — General calendar-related functions[¶](https://docs.python.org/3/library/calendar.html#module-calendar "Link to this heading")

**Source code:** [Lib/calendar.py](https://github.com/python/cpython/tree/3.14/Lib/calendar.py)

---

This module allows you to output calendars like the Unix **cal** program,
and provides additional useful functions related to the calendar. By default,
these calendars have Monday as the first day of the week, and Sunday as the last
(the European convention). Use [`setfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.setfirstweekday "calendar.setfirstweekday") to set the first day of
the week to Sunday (6) or to any other weekday. Parameters that specify dates
are given as integers. For related
functionality, see also the [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime "datetime: Basic date and time types.") and [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.") modules.

The functions and classes defined in this module
use an idealized calendar, the current Gregorian calendar extended indefinitely
in both directions. This matches the definition of the “proleptic Gregorian”
calendar in Dershowitz and Reingold’s book “Calendrical Calculations”, where
it’s the base calendar for all computations. Zero and negative years are
interpreted as prescribed by the ISO 8601 standard. Year 0 is 1 BC, year -1 is
2 BC, and so on.

*class* calendar.Calendar(*firstweekday=0*)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar "Link to this definition")
:   Creates a `Calendar` object. *firstweekday* is an integer specifying the
    first day of the week. [`MONDAY`](https://docs.python.org/3/library/calendar.html#calendar.MONDAY "calendar.MONDAY") is `0` (the default), [`SUNDAY`](https://docs.python.org/3/library/calendar.html#calendar.SUNDAY "calendar.SUNDAY") is `6`.

    A `Calendar` object provides several methods that can be used for
    preparing the calendar data for formatting. This class doesn’t do any formatting
    itself. This is the job of subclasses.

    `Calendar` instances have the following methods and attributes:

    firstweekday[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.firstweekday "Link to this definition")
    :   The first weekday as an integer (0–6).

        This property can also be set and read using
        [`setfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.setfirstweekday "calendar.Calendar.setfirstweekday") and
        [`getfirstweekday()`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.getfirstweekday "calendar.Calendar.getfirstweekday") respectively.

    getfirstweekday()[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.getfirstweekday "Link to this definition")
    :   Return an [`int`](https://docs.python.org/3/library/functions.html#int "int") for the current first weekday (0–6).

        Identical to reading the [`firstweekday`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.firstweekday "calendar.Calendar.firstweekday") property.

    setfirstweekday(*firstweekday*)[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.setfirstweekday "Link to this definition")
    :   Set the first weekday to *firstweekday*, passed as an [`int`](https://docs.python.org/3/library/functions.html#int "int") (0–6).

        Identical to setting the [`firstweekday`](https://docs.python.org/3/library/calendar.html#calendar.Calendar.firstweekday "calendar.Calendar.firstweekday") property.

    iterweekdays()[¶](https://docs.python.org/3/library/calendar.html#calendar.Calendar.iterweekdays "Link to this definition")
    :   Return an iterator for the weekday numbers that will be used for one
        week. The first value from the iterator will be the same as the value of
        the [`firstweekday`](https://docs.python.org/3/library/c