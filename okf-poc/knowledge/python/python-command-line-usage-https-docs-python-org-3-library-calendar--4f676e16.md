---
id: python-command-line-usage-https-docs-python-org-3-library-calendar--4f676e16
type: concept
title: Command-line usage[¶](https://docs.python.org/3/library/calendar.html#command-line-usage
  "Link to this heading")
description: Added in version 2.5.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/calendar.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Command-line usage[¶](https://docs.python.org/3/library/calendar.html#command-line-usage "Link to this heading")

Added in version 2.5.

The `calendar` module can be executed as a script from the command line
to interactively print a calendar.

```
python -m calendar [-h] [-L LOCALE] [-e ENCODING] [-t {text,html}]
                   [-w WIDTH] [-l LINES] [-s SPACING] [-m MONTHS] [-c CSS]
                   [-f FIRST_WEEKDAY] [year] [month]
```

For example, to print a calendar for the year 2000:

```
$ python -m calendar 2000
                                  2000

      January                   February                   March
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6             1  2  3  4  5
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       6  7  8  9 10 11 12
10 11 12 13 14 15 16      14 15 16 17 18 19 20      13 14 15 16 17 18 19
17 18 19 20 21 22 23      21 22 23 24 25 26 27      20 21 22 23 24 25 26
24 25 26 27 28 29 30      28 29                     27 28 29 30 31
31

       April                      May                       June
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2       1  2  3  4  5  6  7                1  2  3  4
 3  4  5  6  7  8  9       8  9 10 11 12 13 14       5  6  7  8  9 10 11
10 11 12 13 14 15 16      15 16 17 18 19 20 21      12 13 14 15 16 17 18
17 18 19 20 21 22 23      22 23 24 25 26 27 28      19 20 21 22 23 24 25
24 25 26 27 28 29 30      29 30 31                  26 27 28 29 30

        July                     August                  September
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                1  2          1  2  3  4  5  6                   1  2  3
 3  4  5  6  7  8  9       7  8  9 10 11 12 13       4  5  6  7  8  9 10
10 11 12 13 14 15 16      14 15 16 17 18 19 20      11 12 13 14 15 16 17
17 18 19 20 21 22 23      21 22 23 24 25 26 27      18 19 20 21 22 23 24
24 25 26 27 28 29 30      28 29 30 31               25 26 27 28 29 30
31

      October                   November                  December
Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
                   1             1  2  3  4  5                   1  2  3
 2  3  4  5  6  7  8       6  7  8  9 10 11 12       4  5  6  7  8  9 10
 9 10 11 12 13 14 15      13 14 15 16 17 18 19      11 12 13 14 15 16 17
16 17 18 19 20 21 22      20 21 22 23 24 25 26      18 19 20 21 22 23 24
23 24 25 26 27 28 29      27 28 29 30               25 26 27 28 29 30 31
30 31
```

The following options are accepted:

--help, -h[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-help "Link to this definition")
:   Show the help message and exit.

--locale LOCALE, -L LOCALE[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-locale "Link to this definition")
:   The locale to use for month and weekday names.
    Defaults to English.

--encoding ENCODING, -e ENCODING[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-encoding "Link to this definition")
:   The encoding to use for output.
    [`--encoding`](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-encoding) is required if [`--locale`](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-locale) is set.

--type {text,html}, -t {text,html}[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-type "Link to this definition")
:   Print the calendar to the terminal as text,
    or as an HTML document.

--first-weekday FIRST\_WEEKDAY, -f FIRST\_WEEKDAY[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-first-weekday "Link to this definition")
:   The weekday to start each week.
    Must be a number between 0 (Monday) and 6 (Sunday).
    Defaults to 0.

    Added in version 3.13.

year[¶](https://docs.python.org/3/library/calendar.html#cmdoption-calendar-arg-year "Link to this definition")