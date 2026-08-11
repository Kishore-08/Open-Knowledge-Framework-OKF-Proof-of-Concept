---
id: python-datetime-basic-date-and-time-types-https-docs-python-org-3-l-30088197
type: concept
title: '`datetime` — Basic date and time types[¶](https://docs.python.org/3/library/date'
description: '**Source code:** [Lib/datetime.py](https://github.com/python/cpython/tree/3.14/Lib/datetime.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `datetime` — Basic date and time types[¶](https://docs.python.org/3/library/datetime.html#module-datetime "Link to this heading")

**Source code:** [Lib/datetime.py](https://github.com/python/cpython/tree/3.14/Lib/datetime.py)

---

The `datetime` module supplies classes for manipulating dates and times.

While date and time arithmetic is supported, the focus of the implementation is
on efficient attribute extraction for output formatting and manipulation.

Tip

Skip to [the format codes](https://docs.python.org/3/library/datetime.html#format-codes).

See also

Module [`calendar`](https://docs.python.org/3/library/calendar.html#module-calendar "calendar: Functions for working with calendars, including some emulation of the Unix cal program.")
:   General calendar related functions.

Module [`time`](https://docs.python.org/3/library/time.html#module-time "time: Time access and conversions.")
:   Time access and conversions.

Module [`zoneinfo`](https://docs.python.org/3/library/zoneinfo.html#module-zoneinfo "zoneinfo: IANA time zone support")
:   Concrete time zones representing the IANA time zone database.

Package [dateutil](https://dateutil.readthedocs.io/en/stable/)
:   Third-party library with expanded time zone and parsing support.

Package [DateType](https://pypi.org/project/DateType/)
:   Third-party library that introduces distinct static types to for example,
    allow [static type checkers](https://docs.python.org/3/glossary.html#term-static-type-checker)
    to differentiate between naive and aware datetimes.