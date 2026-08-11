---
id: python-userstring-https-docs-python-org-3-library-collections-html--4b36d233
type: concept
title: '[`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString
  "collections.UserString") objects[¶](https://docs.python.org/3/library/collections.html#userstring-objects
  "Link to this heading")'
description: The class, [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString
  "collections.UserString") acts as a wrapper around string objects.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString "collections.UserString") objects[¶](https://docs.python.org/3/library/collections.html#userstring-objects "Link to this heading")

The class, [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString "collections.UserString") acts as a wrapper around string objects.
The need for this class has been partially supplanted by the ability to
subclass directly from [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"); however, this class can be easier
to work with because the underlying string is accessible as an
attribute.

*class* collections.UserString(*seq*)[¶](https://docs.python.org/3/library/collections.html#collections.UserString "Link to this definition")
:   Class that simulates a string object. The instance’s
    content is kept in a regular string object, which is accessible via the
    [`data`](https://docs.python.org/3/library/collections.html#collections.UserString.data "collections.UserString.data") attribute of `UserString` instances. The instance’s
    contents are initially set to a copy of *seq*. The *seq* argument can
    be any object which can be converted into a string using the built-in
    [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") function.

    In addition to supporting the methods and operations of strings,
    `UserString` instances provide the following attribute:

    data[¶](https://docs.python.org/3/library/collections.html#collections.UserString.data "Link to this definition")
    :   A real [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") object used to store the contents of the
        `UserString` class.

    Changed in version 3.5: New methods `__getnewargs__`, `__rmod__`, `casefold`,
    `format_map`, `isprintable`, and `maketrans`.