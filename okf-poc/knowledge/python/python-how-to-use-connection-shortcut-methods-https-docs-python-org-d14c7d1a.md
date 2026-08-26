---
id: python-how-to-use-connection-shortcut-methods-https-docs-python-org-d14c7d1a
type: concept
title: How to use connection shortcut methods[¶](https://docs.python.org/3/library/sqlite3.html#how-to-use-connection-shortcut-methods
  "Link to this heading")
description: Using the [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.execute
  "sqlite3.Connection.execute"),
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to use connection shortcut methods[¶](https://docs.python.org/3/library/sqlite3.html#how-to-use-connection-shortcut-methods "Link to this heading")

Using the [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.execute "sqlite3.Connection.execute"),
[`executemany()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.executemany "sqlite3.Connection.executemany"), and [`executescript()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.executescript "sqlite3.Connection.executescript")
methods of the [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") class, your code can
be written more concisely because you don’t have to create the (often
superfluous) [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") objects explicitly. Instead, the `Cursor`
objects are created implicitly and these shortcut methods return the cursor
objects. This way, you can execute a `SELECT` statement and iterate over it
directly using only a single call on the `Connection` object.

```
# Create and fill the table.
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE lang(name, first_appeared)")
data = [
    ("C++", 1985),
    ("Objective-C", 1984),
]
con.executemany("INSERT INTO lang(name, first_appeared) VALUES(?, ?)", data)

# Print the table contents
for row in con.execute("SELECT name, first_appeared FROM lang"):
    print(row)

print("I just deleted", con.execute("DELETE FROM lang").rowcount, "rows")

# close() is not a shortcut method and it's not called automatically;
# the connection object should be closed manually
con.close()
```