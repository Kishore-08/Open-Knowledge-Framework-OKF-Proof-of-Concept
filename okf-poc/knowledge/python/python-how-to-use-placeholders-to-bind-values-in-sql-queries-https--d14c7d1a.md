---
id: python-how-to-use-placeholders-to-bind-values-in-sql-queries-https--d14c7d1a
type: concept
title: How to use placeholders to bind values in SQL queries[¶](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries
  "Link to this heading")
description: SQL operations usually need to use values from Python variables. However,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to use placeholders to bind values in SQL queries[¶](https://docs.python.org/3/library/sqlite3.html#how-to-use-placeholders-to-bind-values-in-sql-queries "Link to this heading")

SQL operations usually need to use values from Python variables. However,
beware of using Python’s string operations to assemble queries, as they
are vulnerable to [SQL injection attacks](https://en.wikipedia.org/wiki/SQL_injection). For example, an attacker can simply
close the single quote and inject `OR TRUE` to select all rows:

```
>>> # Never do this -- insecure!
>>> symbol = input()
' OR TRUE; --
>>> sql = "SELECT * FROM stocks WHERE symbol = '%s'" % symbol
>>> print(sql)
SELECT * FROM stocks WHERE symbol = '' OR TRUE; --'
>>> cur.execute(sql)
```

Instead, use the DB-API’s parameter substitution. To insert a variable into a
query string, use a placeholder in the string, and substitute the actual values
into the query by providing them as a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") of values to the second
argument of the cursor’s [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") method.

An SQL statement may use one of two kinds of placeholders:
question marks (qmark style) or named placeholders (named style).
For the qmark style, *parameters* must be a
[sequence](https://docs.python.org/3/glossary.html#term-sequence) whose length must match the number of placeholders,
or a [`ProgrammingError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") is raised.
For the named style, *parameters* must be
an instance of a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") (or a subclass),
which must contain keys for all named parameters;
any extra items are ignored.
Here’s an example of both styles:

```
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

# This is the named style used with executemany():
data = (
    {"name": "C", "year": 1972},
    {"name": "Fortran", "year": 1957},
    {"name": "Python", "year": 1991},
    {"name": "Go", "year": 2009},
)
cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)

# This is the qmark style used in a SELECT query:
params = (1972,)
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
print(cur.fetchall())
con.close()
```

Note

[**PEP 249**](https://peps.python.org/pep-0249/) numeric placeholders are *not* supported.
If used, they will be interpreted as named placeholders.