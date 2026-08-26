---
id: python-dialects-and-formatting-parameters-https-docs-python-org-3-l-9cfde96b
type: concept
title: Dialects and Formatting Parameters[¶](https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters
  "Link to this heading")
description: To make it easier to specify the format of input and output records,
  specific
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/csv.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Dialects and Formatting Parameters[¶](https://docs.python.org/3/library/csv.html#dialects-and-formatting-parameters "Link to this heading")

To make it easier to specify the format of input and output records, specific
formatting parameters are grouped together into dialects. A dialect is a
subclass of the [`Dialect`](https://docs.python.org/3/library/csv.html#csv.Dialect "csv.Dialect") class containing various attributes
describing the format of the CSV file. When creating [`reader`](https://docs.python.org/3/library/csv.html#csv.reader "csv.reader") or
[`writer`](https://docs.python.org/3/library/csv.html#csv.writer "csv.writer") objects, the programmer can specify a string or a subclass of
the `Dialect` class as the dialect parameter. In addition to, or instead
of, the *dialect* parameter, the programmer can also specify individual
formatting parameters, which have the same names as the attributes defined below
for the `Dialect` class.

Dialects support the following attributes:

Dialect.delimiter[¶](https://docs.python.org/3/library/csv.html#csv.Dialect.delimiter "Link to this definition")
:   A one-character string used to separate fields. It defaults to `','`.

Dialect.doublequote[¶](https://docs.python.org/3/library/csv.html#csv.Dialect.doublequote "Link to this definition")
:   Controls how instances of *quotechar* appearing inside a field should
    themselves be quoted. When [`True`](https://docs.python.org/3/library/constants.html#True "True"), the character is doubled. When
    [`False`](https://docs.python.org/3/library/constants.html#False "False"), the *escapechar* is used as a prefix to the *quotechar*. It
    defaults to `True`.

    On output, if *doublequote* is [`False`](https://docs.python.org/3/library/constants.html#False "False") and no *escapechar* is set,
    [`Error`](https://docs.python.org/3/library/csv.html#csv.Error "csv.Error") is raised if a *quotechar* is found in a field.

Dialect.escapechar[¶](https://docs.python.org/3/library/csv.html#csv.Dialect.escapechar "Link to this definition")
:   A one-character string used by the writer to escape characters that
    require escaping:

    > - the *delimiter*, the *quotechar*, `'\r'`, `'\n'` and any of the
    >   characters in *lineterminator* are escaped if *quoting* is set to
    >   [`QUOTE_NONE`](https://docs.python.org/3/library/csv.html#csv.QUOTE_NONE "csv.QUOTE_NONE");
    > - the *quotechar* is escaped if *doublequote* is [`False`](https://docs.python.org/3/library/constants.html#False "False");
    > - the *escapechar* itself.

    On reading, the *escapechar* removes any special meaning from
    the following character. It defaults to [`None`](https://docs.python.org/3/library/constants.html#None "None"), which disables escaping.

    Changed in version 3.10: Previously the *escapechar* itself was not escaped,
    which lost it on reading.

    Changed in version 3.11: An empty *escapechar* is not allowed.

Dialect.lineterminator[¶](https://docs.python.org/3/library/csv.html#csv.Dialect.lineterminator "Link to this definition")
:   The string used to terminate lines produced by the [`writer`](https://docs.python.org/3/library/csv.html#csv.writer "csv.writer"). It defaults
    to `'\r\n'`.

    Note

    The [`reader`](https://docs.python.org/3/library/csv.html#csv.reader "csv.reader") is hard-coded to recognise either `'\r'` or `'\n'` as
    end-of-line, and ignores *lineterminator*. This behavior may change in the
    future.

Dialect.quotechar[¶](https://docs.python.org/3/library/csv.html#csv.Dialect.quotechar "Link to this definition")
:   A one-character string used to quote fields containing special characters,
    such as the *delimiter* or the *quotechar*, or which contain new-line
    characters (`'\r'`, `'\n'` or any of the characters in *lineterminator*).
    It defaults to `'"'`.
    Can be set to `None` to prevent escaping `'"'` if *quoting* is set
    to [`QUOTE_NONE`](https://docs.python.org/3/library/csv.html#csv.QUOTE_N