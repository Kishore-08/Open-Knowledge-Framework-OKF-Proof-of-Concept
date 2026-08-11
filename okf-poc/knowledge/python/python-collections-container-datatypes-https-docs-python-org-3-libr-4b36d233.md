---
id: python-collections-container-datatypes-https-docs-python-org-3-libr-4b36d233
type: concept
title: '`collections` — Container datatypes[¶](https://docs.python.org/3/library/collect'
description: '**Source code:** [Lib/collections/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/collections/__init__.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `collections` — Container datatypes[¶](https://docs.python.org/3/library/collections.html#module-collections "Link to this heading")

**Source code:** [Lib/collections/\_\_init\_\_.py](https://github.com/python/cpython/tree/3.14/Lib/collections/__init__.py)

---

This module implements specialized container datatypes providing alternatives to
Python’s general purpose built-in containers, [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"),
[`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple").

|  |  |
| --- | --- |
| [`namedtuple()`](https://docs.python.org/3/library/collections.html#collections.namedtuple "collections.namedtuple") | factory function for creating tuple subclasses with named fields |
| [`deque`](https://docs.python.org/3/library/collections.html#collections.deque "collections.deque") | list-like container with fast appends and pops on either end |
| [`ChainMap`](https://docs.python.org/3/library/collections.html#collections.ChainMap "collections.ChainMap") | dict-like class for creating a single view of multiple mappings |
| [`Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "collections.Counter") | dict subclass for counting [hashable](https://docs.python.org/3/glossary.html#term-hashable) objects |
| [`OrderedDict`](https://docs.python.org/3/library/collections.html#collections.OrderedDict "collections.OrderedDict") | dict subclass that remembers the order entries were added |
| [`defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict "collections.defaultdict") | dict subclass that calls a factory function to supply missing values |
| [`UserDict`](https://docs.python.org/3/library/collections.html#collections.UserDict "collections.UserDict") | wrapper around dictionary objects for easier dict subclassing |
| [`UserList`](https://docs.python.org/3/library/collections.html#collections.UserList "collections.UserList") | wrapper around list objects for easier list subclassing |
| [`UserString`](https://docs.python.org/3/library/collections.html#collections.UserString "collections.UserString") | wrapper around string objects for easier string subclassing |