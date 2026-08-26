---
id: python-examples-and-recipes-https-docs-python-org-3-library-collect-3e788865
type: concept
title: Examples and Recipes[¶](https://docs.python.org/3/library/collections.abc.html#examples-and-recipes
  "Link to this heading")
description: ABCs allow us to ask classes or instances if they provide
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/collections.abc.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Examples and Recipes[¶](https://docs.python.org/3/library/collections.abc.html#examples-and-recipes "Link to this heading")

ABCs allow us to ask classes or instances if they provide
particular functionality, for example:

```
size = None
if isinstance(myvar, collections.abc.Sized):
    size = len(myvar)
```

Several of the ABCs are also useful as mixins that make it easier to develop
classes supporting container APIs. For example, to write a class supporting
the full [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") API, it is only necessary to supply the three underlying
abstract methods: [`__contains__()`](https://docs.python.org/3/reference/datamodel.html#object.__contains__ "object.__contains__"), [`__iter__()`](https://docs.python.org/3/library/stdtypes.html#container.__iter__ "container.__iter__"), and
[`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__ "object.__len__"). The ABC supplies the remaining methods such as
`__and__()` and [`isdisjoint()`](https://docs.python.org/3/library/stdtypes.html#frozenset.isdisjoint "frozenset.isdisjoint"):

```
class ListBasedSet(collections.abc.Set):
    ''' Alternate set implementation favoring space over speed
        and not requiring the set elements to be hashable. '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)

    def __contains__(self, value):
        return value in self.elements

    def __len__(self):
        return len(self.elements)

s1 = ListBasedSet('abcdef')
s2 = ListBasedSet('defghi')
overlap = s1 & s2            # The __and__() method is supported automatically
```

Notes on using [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") and [`MutableSet`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableSet "collections.abc.MutableSet") as a mixin:

1. Since some set operations create new sets, the default mixin methods need
   a way to create new instances from an [iterable](https://docs.python.org/3/glossary.html#term-iterable). The class constructor is
   assumed to have a signature in the form `ClassName(iterable)`.
   That assumption is factored-out to an internal [`classmethod`](https://docs.python.org/3/library/functions.html#classmethod "classmethod") called
   `_from_iterable()` which calls `cls(iterable)` to produce a new set.
   If the [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") mixin is being used in a class with a different
   constructor signature, you will need to override `_from_iterable()`
   with a classmethod or regular method that can construct new instances from
   an iterable argument.
2. To override the comparisons (presumably for speed, as the
   semantics are fixed), redefine [`__le__()`](https://docs.python.org/3/reference/datamodel.html#object.__le__ "object.__le__") and
   [`__ge__()`](https://docs.python.org/3/reference/datamodel.html#object.__ge__ "object.__ge__"),
   then the other operations will automatically follow suit.
3. The [`Set`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Set "collections.abc.Set") mixin provides a `_hash()` method to compute a hash value
   for the set; however, [`__hash__()`](https://docs.python.org/3/reference/datamodel.html#object.__hash__ "object.__hash__") is not defined because not all sets
   are [hashable](https://docs.python.org/3/glossary.html#term-hashable) or immutable. To add set hashability using mixins,
   inherit from both `Set` and [`Hashable`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "collections.abc.Hashable"), then define
   `__hash__ = Set._hash`.

See also

- [OrderedSet recipe](https://code.activestate.com/recipes/5766