---
id: python-dbm-dumb-portable-dbm-implementation-https-docs-python-org-3-a1817184
type: concept
title: '`dbm.dumb` — Portable DBM implementation[¶](https://docs.python.org/3/library/dbm.html#module-dbm.dumb
  "Link to this heading")'
description: '**Source code:** [Lib/dbm/dumb.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/dumb.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/dbm.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## `dbm.dumb` — Portable DBM implementation[¶](https://docs.python.org/3/library/dbm.html#module-dbm.dumb "Link to this heading")

**Source code:** [Lib/dbm/dumb.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/dumb.py)

Note

The `dbm.dumb` module is intended as a last resort fallback for the
`dbm` module when a more robust module is not available. The `dbm.dumb`
module is not written for speed and is not nearly as heavily used as the other
database modules.

---

The `dbm.dumb` module provides a persistent [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict")-like
interface which is written entirely in Python.
Unlike other `dbm` backends, such as [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager"), no
external library is required.

The `dbm.dumb` module defines the following:

*exception* dbm.dumb.error[¶](https://docs.python.org/3/library/dbm.html#dbm.dumb.error "Link to this definition")
:   Raised on `dbm.dumb`-specific errors, such as I/O errors. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is
    raised for general mapping errors like specifying an incorrect key.

dbm.dumb.open(*filename*, *flag='c'*, *mode=0o666*)[¶](https://docs.python.org/3/library/dbm.html#dbm.dumb.open "Link to this definition")
:   Open a `dbm.dumb` database.

    Parameters:
    :   - **filename** –

          The basename of the database file (without extensions).
          A new database creates the following files:

          - `filename.dat`
          - `filename.dir`
        - **flag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) –

          - `'r'`: Open existing database for reading only.
          - `'w'`: Open existing database for reading and writing.
          - `'c'` (default): Open database for reading and writing, creating it if it doesn’t exist.
          - `'n'`: Always create a new, empty database, open for reading and writing.
        - **mode** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    Warning

    It is possible to crash the Python interpreter when loading a database
    with a sufficiently large/complex entry due to stack depth limitations in
    Python’s AST compiler.

    Changed in version 3.5: `open()` always creates a new database when *flag* is `'n'`.

    Changed in version 3.8: A database opened read-only if *flag* is `'r'`.
    A database is not created if it does not exist if *flag* is `'r'` or `'w'`.

    Changed in version 3.11: *filename* accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

    The returned database object behaves similar to a mutable [mapping](https://docs.python.org/3/glossary.html#term-mapping),
    but the `keys()` and `items()` methods return lists, and
    the `setdefault()` method requires two arguments.
    It also supports a “closing” context manager via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword.

    The following methods are also provided:

    dumbdbm.close()[¶](https://docs.python.org/3/library/dbm.html#dbm.dumb.dumbdbm.close "Link to this definition")
    :   Close the database.

    dumbdbm.sync()[¶](https://docs.python.org/3/library/dbm.html#dbm.dumb.dumbdbm.sync "Link to this definition")
    :   Synchronize the on-disk directory and data files. This method is called
        by the [`shelve.Shelf.sync()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync "shelve.Shelf.sync") method.