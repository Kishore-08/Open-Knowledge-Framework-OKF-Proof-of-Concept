---
id: python-cursor-objects-https-docs-python-org-3-library-sqlite3-html--d14c7d1a
type: concept
title: Cursor objects[¶](https://docs.python.org/3/library/sqlite3.html#cursor-objects
  "Link to this heading")
description: '> A `Cursor` object represents a [database cursor](https://en.wikipedia.org/wiki/Cursor_(databases))'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Cursor objects[¶](https://docs.python.org/3/library/sqlite3.html#cursor-objects "Link to this heading")

> A `Cursor` object represents a [database cursor](https://en.wikipedia.org/wiki/Cursor_(databases))
> which is used to execute SQL statements,
> and manage the context of a fetch operation.
> Cursors are created using [`Connection.cursor()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor "sqlite3.Connection.cursor"),
> or by using any of the [connection shortcut methods](https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-shortcuts).
>
> Cursor objects are [iterators](https://docs.python.org/3/glossary.html#term-iterator),
> meaning that if you [`execute()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "sqlite3.Cursor.execute") a `SELECT` query,
> you can simply iterate over the cursor to fetch the resulting rows:
>
> ```
> for row in cur.execute("SELECT t FROM data"):
>     print(row)
> ```

*class* sqlite3.Cursor[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "Link to this definition")
:   A `Cursor` instance has the following attributes and methods.

    execute(*sql*, *parameters=()*, */*)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute "Link to this definition")
    :   Execute a single SQL statement,
        optionally binding Python values using
        [placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).

        Parameters:
        :   - **sql** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – A single SQL statement.
            - **parameters** ([`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") | [sequence](https://docs.python.org/3/glossary.html#term-sequence)) – Python values to bind to placeholders in *sql*.
              A `dict` if named placeholders are used.
              A sequence if unnamed placeholders are used.
              See [How to use placeholders to bind values in SQL queries](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).

        Raises:
        :   [**ProgrammingError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") – When *sql* contains more than one SQL statement.
            When [named placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders) are used
            and *parameters* is a sequence instead of a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict").

        If [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is
        [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL"),
        [`isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") is not `None`,
        *sql* is an `INSERT`, `UPDATE`, `DELETE`, or `REPLACE` statement,
        and there is no open transaction,
        a transaction is implicitly opened before executing *sql*.

        Changed in version 3.14: [`ProgrammingError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") is emitted if
        [named placeholders](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders) are used
        and *parameters* is a sequence instead of a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict").

        Use [`executescript()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executescript "sqlite3.Cursor.executescript") to execute multiple SQL statements.

    executemany(*sql*, *parameters*, */*)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany "Link to this definition")
    :   For every item in *parameters*,
        repeatedly execute the [parameterized](h