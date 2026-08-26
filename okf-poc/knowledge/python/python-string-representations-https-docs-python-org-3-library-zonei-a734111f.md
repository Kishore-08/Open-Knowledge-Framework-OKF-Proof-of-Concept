---
id: python-string-representations-https-docs-python-org-3-library-zonei-a734111f
type: concept
title: String representations[¶](https://docs.python.org/3/library/zoneinfo.html#string-representations
  "Link to this heading")
description: The string representation returned when calling [`str`](https://docs.python.org/3/library/stdtypes.html#str
  "str") on a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/zoneinfo.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### String representations[¶](https://docs.python.org/3/library/zoneinfo.html#string-representations "Link to this heading")

The string representation returned when calling [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") on a
[`ZoneInfo`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo "zoneinfo.ZoneInfo") object defaults to using the [`ZoneInfo.key`](https://docs.python.org/3/library/zoneinfo.html#zoneinfo.ZoneInfo.key "zoneinfo.ZoneInfo.key") attribute (see
the note on usage in the attribute documentation):

```
>>> zone = ZoneInfo("Pacific/Kwajalein")
>>> str(zone)
'Pacific/Kwajalein'

>>> when = dt.datetime(2020, 4, 1, 3, 15, tzinfo=zone)
>>> f"{when.isoformat()} [{when.tzinfo}]"
'2020-04-01T03:15:00+12:00 [Pacific/Kwajalein]'
```

For objects constructed from a file without specifying a `key` parameter,
`str` falls back to calling [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr"). `ZoneInfo`’s `repr` is
implementation-defined and not necessarily stable between versions, but it is
guaranteed not to be a valid `ZoneInfo` key.