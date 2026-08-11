---
id: python-generator-types-https-docs-python-org-3-library-stdtypes-htm-5e0bc1d7
type: concept
title: Generator Types[¶](https://docs.python.org/3/library/stdtypes.html#generator-types
  "Link to this heading")
description: Python’s [generator](https://docs.python.org/3/glossary.html#term-generator)s
  provide a convenient way to implement the iterator
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Generator Types[¶](https://docs.python.org/3/library/stdtypes.html#generator-types "Link to this heading")

Python’s [generator](https://docs.python.org/3/glossary.html#term-generator)s provide a convenient way to implement the iterator
protocol. If a container object’s [`__iter__()`](https://docs.python.org/3/reference/datamodel.html#object.__iter__ "object.__iter__") method is implemented as a
generator, it will automatically return an iterator object (technically, a
generator object) supplying the [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__iter__ "iterator.__iter__") and [`__next__()`](https://docs.python.org/3/reference/expressions.html#generator.__next__ "generator.__next__")
methods.
More information about generators can be found in [the documentation for
the yield expression](https://docs.python.org/3/reference/expressions.html#yieldexpr).