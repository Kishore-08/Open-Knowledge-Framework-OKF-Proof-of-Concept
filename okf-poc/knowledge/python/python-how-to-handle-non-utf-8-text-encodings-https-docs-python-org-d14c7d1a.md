---
id: python-how-to-handle-non-utf-8-text-encodings-https-docs-python-org-d14c7d1a
type: concept
title: How to handle non-UTF-8 text encodings[¶](https://docs.python.org/3/library/sqlite3.html#how-to-handle-non-utf-8-text-encodings
  "Link to this heading")
description: By default, `sqlite3` uses [`str`](https://docs.python.org/3/library/stdtypes.html#str
  "str") to adapt SQLite values
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/sqlite3.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### How to handle non-UTF-8 text encodings[¶](https://docs.python.org/3/library/sqlite3.html#how-to-handle-non-utf-8-text-encodings "Link to this heading")

By default, `sqlite3` uses [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") to adapt SQLite values
with the `TEXT` data type.
This works well for UTF-8 encoded text, but it might fail for other encodings
and invalid UTF-8.
You can use a custom [`text_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.text_factory "sqlite3.Connection.text_factory") to handle such cases.

Because of SQLite’s [flexible typing](https://www.sqlite.org/flextypegood.html), it is not uncommon to encounter table
columns with the `TEXT` data type containing non-UTF-8 encodings,
or even arbitrary data.
To demonstrate, let’s assume we have a database with ISO-8859-2 (Latin-2)
encoded text, for example a table of Czech-English dictionary entries.
Assuming we now have a [`Connection`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection "sqlite3.Connection") instance `con`
connected to this database,
we can decode the Latin-2 encoded text using this [`text_factory`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.text_factory "sqlite3.Connection.text_factory"):

```
con.text_factory = lambda data: str(data, encoding="latin2")
```

For invalid UTF-8 or arbitrary data in stored in `TEXT` table columns,
you can use the following technique, borrowed from the [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html#unicode-howto):

```
con.text_factory = lambda data: str(data, errors="surrogateescape")
```

Note

The `sqlite3` module API does not support strings
containing surrogates.

See also

[Unicode HOWTO](https://docs.python.org/3/howto/unicode.html#unicode-howto)

## Explanation[¶](https://docs.python.org/3/library/sqlite3.html#explanation "Link to this heading")