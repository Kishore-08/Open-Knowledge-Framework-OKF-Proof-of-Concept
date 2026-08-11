---
id: python-iterator-types-https-docs-python-org-3-library-stdtypes-html-5e0bc1d7
type: concept
title: Iterator Types[¶](https://docs.python.org/3/library/stdtypes.html#iterator-types
  "Link to this heading")
description: Python supports a concept of iteration over containers. This is implemented
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Iterator Types[¶](https://docs.python.org/3/library/stdtypes.html#iterator-types "Link to this heading")

Python supports a concept of iteration over containers. This is implemented
using two distinct methods; these are used to allow user-defined classes to
support iteration. Sequences, described below in more detail, always support
the iteration methods.

One method needs to be defined for container objects to provide [iterable](https://docs.python.org/3/glossary.html#term-iterable)
support:

container.\_\_iter\_\_()[¶](https://docs.python.org/3/library/stdtypes.html#container.__iter__ "Link to this definition")
:   Return an [iterator](https://docs.python.org/3/glossary.html#term-iterator) object. The object is required to support the
    iterator protocol described below. If a container supports different types
    of iteration, additional methods can be provided to specifically request
    iterators for those iteration types. (An example of an object supporting
    multiple forms of iteration would be a tree structure which supports both
    breadth-first and depth-first traversal.) This method corresponds to the
    [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter") slot of the type structure for Python
    objects in the Python/C API.

The iterator objects themselves are required to support the following two
methods, which together form the *iterator protocol*:

iterator.\_\_iter\_\_()[¶](https://docs.python.org/3/library/stdtypes.html#iterator.__iter__ "Link to this definition")
:   Return the [iterator](https://docs.python.org/3/glossary.html#term-iterator) object itself. This is required to allow both
    containers and iterators to be used with the [`for`](https://docs.python.org/3/reference/compound_stmts.html#for) and
    [`in`](https://docs.python.org/3/reference/expressions.html#in) statements. This method corresponds to the
    [`tp_iter`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iter "PyTypeObject.tp_iter") slot of the type structure for Python
    objects in the Python/C API.

iterator.\_\_next\_\_()[¶](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "Link to this definition")
:   Return the next item from the [iterator](https://docs.python.org/3/glossary.html#term-iterator). If there are no further
    items, raise the [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration") exception. This method corresponds to
    the [`tp_iternext`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_iternext "PyTypeObject.tp_iternext") slot of the type structure for
    Python objects in the Python/C API.

Python defines several iterator objects to support iteration over general and
specific sequence types, dictionaries, and other more specialized forms. The
specific types are not important beyond their implementation of the iterator
protocol.

Once an iterator’s [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") method raises
[`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration"), it must continue to do so on subsequent calls.
Implementations that do not obey this property are deemed broken.