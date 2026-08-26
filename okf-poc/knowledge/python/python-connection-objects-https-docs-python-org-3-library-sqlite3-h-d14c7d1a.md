---
id: python-connection-objects-https-docs-python-org-3-library-sqlite3-h-d14c7d1a
type: concept
title: Connection objects[¶](https://docs.python.org/3/library/sqlite3.html#connection-objects
  "Link to this heading")
description: '*class* sqlite3.Connection[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Connection objects[¶](https://docs.python.org/3/library/sqlite3.html#connection-objects "Link to this heading")

*class* sqlite3.Connection[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "Link to this definition")
:   Each open SQLite database is represented by a `Connection` object,
    which is created using [`sqlite3.connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect").
    Their main purpose is creating [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") objects,
    and [Transaction control](https://docs.python.org/3/library/sqlite3.html#sqlite3-controlling-transactions).

    See also

    - [How to use connection shortcut methods](https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-shortcuts)
    - [How to use the connection context manager](https://docs.python.org/3/library/sqlite3.html#sqlite3-connection-context-manager)

    Changed in version 3.13: A [`ResourceWarning`](https://docs.python.org/3/library/exceptions.html#ResourceWarning "ResourceWarning") is emitted if [`close()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.close "sqlite3.Connection.close") is not called before
    a `Connection` object is deleted.

    An SQLite database connection has the following attributes and methods:

    cursor(*factory=Cursor*)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.cursor "Link to this definition")
    :   Create and return a [`Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor "sqlite3.Cursor") object.
        The cursor method accepts a single optional parameter *factory*. If
        supplied, this must be a [callable](https://docs.python.org/3/glossary.html#term-callable) returning
        an instance of `Cursor` or its subclasses.

    blobopen(*table*, *column*, *rowid*, */*, *\**, *readonly=False*, *name='main'*)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.blobopen "Link to this definition")
    :   Open a [`Blob`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob "sqlite3.Blob") handle to an existing
        BLOB.

        Parameters:
        :   - **table** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the table where the blob is located.
            - **column** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the column where the blob is located.
            - **rowid** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The row id where the blob is located.
            - **readonly** ([*bool*](https://docs.python.org/3/library/functions.html#bool "bool")) – Set to `True` if the blob should be opened without write
              permissions.
              Defaults to `False`.
            - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) – The name of the database where the blob is located.
              Defaults to `"main"`.

        Raises:
        :   [**OperationalError**](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "sqlite3.OperationalError") – When trying to open a blob in a `WITHOUT ROWID` table.

        Return type:
        :   [Blob](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob "sqlite3.Blob")

        Note

        The blob size cannot be changed using the [`Blob`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Blob "sqlite3.Blob") class.
        Use the SQL function `zeroblob` to create a blob with a fixed size.

        Added in version 3.11.

    commit()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.commit "Link to this definition")
    :   Commit any pending transaction to the database.
        If [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is `True`, or there is no open transaction,
        this method does