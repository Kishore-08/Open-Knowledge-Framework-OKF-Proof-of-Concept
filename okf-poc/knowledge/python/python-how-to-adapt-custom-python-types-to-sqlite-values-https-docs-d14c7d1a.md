---
id: python-how-to-adapt-custom-python-types-to-sqlite-values-https-docs-d14c7d1a
type: concept
title: How to adapt custom Python types to SQLite values[¶](https://docs.python.org/3/library/sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values
  "Link to this heading")
description: SQLite supports only a limited set of data types natively.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to adapt custom Python types to SQLite values[¶](https://docs.python.org/3/library/sqlite3.html#how-to-adapt-custom-python-types-to-sqlite-values "Link to this heading")

SQLite supports only a limited set of data types natively.
To store custom Python types in SQLite databases, *adapt* them to one of the
[Python types SQLite natively understands](https://docs.python.org/3/library/sqlite3.html#sqlite3-types).

There are two ways to adapt Python objects to SQLite types:
letting your object adapt itself, or using an *adapter callable*.
The latter will take precedence above the former.
For a library that exports a custom type,
it may make sense to enable that type to adapt itself.
As an application developer, it may make more sense to take direct control by
registering custom adapter functions.

#### How to write adaptable objects[¶](https://docs.python.org/3/library/sqlite3.html#how-to-write-adaptable-objects "Link to this heading")

Suppose we have a `Point` class that represents a pair of coordinates,
`x` and `y`, in a Cartesian coordinate system.
The coordinate pair will be stored as a text string in the database,
using a semicolon to separate the coordinates.
This can be implemented by adding a `__conform__(self, protocol)`
method which returns the adapted value.
The object passed to *protocol* will be of type [`PrepareProtocol`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PrepareProtocol "sqlite3.PrepareProtocol").

```
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __conform__(self, protocol):
        if protocol is sqlite3.PrepareProtocol:
            return f"{self.x};{self.y}"

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("SELECT ?", (Point(4.0, -3.2),))
print(cur.fetchone()[0])
con.close()
```

#### How to register adapter callables[¶](https://docs.python.org/3/library/sqlite3.html#how-to-register-adapter-callables "Link to this heading")

The other possibility is to create a function that converts the Python object
to an SQLite-compatible type.
This function can then be registered using [`register_adapter()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_adapter "sqlite3.register_adapter").

```
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

def adapt_point(point):
    return f"{point.x};{point.y}"

sqlite3.register_adapter(Point, adapt_point)

con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("SELECT ?", (Point(1.0, 2.5),))
print(cur.fetchone()[0])
con.close()
```