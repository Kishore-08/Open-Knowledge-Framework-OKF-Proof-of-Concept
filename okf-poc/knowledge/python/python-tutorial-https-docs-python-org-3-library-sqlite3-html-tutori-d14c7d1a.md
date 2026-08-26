---
id: python-tutorial-https-docs-python-org-3-library-sqlite3-html-tutori-d14c7d1a
type: concept
title: Tutorial[¶](https://docs.python.org/3/library/sqlite3.html#tutorial "Link to
  this heading")
description: In this tutorial, you will create a database of Monty Python movies
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Tutorial[¶](https://docs.python.org/3/library/sqlite3.html#tutorial "Link to this heading")

In this tutorial, you will create a database of Monty Python movies
using basic `sqlite3` functionality.
It assumes a fundamental understanding of database concepts,
including [cursors](https://en.wikipedia.org/wiki/Cursor_(databases)) and [transactions](https://en.wikipedia.org/wiki/Database_transaction).

First, we need to create a new database and open
a database connection to allow `sqlite3` to work with it.
Call [`sqlite3.connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect") to create a connection to
the database `tutorial.db` in the current working directory,
implicitly creating it if it does not exist:

```
import sqlite3
con = sqlite3.connect("tutorial.db")
```

The returned [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") object `con`
represents the connection to the on-disk database.

In order to execute SQL statements and fetch results from SQL queries,
we will need to use a database cursor.
Call [`con.cursor()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor "sqlite3.Connection.cursor") to create the [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor"):

```
cur = con.cursor()
```

Now that we’ve got a database connection and a cursor,
we can create a database table `movie` with columns for title,
release year, and review score.
For simplicity, we can just use column names in the table declaration –
thanks to the [flexible typing](https://www.sqlite.org/flextypegood.html) feature of SQLite,
specifying the data types is optional.
Execute the `CREATE TABLE` statement
by calling [`cur.execute(...)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute"):

```
cur.execute("CREATE TABLE movie(title, year, score)")
```

We can verify that the new table has been created by querying
the `sqlite_master` table built-in to SQLite,
which should now contain an entry for the `movie` table definition
(see [The Schema Table](https://www.sqlite.org/schematab.html) for details).
Execute that query by calling [`cur.execute(...)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute"),
assign the result to `res`,
and call [`res.fetchone()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.fetchone "sqlite3.Cursor.fetchone") to fetch the resulting row:

```
>>> res = cur.execute("SELECT name FROM sqlite_master")
>>> res.fetchone()
('movie',)
```

We can see that the table has been created,
as the query returns a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") containing the table’s name.
If we query `sqlite_master` for a non-existent table `spam`,
`res.fetchone()` will return `None`:

```
>>> res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
>>> res.fetchone() is None
True
```

Now, add two rows of data supplied as SQL literals
by executing an `INSERT` statement,
once again by calling [`cur.execute(...)`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute"):

```
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
```

The `INSERT` statement implicitly opens a transaction,
which needs to be committed before changes are saved in the database
(see [Transaction control](https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions) for details).
Call [`con.commit()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "sqlite3.Connection.commit") on the connection object
to commit the transaction:

```
con.commit()
```

We can verify that the data was inserted correctly
by executing a `SELECT` query.
Use the now-familiar [`cur.execute(...)`](https://docs