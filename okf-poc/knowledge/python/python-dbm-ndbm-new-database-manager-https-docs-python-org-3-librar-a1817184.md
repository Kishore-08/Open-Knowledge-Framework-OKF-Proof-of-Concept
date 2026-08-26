---
id: python-dbm-ndbm-new-database-manager-https-docs-python-org-3-librar-a1817184
type: concept
title: '`dbm.ndbm` — New Database Manager[¶](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm
  "Link to this heading")'
description: '**Source code:** [Lib/dbm/ndbm.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/ndbm.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/dbm.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## `dbm.ndbm` — New Database Manager[¶](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "Link to this heading")

**Source code:** [Lib/dbm/ndbm.py](https://github.com/python/cpython/tree/3.14/Lib/dbm/ndbm.py)

---

The `dbm.ndbm` module provides an interface to the
NDBM library.
This module can be used with the “classic” NDBM interface or the
GDBM compatibility interface.

Note

The file formats created by [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager") and `dbm.ndbm` are incompatible
and can not be used interchangeably.

Warning

The NDBM library shipped as part of macOS has an undocumented limitation on the
size of values, which can result in corrupted database files
when storing values larger than this limit. Reading such corrupted files can
result in a hard crash (segmentation fault).

[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability)
or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

*exception* dbm.ndbm.error[¶](https://docs.python.org/3/library/dbm.html#dbm.ndbm.error "Link to this definition")
:   Raised on `dbm.ndbm`-specific errors, such as I/O errors. [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised
    for general mapping errors like specifying an incorrect key.

dbm.ndbm.library[¶](https://docs.python.org/3/library/dbm.html#dbm.ndbm.library "Link to this definition")
:   Name of the NDBM implementation library used.

dbm.ndbm.open(*filename*, *flag='r'*, *mode=0o666*, */*)[¶](https://docs.python.org/3/library/dbm.html#dbm.ndbm.open "Link to this definition")
:   Open an NDBM database and return an `ndbm` object.

    Parameters:
    :   - **filename** ([path-like object](https://docs.python.org/3/glossary.html#term-path-like-object)) – The basename of the database file
          (without the `.dir` or `.pag` extensions).
        - **flag** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "str")) –

          - `'r'` (default): Open existing database for reading only.
          - `'w'`: Open existing database for reading and writing.
          - `'c'`: Open database for reading and writing, creating it if it doesn’t exist.
          - `'n'`: Always create a new, empty database, open for reading and writing.
        - **mode** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The Unix file access mode of the file (default: octal `0o666`),
          used only when the database has to be created.

    Changed in version 3.11: Accepts [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for filename.

    `ndbm` objects behave similar to mutable [mappings](https://docs.python.org/3/glossary.html#term-mapping),
    but methods `items()`, `values()`, `pop()`, `popitem()`,
    and `update()` are not supported,
    the `keys()` method returns a list, and
    the `setdefault()` method requires two arguments.
    It also supports a “closing” context manager via the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) keyword.

    Changed in version 3.2: Added the `get()` and `setdefault()` methods.

    Changed in version 3.13: Added the `clear()` method.

    The following method is also provided:

    ndbm.close()[¶](https://docs.python.org/3/library/dbm.html#dbm.ndbm.ndbm.close "Link to this definition")
    :   Close the NDBM database.