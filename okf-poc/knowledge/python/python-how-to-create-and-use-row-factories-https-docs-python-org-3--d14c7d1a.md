---
id: python-how-to-create-and-use-row-factories-https-docs-python-org-3--d14c7d1a
type: concept
title: How to create and use row factories[¶](https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories
  "Link to this heading")
description: By default, `sqlite3` represents each row as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple
  "tuple").
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to create and use row factories[¶](https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories "Link to this heading")

By default, `sqlite3` represents each row as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple").
If a `tuple` does not suit your needs,
you can use the [`sqlite3.Row`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row "sqlite3.Row") class
or a custom [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.row_factory "sqlite3.Cursor.row_factory").

While `row_factory` exists as an attribute both on the
[`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") and the [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection"),
it is recommended to set [`Connection.row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory "sqlite3.Connection.row_factory"),
so all cursors created from the connection will use the same row factory.

`Row` provides indexed and case-insensitive named access to columns,
with minimal memory overhead and performance impact over a `tuple`.
To use `Row` as a row factory,
assign it to the `row_factory` attribute:

```
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = sqlite3.Row
```

Queries now return `Row` objects:

```
>>> res = con.execute("SELECT 'Earth' AS name, 6378 AS radius")
>>> row = res.fetchone()
>>> row.keys()
['name', 'radius']
>>> row[0]         # Access by index.
'Earth'
>>> row["name"]    # Access by name.
'Earth'
>>> row["RADIUS"]  # Column names are case-insensitive.
6378
>>> con.close()
```

Note

The `FROM` clause can be omitted in the `SELECT` statement, as in the
above example. In such cases, SQLite returns a single row with columns
defined by expressions, e.g. literals, with the given aliases
`expr AS alias`.

You can create a custom [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.row_factory "sqlite3.Cursor.row_factory")
that returns each row as a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), with column names mapped to values:

```
def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}
```

Using it, queries now return a `dict` instead of a `tuple`:

```
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = dict_factory
>>> for row in con.execute("SELECT 1 AS a, 2 AS b"):
...     print(row)
{'a': 1, 'b': 2}
>>> con.close()
```

The following row factory returns a [named tuple](https://docs.python.org/3/glossary.html#term-named-tuple):

```
from collections import namedtuple

def namedtuple_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    cls = namedtuple("Row", fields)
    return cls._make(row)
```

`namedtuple_factory()` can be used as follows:

```
>>> con = sqlite3.connect(":memory:")
>>> con.row_factory = namedtuple_factory
>>> cur = con.execute("SELECT 1 AS a, 2 AS b")
>>> row = cur.fetchone()
>>> row
Row(a=1, b=2)
>>> row[0]  # Indexed access.
1
>>> row.b   # Attribute access.
2
>>> con.close()
```

With some adjustments, the above recipe can be adapted to use a
[`dataclass`](https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass "dataclasses.dataclass"), or any other custom class,
instead of a [`namedtuple`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple").