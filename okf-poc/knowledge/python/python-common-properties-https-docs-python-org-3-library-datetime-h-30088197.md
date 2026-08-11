---
id: python-common-properties-https-docs-python-org-3-library-datetime-h-30088197
type: concept
title: Common properties[¶](https://docs.python.org/3/library/datetime.html#common-properties
  "Link to this heading")
description: The [`date`](https://docs.python.org/3/library/datetime.html#datetime.date
  "datetime.date"), [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime
  "datetime.datetime"), [`time
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/datetime.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Common properties[¶](https://docs.python.org/3/library/datetime.html#common-properties "Link to this heading")

The [`date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date"), [`datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime"), [`time`](https://docs.python.org/3/library/datetime.html#datetime.time "datetime.time"), and [`timezone`](https://docs.python.org/3/library/datetime.html#datetime.timezone "datetime.timezone") types
share these common features:

- Objects of these types are immutable.
- Objects of these types are [hashable](https://docs.python.org/3/glossary.html#term-hashable), meaning that they can be used as
  dictionary keys.
- Objects of these types support efficient pickling via the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module.