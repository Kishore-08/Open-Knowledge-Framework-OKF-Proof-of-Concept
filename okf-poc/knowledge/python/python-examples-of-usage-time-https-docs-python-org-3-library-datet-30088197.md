---
id: python-examples-of-usage-time-https-docs-python-org-3-library-datet-30088197
type: concept
title: 'Examples of usage: `time`[¶](https://docs.python.org/3/library/datetime.html#examples-of-usage-time
  "Link to this heading")'
description: 'Examples of working with a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time
  "datetime.time") object:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Examples of usage: `time`[¶](https://docs.python.org/3/library/datetime.html#examples-of-usage-time "Link to this heading")

Examples of working with a [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object:

```
>>> import datetime as dt
>>> class TZ1(dt.tzinfo):
...     def utcoffset(self, when):
...         return dt.timedelta(hours=1)
...     def dst(self, when):
...         return dt.timedelta(0)
...     def tzname(self, when):
...         return "+01:00"
...     def  __repr__(self):
...         return f"{self.__class__.__name__}()"
...
>>> t = dt.time(12, 10, 30, tzinfo=TZ1())
>>> t
datetime.time(12, 10, 30, tzinfo=TZ1())
>>> t.isoformat()
'12:10:30+01:00'
>>> t.dst()
datetime.timedelta(0)
>>> t.tzname()
'+01:00'
>>> t.strftime("%H:%M:%S %Z")
'12:10:30 +01:00'
>>> 'The {} is {:%H:%M}.'.format("time", t)
'The time is 12:10.'
```