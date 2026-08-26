---
id: python-module-contents-https-docs-python-org-3-library-csv-html-mod-9cfde96b
type: concept
title: Module Contents[¶](https://docs.python.org/3/library/csv.html#module-contents
  "Link to this heading")
description: 'The `csv` module defines the following functions:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/csv.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Module Contents[¶](https://docs.python.org/3/library/csv.html#module-contents "Link to this heading")

The `csv` module defines the following functions:

csv.reader(*csvfile*, */*, *dialect='excel'*, *\*\*fmtparams*)[¶](https://docs.python.org/3/library/csv.html#csv.reader "Link to this definition")
:   Return a [reader object](https://docs.python.org/3/library/csv.html#reader-objects) that will process
    lines from the given *csvfile*. A csvfile must be an iterable of
    strings, each in the reader’s defined csv format.
    A csvfile is most commonly a file-like object or list.
    If *csvfile* is a file object,
    it should be opened with `newline=''`. [[1]](https://docs.python.org/3/library/csv.html#id4) An optional
    *dialect* parameter can be given which is used to define a set of parameters
    specific to a particular CSV dialect. It may be an instance of a subclass of
    the [`Dialect`](https://docs.python.org/3/library/csv.html#csv.Dialect "csv.Dialect") class or one of the strings returned by the
    [`list_dialects()`](https://docs.python.org/3/library/csv.html#csv.list_dialects "csv.list_dialects") function. The other optional *fmtparams* keyword arguments
    can be given to override individual formatting parameters in the current
    dialect. For full details about the dialect and formatting parameters, see
    section [Dialects and Formatting Parameters](https://docs.python.org/3/library/csv.html#csv-fmt-params).

    Each row read from the csv file is returned as a list of strings. No
    automatic data type conversion is performed unless the [`QUOTE_NONNUMERIC`](https://docs.python.org/3/library/csv.html#csv.QUOTE_NONNUMERIC "csv.QUOTE_NONNUMERIC") format
    option is specified (in which case unquoted fields are transformed into floats).

    A short usage example:

    ```
    >>> import csv
    >>> with open('eggs.csv', newline='') as csvfile:
    ...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    ...     for row in spamreader:
    ...         print(', '.join(row))
    Spam, Spam, Spam, Spam, Spam, Baked Beans
    Spam, Lovely Spam, Wonderful Spam
    ```

    where `eggs.csv` contains:

    ```
    Spam Spam Spam Spam Spam |Baked Beans|
    Spam |Lovely Spam| |Wonderful Spam|
    ```

csv.writer(*csvfile*, */*, *dialect='excel'*, *\*\*fmtparams*)[¶](https://docs.python.org/3/library/csv.html#csv.writer "Link to this definition")
:   Return a writer object responsible for converting the user’s data into delimited
    strings on the given file-like object. *csvfile* can be any object with a
    [`write()`](https://docs.python.org/3/library/io.html#io.TextIOBase.write "io.TextIOBase.write") method. If *csvfile* is a file object, it should be opened with
    `newline=''` [[1]](https://docs.python.org/3/library/csv.html#id4). An optional *dialect*
    parameter can be given which is used to define a set of parameters specific to a
    particular CSV dialect. It may be an instance of a subclass of the
    [`Dialect`](https://docs.python.org/3/library/csv.html#csv.Dialect "csv.Dialect") class or one of the strings returned by the
    [`list_dialects()`](https://docs.python.org/3/library/csv.html#csv.list_dialects "csv.list_dialects") function. The other optional *fmtparams* keyword arguments
    can be given to override individual formatting parameters in the current
    dialect. For full details about dialects and formatting parameters, see
    the [Dialects and Formatting Parameters](https://docs.python.org/3/library/csv.html#csv-fmt-params) section. To make it
    as easy as possible to interface with modules which implement the DB API, the
    value [`None`](https://docs.python.org/3/library/constants.html#None "None") is written as the empty string. While this isn’t a
    reversible transformation, it makes it easier to dump SQL NULL data values to
    CSV files without preprocessing the data returned from a `cursor.fetch*` call.
    All other non-string data are stringified