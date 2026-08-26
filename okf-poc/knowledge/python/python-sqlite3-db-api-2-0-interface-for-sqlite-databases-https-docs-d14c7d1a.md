---
id: python-sqlite3-db-api-2-0-interface-for-sqlite-databases-https-docs-d14c7d1a
type: concept
title: '`sqlite3` — DB-API 2.0 interface for SQLite databases[¶](https://docs.python.org'
description: '**Source code:** [Lib/sqlite3/](https://github.com/python/cpython/tree/3.14/Lib/sqlite3/)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `sqlite3` — DB-API 2.0 interface for SQLite databases[¶](https://docs.python.org/3/library/sqlite3.html#module-sqlite3 "Link to this heading")

**Source code:** [Lib/sqlite3/](https://github.com/python/cpython/tree/3.14/Lib/sqlite3/)

SQLite is a C library that provides a lightweight disk-based database that
doesn’t require a separate server process and allows accessing the database
using a nonstandard variant of the SQL query language. Some applications can use
SQLite for internal data storage. It’s also possible to prototype an
application using SQLite and then port the code to a larger database such as
PostgreSQL or Oracle.

The `sqlite3` module was written by Gerhard Häring. It provides an SQL interface
compliant with the DB-API 2.0 specification described by [**PEP 249**](https://peps.python.org/pep-0249/), and
requires the third-party [SQLite](https://sqlite.org/) library.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).

This document includes four main sections:

- [Tutorial](https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial) teaches how to use the `sqlite3` module.
- [Reference](https://docs.python.org/3/library/sqlite3.html#sqlite3-reference) describes the classes and functions this module
  defines.
- [How-to guides](https://docs.python.org/3/library/sqlite3.html#sqlite3-howtos) details how to handle specific tasks.
- [Explanation](https://docs.python.org/3/library/sqlite3.html#sqlite3-explanation) provides in-depth background on
  transaction control.

See also

<https://www.sqlite.org>
:   The SQLite web page; the documentation describes the syntax and the
    available data types for the supported SQL dialect.

<https://www.w3schools.com/sql/>
:   Tutorial, reference and examples for learning SQL syntax.

[**PEP 249**](https://peps.python.org/pep-0249/) - Database API Specification 2.0
:   PEP written by Marc-André Lemburg.