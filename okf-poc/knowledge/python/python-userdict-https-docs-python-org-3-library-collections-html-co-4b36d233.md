---
id: python-userdict-https-docs-python-org-3-library-collections-html-co-4b36d233
type: concept
title: '[`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict
  "collections.UserDict") objects[¶](https://docs.python.org/3/library/collections.html#userdict-objects
  "Link to this heading")'
description: The class, [`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict
  "collections.UserDict") acts as a wrapper around dictionary objects.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## [`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict "collections.UserDict") objects[¶](https://docs.python.org/3/library/collections.html#userdict-objects "Link to this heading")

The class, [`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict "collections.UserDict") acts as a wrapper around dictionary objects.
The need for this class has been partially supplanted by the ability to
subclass directly from [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"); however, this class can be easier
to work with because the underlying dictionary is accessible as an
attribute.

*class* collections.UserDict(*\*\*kwargs*)[¶](https://docs.python.org/3/library/collections.html#collections.UserDict "Link to this definition")

*class* collections.UserDict(*mapping*, */*, *\*\*kwargs*)

*class* collections.UserDict(*iterable*, */*, *\*\*kwargs*)
:   Class that simulates a dictionary. The instance’s contents are kept in a
    regular dictionary, which is accessible via the [`data`](https://docs.python.org/3/library/collections.html#collections.UserDict.data "collections.UserDict.data") attribute of
    `UserDict` instances. If arguments are provided, they are used to
    initialize `data`, like a regular dictionary.

    In addition to supporting the methods and operations of mappings,
    `UserDict` instances provide the following attribute:

    data[¶](https://docs.python.org/3/library/collections.html#collections.UserDict.data "Link to this definition")
    :   A real dictionary used to store the contents of the `UserDict`
        class.