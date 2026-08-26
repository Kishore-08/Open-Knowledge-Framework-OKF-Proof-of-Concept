---
id: python-module-functions-https-docs-python-org-3-library-sqlite3-htm-d14c7d1a
type: concept
title: Module functions[¶](https://docs.python.org/3/library/sqlite3.html#module-functions
  "Link to this heading")
description: sqlite3.connect(*database*, *timeout=5.0*, *detect\_types=0*, *isolation\_level='DEFERRED'*,
  *check\_same\_thread=True*, *factory=sqlite3.Connection*, *cached\_statements=128*,
  *uri=False*, *\**, *aut
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Module functions[¶](https://docs.python.org/3/library/sqlite3.html#module-functions "Link to this heading")

sqlite3.connect(*database*, *timeout=5.0*, *detect\_types=0*, *isolation\_level='DEFERRED'*, *check\_same\_thread=True*, *factory=sqlite3.Connection*, *cached\_statements=128*, *uri=False*, *\**, *autocommit=sqlite3.LEGACY\_TRANSACTION\_CONTROL*)[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "Link to this definition")
:   Open a connection to an SQLite database.

    Parameters:
    :   - **database** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) – The path to the database file to be opened.
          You can pass `":memory:"` to create an [SQLite database existing only
          in memory](https://sqlite.org/inmemorydb.html), and open a connection
          to it.
        - **timeout** ([*float*](https://docs.python.org/3/library/functions.html#float "float")) – How many seconds the connection should wait before raising
          an [`OperationalError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "sqlite3.OperationalError") when a table is locked.
          If another connection opens a transaction to modify a table,
          that table will be locked until the transaction is committed.
          Default five seconds.
        - **detect\_types** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – Control whether and how data types not
          [natively supported by SQLite](https://docs.python.org/3/library/sqlite3.html#sqlite3-types)
          are looked up to be converted to Python types,
          using the converters registered with [`register_converter()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.register_converter "sqlite3.register_converter").
          Set it to any combination (using `|`, bitwise or) of
          [`PARSE_DECLTYPES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES "sqlite3.PARSE_DECLTYPES") and [`PARSE_COLNAMES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES "sqlite3.PARSE_COLNAMES")
          to enable this.
          Column names take precedence over declared types if both flags are set.
          By default (`0`), type detection is disabled.
        - **isolation\_level** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str") *|* *None*) – Control legacy transaction handling behaviour.
          See [`Connection.isolation_level`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.isolation_level "sqlite3.Connection.isolation_level") and
          [Transaction control via the isolation\_level attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level) for more information.
          Can be `"DEFERRED"` (default), `"EXCLUSIVE"` or `"IMMEDIATE"`;
          or `None` to disable opening transactions implicitly.
          Has no effect unless [`Connection.autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") is set to
          [`LEGACY_TRANSACTION_CONTROL`](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "sqlite3.LEGACY_TRANSACTION_CONTROL") (the default).
        - **check\_same\_thread** ([*bool*](https://docs.python.org/3/library/functions.html#bool "bool")) – If `True` (default), [`ProgrammingError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.ProgrammingError "sqlite3.ProgrammingError") will be raised
          if the database connection is used by a thread
          other than the one that created it.
          If `False`, the connection may be accessed in multiple threads;
          write operations may need to be serialized by the user
          to avoid data corruption.
          See [`threadsafety`](https://docs.python.org/3/library/sqlite3.html#sqlite3.threadsafety "sqlite3.threadsafety") for more information.
        - **factory** ([