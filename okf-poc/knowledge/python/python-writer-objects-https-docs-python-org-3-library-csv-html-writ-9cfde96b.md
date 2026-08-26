---
id: python-writer-objects-https-docs-python-org-3-library-csv-html-writ-9cfde96b
type: concept
title: Writer Objects[¶](https://docs.python.org/3/library/csv.html#writer-objects
  "Link to this heading")
description: '[`writer`](https://docs.python.org/3/library/csv.html#csv.writer "csv.writer")
  objects ([`DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter
  "csv.DictWriter") instances and objects'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/csv.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Writer Objects[¶](https://docs.python.org/3/library/csv.html#writer-objects "Link to this heading")

[`writer`](https://docs.python.org/3/library/csv.html#csv.writer "csv.writer") objects ([`DictWriter`](https://docs.python.org/3/library/csv.html#csv.DictWriter "csv.DictWriter") instances and objects returned by
the [`writer()`](https://docs.python.org/3/library/csv.html#csv.writer "csv.writer") function) have the following public methods. A *row* must be
an iterable of strings or numbers for `writer` objects and a dictionary
mapping fieldnames to strings or numbers (by passing them through [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str")
first) for `DictWriter` objects. Note that complex numbers are written
out surrounded by parens. This may cause some problems for other programs which
read CSV files (assuming they support complex numbers at all).

csvwriter.writerow(*row*, */*)[¶](https://docs.python.org/3/library/csv.html#csv.csvwriter.writerow "Link to this definition")
:   Write the *row* parameter to the writer’s file object, formatted according
    to the current [`Dialect`](https://docs.python.org/3/library/csv.html#csv.Dialect "csv.Dialect"). Return the return value of the call to the
    *write* method of the underlying file object.

    Changed in version 3.5: Added support of arbitrary iterables.

csvwriter.writerows(*rows*, */*)[¶](https://docs.python.org/3/library/csv.html#csv.csvwriter.writerows "Link to this definition")
:   Write all elements in *rows* (an iterable of *row* objects as described
    above) to the writer’s file object, formatted according to the current
    dialect.

Writer objects have the following public attribute:

csvwriter.dialect[¶](https://docs.python.org/3/library/csv.html#csv.csvwriter.dialect "Link to this definition")
:   A read-only description of the dialect in use by the writer.

DictWriter objects have the following public method:

DictWriter.writeheader()[¶](https://docs.python.org/3/library/csv.html#csv.DictWriter.writeheader "Link to this definition")
:   Write a row with the field names (as specified in the constructor) to
    the writer’s file object, formatted according to the current dialect. Return
    the return value of the [`csvwriter.writerow()`](https://docs.python.org/3/library/csv.html#csv.csvwriter.writerow "csv.csvwriter.writerow") call used internally.

    Added in version 3.2.

    Changed in version 3.8: `writeheader()` now also returns the value returned by
    the [`csvwriter.writerow()`](https://docs.python.org/3/library/csv.html#csv.csvwriter.writerow "csv.csvwriter.writerow") method it uses internally.