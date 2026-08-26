---
id: python-module-constants-https-docs-python-org-3-library-sqlite3-htm-d14c7d1a
type: concept
title: Module constants[¶](https://docs.python.org/3/library/sqlite3.html#module-constants
  "Link to this heading")
description: sqlite3.LEGACY\_TRANSACTION\_CONTROL[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Module constants[¶](https://docs.python.org/3/library/sqlite3.html#module-constants "Link to this heading")

sqlite3.LEGACY\_TRANSACTION\_CONTROL[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.LEGACY_TRANSACTION_CONTROL "Link to this definition")
:   Set [`autocommit`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.autocommit "sqlite3.Connection.autocommit") to this constant to select
    old style (pre-Python 3.12) transaction control behaviour.
    See [Transaction control via the isolation\_level attribute](https://docs.python.org/3/library/sqlite3.html#sqlite3-transaction-control-isolation-level) for more information.

sqlite3.PARSE\_DECLTYPES[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES "Link to this definition")
:   Pass this flag value to the *detect\_types* parameter of
    [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect") to look up a converter function using
    the declared types for each column.
    The types are declared when the database table is created.
    `sqlite3` will look up a converter function using the first word of the
    declared type as the converter dictionary key.
    For example:

    ```
    CREATE TABLE test(
       i integer primary key,  ! will look up a converter named "integer"
       p point,                ! will look up a converter named "point"
       n number(10)            ! will look up a converter named "number"
     )
    ```

    This flag may be combined with [`PARSE_COLNAMES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES "sqlite3.PARSE_COLNAMES") using the `|`
    (bitwise or) operator.

    Note

    Generated fields (for example `MAX(p)`) are returned as [`str`](https://docs.python.org/3/library/stdtypes.html#str "str").
    Use `PARSE_COLNAMES` to enforce types for such queries.

sqlite3.PARSE\_COLNAMES[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_COLNAMES "Link to this definition")
:   Pass this flag value to the *detect\_types* parameter of
    [`connect()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.connect "sqlite3.connect") to look up a converter function by
    using the type name, parsed from the query column name,
    as the converter dictionary key.
    The query column name must be wrapped in double quotes (`"`)
    and the type name must be wrapped in square brackets (`[]`).

    ```
    SELECT MAX(p) as "p [point]" FROM test;  ! will look up converter "point"
    ```

    This flag may be combined with [`PARSE_DECLTYPES`](https://docs.python.org/3/library/sqlite3.html#sqlite3.PARSE_DECLTYPES "sqlite3.PARSE_DECLTYPES") using the `|`
    (bitwise or) operator.

sqlite3.SQLITE\_OK[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_OK "Link to this definition")

sqlite3.SQLITE\_DENY[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_DENY "Link to this definition")

sqlite3.SQLITE\_IGNORE[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.SQLITE_IGNORE "Link to this definition")
:   Flags that should be returned by the *authorizer\_callback* [callable](https://docs.python.org/3/glossary.html#term-callable)
    passed to [`Connection.set_authorizer()`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.set_authorizer "sqlite3.Connection.set_authorizer"), to indicate whether:

    - Access is allowed (`SQLITE_OK`),
    - The SQL statement should be aborted with an error (`SQLITE_DENY`)
    - The column should be treated as a `NULL` value (`SQLITE_IGNORE`)

sqlite3.apilevel[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.apilevel "Link to this definition")
:   String constant stating the supported DB-API level. Required by the DB-API.
    Hard-coded to `"2.0"`.

sqlite3.paramstyle[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.paramstyle "Link to this definition")
:   String constant stating the type of parameter marker formatting expected