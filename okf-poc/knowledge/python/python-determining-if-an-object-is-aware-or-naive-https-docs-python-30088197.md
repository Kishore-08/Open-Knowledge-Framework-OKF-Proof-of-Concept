---
id: python-determining-if-an-object-is-aware-or-naive-https-docs-python-30088197
type: concept
title: Determining if an object is aware or naive[¶](https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive
  "Link to this heading")
description: Objects of the [`date`](https://docs.python.org/3/library/datetime.html#datetime.date
  "datetime.date") type are always naive.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Determining if an object is aware or naive[¶](https://docs.python.org/3/library/datetime.html#determining-if-an-object-is-aware-or-naive "Link to this heading")

Objects of the [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") type are always naive.

An object of type [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") or [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") may be aware or naive.

A [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object `d` is aware if both of the following hold:

1. `d.tzinfo` is not `None`
2. `d.tzinfo.utcoffset(d)` does not return `None`

Otherwise, `d` is naive.

A [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time") object `t` is aware if both of the following hold:

1. `t.tzinfo` is not `None`
2. `t.tzinfo.utcoffset(None)` does not return `None`.

Otherwise, `t` is naive.

The distinction between aware and naive doesn’t apply to [`timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "datetime.timedelta")
objects.