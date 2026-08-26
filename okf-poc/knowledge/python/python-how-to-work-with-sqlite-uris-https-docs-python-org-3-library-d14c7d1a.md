---
id: python-how-to-work-with-sqlite-uris-https-docs-python-org-3-library-d14c7d1a
type: concept
title: How to work with SQLite URIs[¶](https://docs.python.org/3/library/sqlite3.html#how-to-work-with-sqlite-uris
  "Link to this heading")
description: 'Some useful URI tricks include:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to work with SQLite URIs[¶](https://docs.python.org/3/library/sqlite3.html#how-to-work-with-sqlite-uris "Link to this heading")

Some useful URI tricks include:

- Open a database in read-only mode:

```
>>> con = sqlite3.connect("file:tutorial.db?mode=ro", uri=True)
>>> con.execute("CREATE TABLE readonly(data)")
Traceback (most recent call last):
OperationalError: attempt to write a readonly database
>>> con.close()
```

- Do not implicitly create a new database file if it does not already exist;
  will raise [`OperationalError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "sqlite3.OperationalError") if unable to create a new file:

```
>>> con = sqlite3.connect("file:nosuchdb.db?mode=rw", uri=True)
Traceback (most recent call last):
OperationalError: unable to open database file
```

- Create a shared named in-memory database:

```
db = "file:mem1?mode=memory&cache=shared"
con1 = sqlite3.connect(db, uri=True)
con2 = sqlite3.connect(db, uri=True)
with con1:
    con1.execute("CREATE TABLE shared(data)")
    con1.execute("INSERT INTO shared VALUES(28)")
res = con2.execute("SELECT data FROM shared")
assert res.fetchone() == (28,)

con1.close()
con2.close()
```

More information about this feature, including a list of parameters,
can be found in the [SQLite URI documentation](https://www.sqlite.org/uri.html).