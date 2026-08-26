---
id: python-row-objects-https-docs-python-org-3-library-sqlite3-html-row-d14c7d1a
type: concept
title: Row objects[¶](https://docs.python.org/3/library/sqlite3.html#row-objects "Link
  to this heading")
description: '*class* sqlite3.Row[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Row objects[¶](https://docs.python.org/3/library/sqlite3.html#row-objects "Link to this heading")

*class* sqlite3.Row[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row "Link to this definition")
:   A `Row` instance serves as a highly optimized
    [`row_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory "sqlite3.Connection.row_factory") for [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") objects.
    It supports iteration, equality testing, [`len()`](https://docs.python.org/3/library/functions.html#len "len"),
    and [mapping](https://docs.python.org/3/glossary.html#term-mapping) access by column name and index.

    Two `Row` objects compare equal
    if they have identical column names and values.

    See [How to create and use row factories](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory) for more details.

    keys()[¶](https://docs.python.org/3/library/sqlite3.html#sqlite3.Row.keys "Link to this definition")
    :   Return a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") of column names as [`strings`](https://docs.python.org/3/library/stdtypes.html#str "str").
        Immediately after a query,
        it is the first member of each tuple in [`Cursor.description`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.description "sqlite3.Cursor.description").

    Changed in version 3.5: Added support of slicing.