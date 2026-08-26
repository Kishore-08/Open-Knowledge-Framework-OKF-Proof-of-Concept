---
id: python-dbm-interfaces-to-unix-databases-https-docs-python-org-3-lib-a1817184
type: concept
title: '`dbm` — Interfaces to Unix “databases”[¶](https://docs.python.org/3/library/dbm.'
description: '**Source code:** [Lib/dbm/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/__init__.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/dbm.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `dbm` — Interfaces to Unix “databases”[¶](https://docs.python.org/3/library/dbm.html#module-dbm "Link to this heading")

**Source code:** [Lib/dbm/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/__init__.py)

---

`dbm` is a generic interface to variants of the DBM database:

- [`dbm.sqlite3`](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm")
- [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager")
- [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager")

If none of these modules are installed, the
slow-but-simple implementation in module [`dbm.dumb`](https://docs.python.org/3/library/dbm.html#module-dbm.dumb "dbm.dumb: Portable implementation of the simple DBM interface.") will be used. There
is a [third party interface](https://www.jcea.es/programacion/pybsddb.htm) to
the Oracle Berkeley DB.

*exception* dbm.error[¶](https://docs.python.org/3/library/dbm.html#dbm.error "Link to this definition")
:   A tuple containing the exceptions that can be raised by each of the supported
    modules, with a unique exception also named [`dbm.error`](https://docs.python.org/3/library/dbm.html#dbm.error "dbm.error") as the first
    item — the latter is used when `dbm.error` is raised.

dbm.whichdb(*filename*)[¶](https://docs.python.org/3/library/dbm.html#dbm.whichdb "Link to this definition")
:   This function attempts to guess which of the several simple database modules
    available — [`dbm.sqlite3`](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3 "dbm.sqlite3: SQLite backend for dbm"), [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager"), [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager"),
    or [`dbm.dumb`](https://docs.python.org/3/library/dbm.html#module-dbm.dumb "dbm.dumb: Portable implementation of the simple DBM interface.") — should be used to open a given file.

    Return one of the following values:

    - `None` if the file can’t be opened because it’s unreadable or doesn’t exist
    - the empty string (`''`) if the file’s format can’t be guessed
    - a string containing the required module name, such as `'dbm.ndbm'` or `'dbm.gnu'`

    Changed in version 3.11: *filename* accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

dbm.open(*file*, *flag='r'*, *mode=0o666*)[¶](https://docs.python.org/3/library/dbm.html#dbm.open "Link to this definition")
:   Open a database and return the corresponding database object.

    Parameters:
    :   - **file** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) –

          The database file to open.

          If the database file already exists, the [`whichdb()`](https://docs.python.org/3/library/dbm.html#dbm.whichdb "dbm.whichdb") function is used to
          determine its type and the appropriate module is used; if it does not exist,
          the first submodule listed above that can be imported is used.
        - **flag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) –

          - `'r'` (default): Open existing database for reading only.
          - `'w'`: Open existing database for reading and writing.
          - `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
          - `'n'`: Always create a new, empty database, open for reading and writing.
        - **mode** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    Changed in version 3.11: *file* accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

The object returned by [`open()`](https://docs.python.org/3/library/dbm.html#