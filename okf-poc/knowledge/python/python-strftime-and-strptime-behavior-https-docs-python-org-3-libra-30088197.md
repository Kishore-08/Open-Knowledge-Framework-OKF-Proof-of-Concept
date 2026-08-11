---
id: python-strftime-and-strptime-behavior-https-docs-python-org-3-libra-30088197
type: concept
title: '`strftime()` and `strptime()` behavior[¶](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
  "Link to this heading")'
description: '[`date`](https://docs.python.org/3/library/datetime.html#datetime.date
  "datetime.date"), [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime
  "datetime.datetime"), and [`time'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## `strftime()` and `strptime()` behavior[¶](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior "Link to this heading")

[`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date"), [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"), and [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") objects all support a
`strftime(format)` method, to create a string representing the time under the
control of an explicit format string.

Conversely, the [`date.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.date.strptime "datetime.date.strptime"), [`datetime.strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime") and
[`time.strptime()`](https://docs.python.org/3/library/time.html#time.strptime "time.strptime") class methods create an object from a string
representing the time and a corresponding format string.

The table below provides a high-level comparison of [`strftime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime "datetime.datetime.strftime")
versus [`strptime()`](https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime "datetime.datetime.strptime"):

|  | `strftime` | `strptime` |
| --- | --- | --- |
| Usage | Convert object to a string according to a given format | Parse a string into an object given a corresponding format |
| Type of method | Instance method | Class method |
| Signature | `strftime(format)` | `strptime(date_string, format)` |