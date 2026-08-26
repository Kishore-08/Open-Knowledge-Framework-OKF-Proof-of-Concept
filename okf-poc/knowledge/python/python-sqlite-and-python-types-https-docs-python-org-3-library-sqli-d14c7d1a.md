---
id: python-sqlite-and-python-types-https-docs-python-org-3-library-sqli-d14c7d1a
type: concept
title: SQLite and Python types[¶](https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types
  "Link to this heading")
description: 'SQLite natively supports the following types: `NULL`, `INTEGER`,'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### SQLite and Python types[¶](https://docs.python.org/3/library/sqlite3.html#sqlite-and-python-types "Link to this heading")

SQLite natively supports the following types: `NULL`, `INTEGER`,
`REAL`, `TEXT`, `BLOB`.

The following Python types can thus be sent to SQLite without any problem:

| Python type | SQLite type |
| --- | --- |
| `None` | `NULL` |
| [`int`](https://docs.python.org/3/library/functions.html#int "int") | `INTEGER` |
| [`float`](https://docs.python.org/3/library/functions.html#float "float") | `REAL` |
| [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") | `TEXT` |
| [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") | `BLOB` |

This is how SQLite types are converted to Python types by default:

| SQLite type | Python type |
| --- | --- |
| `NULL` | `None` |
| `INTEGER` | [`int`](https://docs.python.org/3/library/functions.html#int "int") |
| `REAL` | [`float`](https://docs.python.org/3/library/functions.html#float "float") |
| `TEXT` | depends on [`text_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.text_factory "sqlite3.Connection.text_factory"), [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") by default |
| `BLOB` | [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") |

The type system of the `sqlite3` module is extensible in two ways: you can
store additional Python types in an SQLite database via
[object adapters](https://docs.python.org/3/library/sqlite3.html#sqlite3-adapters),
and you can let the `sqlite3` module convert SQLite types to
Python types via [converters](https://docs.python.org/3/library/sqlite3.html#sqlite3-converters).