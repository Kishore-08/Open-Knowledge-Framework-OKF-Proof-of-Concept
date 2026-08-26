---
id: python-strftime-and-strptime-format-codes-https-docs-python-org-3-l-30088197
type: concept
title: '`strftime()` and `strptime()` format codes[¶](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
  "Link to this heading")'
description: 'These methods accept format codes that can be used to parse and format
  dates:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### `strftime()` and `strptime()` format codes[¶](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes "Link to this heading")

These methods accept format codes that can be used to parse and format dates:

```
>>> import datetime as dt
>>> dt.datetime.strptime('31/01/22 23:59:59.999999',
...                      '%d/%m/%y %H:%M:%S.%f')
datetime.datetime(2022, 1, 31, 23, 59, 59, 999999)
>>> _.strftime('%a %d %b %Y, %I:%M%p')
'Mon 31 Jan 2022, 11:59PM'
```

The following is a list of all the format codes that the 1989 C standard
requires, and these work on all platforms with a standard C implementation.

| Directive | Meaning | Example | Notes |
| --- | --- | --- | --- |
| `%a` | Weekday as locale’s abbreviated name. | Sun, Mon, …, Sat (en\_US);  So, Mo, …, Sa (de\_DE) | (1) |
| `%A` | Weekday as locale’s full name. | Sunday, Monday, …, Saturday (en\_US);  Sonntag, Montag, …, Samstag (de\_DE) | (1) |
| `%w` | Weekday as a decimal number, where 0 is Sunday and 6 is Saturday. | 0, 1, …, 6 |  |
| `%d` | Day of the month as a zero-padded decimal number. | 01, 02, …, 31 | (9) |
| `%b` | Month as locale’s abbreviated name. | Jan, Feb, …, Dec (en\_US);  Jan, Feb, …, Dez (de\_DE) | (1) |
| `%B` | Month as locale’s full name. | January, February, …, December (en\_US);  Januar, Februar, …, Dezember (de\_DE) | (1) |
| `%m` | Month as a zero-padded decimal number. | 01, 02, …, 12 | (9) |
| `%y` | Year without century as a zero-padded decimal number. | 00, 01, …, 99 | (9) |
| `%Y` | Year with century as a decimal number. | 0001, 0002, …, 2013, 2014, …, 9998, 9999 | (2) |
| `%H` | Hour (24-hour clock) as a zero-padded decimal number. | 00, 01, …, 23 | (9) |
| `%I` | Hour (12-hour clock) as a zero-padded decimal number. | 01, 02, …, 12 | (9) |
| `%p` | Locale’s equivalent of either AM or PM. | AM, PM (en\_US);  am, pm (de\_DE) | (1), (3) |
| `%M` | Minute as a zero-padded decimal number. | 00, 01, …, 59 | (9) |
| `%S` | Second as a zero-padded decimal number. | 00, 01, …, 59 | (4), (9) |
| `%f` | Microsecond as a decimal number, zero-padded to 6 digits. | 000000, 000001, …, 999999 | (5) |
| `%z` | UTC offset in the form `±HHMM[SS[.ffffff]]` (empty string if the object is naive). | (empty), +0000, -0400, +1030, +063415, -030712.345216 | (6) |
| `%Z` | Time zone name (empty string if the object is naive). | (empty), UTC, GMT | (6) |
| `%j` | Day of the year as a zero-padded decimal number. | 001, 002, …, 366 | (9) |
| `%U` | Week number of the year (Sunday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0. | 00, 01, …, 53 | (7), (9) |
| `%W` | Week number of the year (Monday as the first day of the week) as a zero-padded decimal number. All days in a new year preceding the first Monday are considered to be in week 0. | 00, 01, …, 53 | (7), (9) |
| `%c` | Locale’s appropriate date and time representation. | Tue Aug 16 21:30:00 1988 (en\_US);  Di 16 Aug 21:30:00 1988 (de\_DE) | (1) |
| `%x` | Locale’s appropriate date representation. | 08/16/88 (None);  08/16/1988 (en\_US);  16.08.1988 (de\_DE) | (1) |
| `%X` | Locale’s appropriate time representation. | 21:30:00 (en\_US);  21:30:00 (de\_DE) | (1) |
| `%%` | A literal `'%'` character. | % |  |

Several additional directives not required by the C89 standard are included for
convenience. These parameters all correspond to ISO 8601 date values.

| Directive | Meaning | Example | Notes |
| --- | --- | --- | --- |
| `%G` | ISO 8601 year with century representing the year that contains the greater part of the ISO week (`%V`). | 0001, 0002, …, 2013, 2014, …, 9998, 9999 | (8) |
| `%u` | ISO 8601 weekday as a decimal number where 1 is Monday. | 1, 2, …, 7 |  |
| `%V` | ISO 8601 week as a decimal number with Monday as the first day of the week. Week 01 is the week containing Jan 4. | 01, 02, …, 53 | (8), (9) |
| `%:z` | UTC offset in the form `±HH:MM[:SS[.ffffff]]` (empty string if th