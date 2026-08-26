---
id: python-how-to-convert-sqlite-values-to-custom-python-types-https-do-d14c7d1a
type: concept
title: How to convert SQLite values to custom Python types[¶](https://docs.python.org/3/library/sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types
  "Link to this heading")
description: Writing an adapter lets you convert *from* custom Python types *to* SQLite
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to convert SQLite values to custom Python types[¶](https://docs.python.org/3/library/sqlite3.html#how-to-convert-sqlite-values-to-custom-python-types "Link to this heading")

Writing an adapter lets you convert *from* custom Python types *to* SQLite
values.
To be able to convert *from* SQLite values *to* custom Python types,
we use *converters*.

Let’s go back to the `Point` class. We stored the x and y coordinates
separated via semicolons as strings in SQLite.

First, we’ll define a converter function that accepts the string as a parameter
and constructs a `Point` object from it.

Note

Converter functions are **always** passed a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object,
no matter the underlying SQLite data type.

```
def convert_point(s):
    x, y = map(float, s.split(b";"))
    return Point(x, y)
```

We now need to tell `sqlite3` when it should convert a given SQLite value.
This is done when connecting to a database, using the *detect\_types* parameter
of [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect"). There are three options:

- Implicit: set *detect\_types* to [`PARSE_DECLTYPES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES "sqlite3.PARSE_DECLTYPES")
- Explicit: set *detect\_types* to [`PARSE_COLNAMES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES "sqlite3.PARSE_COLNAMES")
- Both: set *detect\_types* to
  `sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES`.
  Column names take precedence over declared types.

The following example illustrates the implicit and explicit approaches:

```
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

def adapt_point(point):
    return f"{point.x};{point.y}"

def convert_point(s):
    x, y = list(map(float, s.split(b";")))
    return Point(x, y)

# Register the adapter and converter
sqlite3.register_adapter(Point, adapt_point)
sqlite3.register_converter("point", convert_point)

# 1) Parse using declared types
p = Point(4.0, -3.2)
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
cur = con.execute("CREATE TABLE test(p point)")

cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute("SELECT p FROM test")
print("with declared types:", cur.fetchone()[0])
cur.close()
con.close()

# 2) Parse using column names
con = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_COLNAMES)
cur = con.execute("CREATE TABLE test(p)")

cur.execute("INSERT INTO test(p) VALUES(?)", (p,))
cur.execute('SELECT p AS "p [point]" FROM test')
print("with column names:", cur.fetchone()[0])
cur.close()
con.close()
```