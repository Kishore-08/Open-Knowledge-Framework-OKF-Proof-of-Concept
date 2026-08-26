---
id: python-data-types-https-docs-python-org-3-library-datatypes-html-da-ba259cd5
type: concept
title: 'Data Types[¶](https://docs.python.org/3/library/datatypes.html#data-types
  "Link '
description: The modules described in this chapter provide a variety of specialized
  data
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datatypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# Data Types[¶](https://docs.python.org/3/library/datatypes.html#data-types "Link to this heading")

The modules described in this chapter provide a variety of specialized data
types such as dates and times, fixed-type arrays, heap queues, double-ended
queues, and enumerations.

Python also provides some built-in data types, in particular,
[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") and [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"), and
[`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"). The [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") class is used to hold
Unicode strings, and the [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") and [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") classes are used
to hold binary data.

The following modules are documented in this chapter:

- [`datetime` — Basic date and time types](https://docs.python.org/3/library/datetime.html)
  - [Aware and naive objects](https://docs.python.org/3/library/datetime.html#aware-and-naive-objects)
  - [Constants](https://docs.python.org/3/library/datetime.html#constants)
  - [Available types](https://docs.python.org/3/library/datetime.html#available-types)
    - [Common properties](https://docs.python.org/3/library/datetime.html#common-properties)
    - [Determining if an object is aware or naive](https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive)
  - [`timedelta` objects](https://docs.python.org/3/library/datetime.html#timedelta-objects)
    - [Examples of usage: `timedelta`](https://docs.python.org/3/library/datetime.html#examples-of-usage-timedelta)
  - [`date` objects](https://docs.python.org/3/library/datetime.html#date-objects)
    - [Examples of usage: `date`](https://docs.python.org/3/library/datetime.html#examples-of-usage-date)
  - [`datetime` objects](https://docs.python.org/3/library/datetime.html#datetime-objects)
    - [Examples of usage: `datetime`](https://docs.python.org/3/library/datetime.html#examples-of-usage-datetime)
  - [`time` objects](https://docs.python.org/3/library/datetime.html#time-objects)
    - [Examples of usage: `time`](https://docs.python.org/3/library/datetime.html#examples-of-usage-time)
  - [`tzinfo` objects](https://docs.python.org/3/library/datetime.html#tzinfo-objects)
  - [`timezone` objects](https://docs.python.org/3/library/datetime.html#timezone-objects)
  - [`strftime()` and `strptime()` behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
    - [`strftime()` and `strptime()` format codes](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)
    - [Technical detail](https://docs.python.org/3/library/datetime.html#technical-detail)
- [`zoneinfo` — IANA time zone support](https://docs.python.org/3/library/zoneinfo.html)
  - [Using `ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#using-zoneinfo)
  - [Data sources](https://docs.python.org/3/library/zoneinfo.html#data-sources)
    - [Configuring the data sources](https://docs.python.org/3/library/zoneinfo.html#configuring-the-data-sources)
      - [Compile-time configuration](https://docs.python.org/3/library/zoneinfo.html#compile-time-configuration)
      - [Environment configuration](https://docs.python.org/3/library/zoneinfo.html#environment-configuration)
      - [Runtime configuration](https://docs.python.org/3/library/zoneinfo.html#runtime-configuration)
  - [The `ZoneInfo` class](https://docs.python.org/3/library/zoneinfo.html#the-zoneinfo-class)
    - [String representations](https://docs.python.org/3/library/zoneinfo.html#string-representations)
    - [Pickle serialization](https://docs.python.org/3/library/zoneinfo.html#pickle-serializatio