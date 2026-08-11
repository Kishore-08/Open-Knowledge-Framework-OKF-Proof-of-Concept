---
id: python-collections-abstract-base-classes-https-docs-python-org-3-li-3e788865
type: concept
title: Collections Abstract Base Classes[¶](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes
  "Link to this heading")
description: 'The collections module offers the following [ABCs](https://docs.python.org/3/glossary.html#term-abstract-base-class):'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.abc.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Collections Abstract Base Classes[¶](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes "Link to this heading")

The collections module offers the following [ABCs](https://docs.python.org/3/glossary.html#term-abstract-base-class):

| ABC | Inherits from | Abstract Methods | Mixin Methods |
| --- | --- | --- | --- |
| [`Container`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "collections.abc.Container") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) |  | `__contains__` |  |
| [`Hashable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "collections.abc.Hashable") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) |  | `__hash__` |  |
| [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) [[2]](https://docs.python.org/3/library/collections.abc.html#id19) |  | `__iter__` |  |
| [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") | `__next__` | `__iter__` |
| [`Reversible`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible "collections.abc.Reversible") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable") | `__reversed__` |  |
| [`Generator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Generator "collections.abc.Generator") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "collections.abc.Iterator") | `send`, `throw` | `close`, `__iter__`, `__next__` |
| [`Sized`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) |  | `__len__` |  |
| [`Callable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "collections.abc.Callable") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) |  | `__call__` |  |
| [`Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection") [[1]](https://docs.python.org/3/library/collections.abc.html#id18) | [`Sized`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sized "collections.abc.Sized"), [`Iterable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "collections.abc.Iterable"), [`Container`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Container "collections.abc.Container") | `__contains__`, `__iter__`, `__len__` |  |
| [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") | [`Reversible`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Reversible "collections.abc.Reversible"), [`Collection`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Collection "collections.abc.Collection") | `__getitem__`, `__len__` | `__contains__`, `__iter__`, `__reversed__`, `index`, and `count` |
| [`MutableSequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSequence "collections.abc.MutableSequence") | [`Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence") | `__getitem__`, `__setitem__`, `__delitem__`, `__len__`, `insert` | Inherited [`Sequence`](https://docs.python.org/3/library/