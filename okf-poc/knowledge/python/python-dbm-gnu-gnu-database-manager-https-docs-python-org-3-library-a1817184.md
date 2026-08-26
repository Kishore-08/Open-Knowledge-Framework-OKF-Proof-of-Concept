---
id: python-dbm-gnu-gnu-database-manager-https-docs-python-org-3-library-a1817184
type: concept
title: '`dbm.gnu` — GNU database manager[¶](https://docs.python.org/3/library/dbm.html#module-dbm.gnu
  "Link to this heading")'
description: '**Source code:** [Lib/dbm/gnu.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/gnu.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/dbm.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## `dbm.gnu` — GNU database manager[¶](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "Link to this heading")

**Source code:** [Lib/dbm/gnu.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/gnu.py)

---

The `dbm.gnu` module provides an interface to the GDBM
library, similar to the [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") module, but with additional
functionality like crash tolerance.

Note

The file formats created by `dbm.gnu` and [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") are incompatible
and can not be used interchangeably.

[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability)
or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

*exception* dbm.gnu.error[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.error "Link to this definition")
:   Raised on `dbm.gnu`-specific errors, such as I/O errors. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is
    raised for general mapping errors like specifying an incorrect key.

dbm.gnu.open\_flags[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.open_flags "Link to this definition")
:   A string of characters the *flag* parameter of [`open()`](https://docs.python.org/3/library/dbm.html#dbm.gnu.open "dbm.gnu.open") supports.

dbm.gnu.open(*filename*, *flag='r'*, *mode=0o666*, */*)[¶](https://docs.python.org/3/library/dbm.html#dbm.gnu.open "Link to this definition")
:   Open a GDBM database and return a `gdbm` object.

    Parameters:
    :   - **filename** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) – The database file to open.
        - **flag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) –

          - `'r'` (default): Open existing database for reading only.
          - `'w'`: Open existing database for reading and writing.
          - `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
          - `'n'`: Always create a new, empty database, open for reading and writing.

          The following additional characters may be appended
          to control how the database is opened:

          - `'f'`: Open the database in fast mode.
            Writes to the database will not be synchronized.
          - `'s'`: Synchronized mode.
            Changes to the database will be written immediately to the file.
          - `'u'`: Do not lock database.

          Not all flags are valid for all versions of GDBM.
          See the [`open_flags`](https://docs.python.org/3/library/dbm.html#dbm.gnu.open_flags "dbm.gnu.open_flags") member for a list of supported flag characters.
        - **mode** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    Raises:
    :   [**error**](https://docs.python.org/3/library/dbm.html#dbm.gnu.error "dbm.gnu.error") – If an invalid *flag* argument is passed.

    Changed in version 3.11: *filename* accepts a [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object).

    `gdbm` objects behave similar to mutable [mappings](https://docs.python.org/3/glossary.html#term-mapping),
    but methods `items()`, `values()`, `pop()`, `popitem()`,
    and `update()` are not supported,
    the `keys()` method returns a list, and
    the `setdefault()` method requires two arguments.
    It also supports a “closing” context manager via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword.

    Changed in ve