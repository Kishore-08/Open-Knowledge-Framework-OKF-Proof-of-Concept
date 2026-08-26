---
id: python-default-adapters-and-converters-deprecated-https-docs-python-d14c7d1a
type: concept
title: Default adapters and converters (deprecated)[¶](https://docs.python.org/3/library/sqlite3.html#default-adapters-and-converters-deprecated
  "Link to this heading")
description: Note
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Default adapters and converters (deprecated)[¶](https://docs.python.org/3/library/sqlite3.html#default-adapters-and-converters-deprecated "Link to this heading")

Note

The default adapters and converters are deprecated as of Python 3.12.
Instead, use the [Adapter and converter recipes](https://docs.python.org/3/library/sqlite3.html#sqlite3-adapter-converter-recipes)
and tailor them to your needs.

The deprecated default adapters and converters consist of:

- An adapter for [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects to [`strings`](https://docs.python.org/3/library/stdtypes.html#str "str") in
  [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
- An adapter for [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects to strings in
  ISO 8601 format.
- A converter for [declared](https://docs.python.org/3/library/sqlite3.html#sqlite3-converters) “date” types to
  [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "datetime.date") objects.
- A converter for declared “timestamp” types to
  [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") objects.
  Fractional parts will be truncated to 6 digits (microsecond precision).

Note

The default “timestamp” converter ignores UTC offsets in the database and
always returns a naive [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "datetime.datetime") object. To preserve UTC
offsets in timestamps, either leave converters disabled, or register an
offset-aware converter with [`register_converter()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_converter "sqlite3.register_converter").

Deprecated since version 3.12.