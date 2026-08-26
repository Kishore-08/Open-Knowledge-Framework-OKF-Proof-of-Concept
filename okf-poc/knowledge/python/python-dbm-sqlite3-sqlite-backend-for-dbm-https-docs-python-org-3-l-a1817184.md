---
id: python-dbm-sqlite3-sqlite-backend-for-dbm-https-docs-python-org-3-l-a1817184
type: concept
title: '`dbm.sqlite3` — SQLite backend for dbm[¶](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3
  "Link to this heading")'
description: Added in version 3.13.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/dbm.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## `dbm.sqlite3` — SQLite backend for dbm[¶](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "Link to this heading")

Added in version 3.13.

**Source code:** [Lib/dbm/sqlite3.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/sqlite3.py)

---

This module uses the standard library [`sqlite3`](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "sqlite3: A DB-API 2.0 implementation using SQLite 3.x.") module to provide an
SQLite backend for the `dbm` module.
The files created by `dbm.sqlite3` can thus be opened by `sqlite3`,
or any other SQLite browser, including the SQLite CLI.

[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

dbm.sqlite3.open(*filename*, */*, *flag='r'*, *mode=0o666*)[¶](https://docs.python.org/3/library/dbm.html#dbm.sqlite3.open "Link to this definition")
:   Open an SQLite database.

    Parameters:
    :   - **filename** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) – The path to the database to be opened.
        - **flag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) –

          - `'r'` (default): Open existing database for reading only.
          - `'w'`: Open existing database for reading and writing.
          - `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
          - `'n'`: Always create a new, empty database, open for reading and writing.
        - **mode** – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    The returned database object behaves similar to a mutable [mapping](https://docs.python.org/3/glossary.html#term-mapping),
    but the `keys()` method returns a list, and
    the `setdefault()` method requires two arguments.
    It also supports a “closing” context manager via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword.

    The following method is also provided:

    sqlite3.close()[¶](https://docs.python.org/3/library/dbm.html#dbm.sqlite3.sqlite3.close "Link to this definition")
    :   Close the SQLite database.