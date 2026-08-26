---
id: python-generic-alias-type-https-docs-python-org-3-library-stdtypes--5e0bc1d7
type: concept
title: Generic Alias Type[¶](https://docs.python.org/3/library/stdtypes.html#generic-alias-type
  "Link to this heading")
description: '`GenericAlias` objects are generally created by'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Generic Alias Type[¶](https://docs.python.org/3/library/stdtypes.html#generic-alias-type "Link to this heading")

`GenericAlias` objects are generally created by
[subscripting](https://docs.python.org/3/reference/expressions.html#subscriptions) a class. They are most often used with
[container classes](https://docs.python.org/3/reference/datamodel.html#sequence-types), such as [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") or
[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"). For example, `list[int]` is a `GenericAlias` object created
by subscripting the `list` class with the argument [`int`](https://docs.python.org/3/library/functions.html#int "int").
`GenericAlias` objects are intended primarily for use with
[type annotations](https://docs.python.org/3/glossary.html#term-annotation).

Note

It is generally only possible to subscript a class if the class implements
the special method [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__").

A `GenericAlias` object acts as a proxy for a [generic type](https://docs.python.org/3/glossary.html#term-generic-type),
implementing *parameterized generics*.

For a container class, the
argument(s) supplied to a [subscription](https://docs.python.org/3/reference/expressions.html#subscriptions) of the class may
indicate the type(s) of the elements an object contains. For example,
`set[bytes]` can be used in type annotations to signify a [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") in
which all the elements are of type [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").

For a class which defines [`__class_getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__class_getitem__ "object.__class_getitem__") but is not a
container, the argument(s) supplied to a subscription of the class will often
indicate the return type(s) of one or more methods defined on an object. For
example, [`regular expressions`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.") can be used on both the [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") data
type and the [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") data type:

- If `x = re.search('foo', 'foo')`, `x` will be a
  [re.Match](https://docs.python.org/3/library/re.html#match-objects) object where the return values of
  `x.group(0)` and `x[0]` will both be of type [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). We can
  represent this kind of object in type annotations with the `GenericAlias`
  `re.Match[str]`.
- If `y = re.search(b'bar', b'bar')`, (note the `b` for [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")),
  `y` will also be an instance of `re.Match`, but the return
  values of `y.group(0)` and `y[0]` will both be of type
  `bytes`. In type annotations, we would represent this
  variety of [re.Match](https://docs.python.org/3/library/re.html#match-objects) objects with `re.Match[bytes]`.

`GenericAlias` objects are instances of the class
[`types.GenericAlias`](https://docs.python.org/3/library/types.html#types.GenericAlias "types.GenericAlias"), which can also be used to create `GenericAlias`
objects directly. Specializations of user-defined [generic classes](https://docs.python.org/3/reference/compound_stmts.html#generic-classes)
may not be instances of `types.GenericAlias`, but they provide similar functionality.

T[X, Y, ...]
:   Creates a `GenericAlias` representing a type `T` parameterized by types
    *X*, *Y*, and more depending on the `T` used.
    For example, a function expecting a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") containing
    [`float`](https://docs.python.org/3/library/functions.html#float "float") elements:

    ```
    def average(values: list[float]) -> float:
        return sum(values) / len(v