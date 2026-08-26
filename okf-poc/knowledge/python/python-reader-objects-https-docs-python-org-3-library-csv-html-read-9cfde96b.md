---
id: python-reader-objects-https-docs-python-org-3-library-csv-html-read-9cfde96b
type: concept
title: Reader Objects[¶](https://docs.python.org/3/library/csv.html#reader-objects
  "Link to this heading")
description: Reader objects ([`DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader
  "csv.DictReader") instances and objects returned by the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/csv.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Reader Objects[¶](https://docs.python.org/3/library/csv.html#reader-objects "Link to this heading")

Reader objects ([`DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader "csv.DictReader") instances and objects returned by the
[`reader()`](https://docs.python.org/3/library/csv.html#csv.reader "csv.reader") function) have the following public methods:

csvreader.\_\_next\_\_()[¶](https://docs.python.org/3/library/csv.html#csv.csvreader.__next__ "Link to this definition")
:   Return the next row of the reader’s iterable object as a list (if the object
    was returned from [`reader()`](https://docs.python.org/3/library/csv.html#csv.reader "csv.reader")) or a dict (if it is a [`DictReader`](https://docs.python.org/3/library/csv.html#csv.DictReader "csv.DictReader")
    instance), parsed according to the current [`Dialect`](https://docs.python.org/3/library/csv.html#csv.Dialect "csv.Dialect"). Usually you
    should call this as `next(reader)`.

Reader objects have the following public attributes:

csvreader.dialect[¶](https://docs.python.org/3/library/csv.html#csv.csvreader.dialect "Link to this definition")
:   A read-only description of the dialect in use by the parser.

csvreader.line\_num[¶](https://docs.python.org/3/library/csv.html#csv.csvreader.line_num "Link to this definition")
:   The number of lines read from the source iterator. This is not the same as the
    number of records returned, as records can span multiple lines.

DictReader objects have the following public attribute:

DictReader.fieldnames[¶](https://docs.python.org/3/library/csv.html#csv.DictReader.fieldnames "Link to this definition")
:   If not passed as a parameter when creating the object, this attribute is
    initialized upon first access or when the first record is read from the
    file.