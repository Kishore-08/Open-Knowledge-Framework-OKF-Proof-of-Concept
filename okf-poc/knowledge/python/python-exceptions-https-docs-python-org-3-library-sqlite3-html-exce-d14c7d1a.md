---
id: python-exceptions-https-docs-python-org-3-library-sqlite3-html-exce-d14c7d1a
type: concept
title: Exceptions[¶](https://docs.python.org/3/library/sqlite3.html#exceptions "Link
  to this heading")
description: The exception hierarchy is defined by the DB-API 2.0 ([**PEP 249**](https://peps.python.org/pep-0249/)).
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Exceptions[¶](https://docs.python.org/3/library/sqlite3.html#exceptions "Link to this heading")

The exception hierarchy is defined by the DB-API 2.0 ([**PEP 249**](https://peps.python.org/pep-0249/)).

*exception* sqlite3.Warning[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Warning "Link to this definition")
:   This exception is not currently raised by the `sqlite3` module,
    but may be raised by applications using `sqlite3`,
    for example if a user-defined function truncates data while inserting.
    `Warning` is a subclass of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception").

*exception* sqlite3.Error[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error "Link to this definition")
:   The base class of the other exceptions in this module.
    Use this to catch all errors with one single [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) statement.
    `Error` is a subclass of [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception").

    If the exception originated from within the SQLite library,
    the following two attributes are added to the exception:

    sqlite\_errorcode[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error.sqlite_errorcode "Link to this definition")
    :   The numeric error code from the
        [SQLite API](https://sqlite.org/rescode.html)

        Added in version 3.11.

    sqlite\_errorname[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error.sqlite_errorname "Link to this definition")
    :   The symbolic name of the numeric error code
        from the [SQLite API](https://sqlite.org/rescode.html)

        Added in version 3.11.

*exception* sqlite3.InterfaceError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.InterfaceError "Link to this definition")
:   Exception raised for misuse of the low-level SQLite C API.
    In other words, if this exception is raised, it probably indicates a bug in the
    `sqlite3` module.
    `InterfaceError` is a subclass of [`Error`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error "sqlite3.Error").

*exception* sqlite3.DatabaseError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "Link to this definition")
:   Exception raised for errors that are related to the database.
    This serves as the base exception for several types of database errors.
    It is only raised implicitly through the specialised subclasses.
    `DatabaseError` is a subclass of [`Error`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Error "sqlite3.Error").

*exception* sqlite3.DataError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.DataError "Link to this definition")
:   Exception raised for errors caused by problems with the processed data,
    like numeric values out of range, and strings which are too long.
    `DataError` is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").

*exception* sqlite3.OperationalError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.OperationalError "Link to this definition")
:   Exception raised for errors that are related to the database’s operation,
    and not necessarily under the control of the programmer.
    For example, the database path is not found,
    or a transaction could not be processed.
    `OperationalError` is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").

*exception* sqlite3.IntegrityError[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.IntegrityError "Link to this definition")
:   Exception raised when the relational integrity of the database is affected,
    e.g. a foreign key check fails. It is a subclass of [`DatabaseError`](https://docs.python.org/3/library/sqlite3.html#sqlite3.DatabaseError "sqlite3.DatabaseError").

*exception* sqlite3.InternalErro