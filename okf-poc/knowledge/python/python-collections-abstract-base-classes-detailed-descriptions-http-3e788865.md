---
id: python-collections-abstract-base-classes-detailed-descriptions-http-3e788865
type: concept
title: Collections Abstract Base Classes – Detailed Descriptions[¶](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes-detailed-descriptions
  "Link to this heading")
description: '*class* collections.abc.Container[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.abc.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Collections Abstract Base Classes – Detailed Descriptions[¶](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes-detailed-descriptions "Link to this heading")

*class* collections.abc.Container[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "Link to this definition")
:   ABC for classes that provide the [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__") method.

*class* collections.abc.Hashable[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "Link to this definition")
:   ABC for classes that provide the [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__") method.

*class* collections.abc.Sized[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "Link to this definition")
:   ABC for classes that provide the [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__") method.

*class* collections.abc.Callable[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "Link to this definition")
:   ABC for classes that provide the [`__call__()`](https://docs.python.org/3/reference/datamodel.html#object.__call__ "object.__call__") method.

    See [Annotating callable objects](https://docs.python.org/3/library/typing.html#annotating-callables) for details on how to use
    `Callable` in type annotations.

*class* collections.abc.Iterable[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "Link to this definition")
:   ABC for classes that provide the [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#container.__iter__ "container.__iter__") method.

    Checking `isinstance(obj, Iterable)` detects classes that are registered
    as `Iterable` or that have an [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#container.__iter__ "container.__iter__") method,
    but it does
    not detect classes that iterate with the [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__") method.
    The only reliable way to determine whether an object is [iterable](https://docs.python.org/3/glossary.html#term-iterable)
    is to call `iter(obj)`.

*class* collections.abc.Collection[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "Link to this definition")
:   ABC for sized iterable container classes.

    Added in version 3.6.

*class* collections.abc.Iterator[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "Link to this definition")
:   ABC for classes that provide the [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__iter__ "iterator.__iter__") and
    [`__next__()`](https://docs.python.org/3/library/stdtypes.html#iterator.__next__ "iterator.__next__") methods. See also the definition of
    [iterator](https://docs.python.org/3/glossary.html#term-iterator).

*class* collections.abc.Reversible[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible "Link to this definition")
:   ABC for iterable classes that also provide the [`__reversed__()`](https://docs.python.org/3/reference/datamodel.html#object.__reversed__ "object.__reversed__")
    method.

    Added in version 3.6.

*class* collections.abc.Generator[¶](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "Link to this definition")
:   ABC for [generator](https://docs.python.org/3/glossary.html#term-generator) classes that implement the protocol defined in
    [**PEP 342**](https://peps.python.org/pep-0342/) that extends [iterators](https://docs.python.org/3/glossary.html#term-iterator) with the
    [`send()`](https://docs.python.org/3/reference/expressions.html#generator.send "generator.send"),
    [`throw()`](https://docs