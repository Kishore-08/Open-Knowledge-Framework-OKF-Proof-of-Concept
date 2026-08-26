---
id: python-mapping-types-dict-https-docs-python-org-3-library-stdtypes--5e0bc1d7
type: concept
title: Mapping Types — [`dict`](https://docs.python.org/3/library/stdtypes.html#dict
  "dict")[¶](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict "Link
  to this heading")
description: A [mapping](https://docs.python.org/3/glossary.html#term-mapping) object
  maps [hashable](https://docs.python.org/3/glossary.html#term-hashable) values to
  arbitrary objects.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Mapping Types — [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict")[¶](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict "Link to this heading")

A [mapping](https://docs.python.org/3/glossary.html#term-mapping) object maps [hashable](https://docs.python.org/3/glossary.html#term-hashable) values to arbitrary objects.
Mappings are mutable objects. There is currently only one standard mapping
type, the *dictionary*. (For other containers see the built-in
[`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), and [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") classes, and the
[`collections`](https://docs.python.org/3/library/collections.html#module-collections "collections: Container datatypes") module.)

A dictionary’s keys are *almost* arbitrary values. Values that are not
[hashable](https://docs.python.org/3/glossary.html#term-hashable), that is, values containing lists, dictionaries or other
mutable types (that are compared by value rather than by object identity) may
not be used as keys.
Values that compare equal (such as `1`, `1.0`, and `True`)
can be used interchangeably to index the same dictionary entry.

*class* dict(*\*\*kwargs*)[¶](https://docs.python.org/3/library/stdtypes.html#dict "Link to this definition")

*class* dict(*mapping*, */*, *\*\*kwargs*)

*class* dict(*iterable*, */*, *\*\*kwargs*)
:   Return a new dictionary initialized from an optional positional argument
    and a possibly empty set of keyword arguments.

    Dictionaries can be created by several means:

    - Use a comma-separated list of `key: value` pairs within braces:
      `{'jack': 4098, 'sjoerd': 4127}` or `{4098: 'jack', 4127: 'sjoerd'}`
    - Use a dict comprehension: `{}`, `{x: x ** 2 for x in range(10)}`
    - Use the type constructor: `dict()`,
      `dict([('foo', 100), ('bar', 200)])`, `dict(foo=100, bar=200)`

    If no positional argument is given, an empty dictionary is created.
    If a positional argument is given and it defines a `keys()` method, a
    dictionary is created by calling [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__") on the argument with
    each returned key from the method. Otherwise, the positional argument must be an
    [iterable](https://docs.python.org/3/glossary.html#term-iterable) object. Each item in the iterable must itself be an iterable
    with exactly two elements. The first element of each item becomes a key in the
    new dictionary, and the second element the corresponding value. If a key occurs
    more than once, the last value for that key becomes the corresponding value in
    the new dictionary.

    If keyword arguments are given, the keyword arguments and their values are
    added to the dictionary created from the positional argument. If a key
    being added is already present, the value from the keyword argument
    replaces the value from the positional argument.

    Dictionaries compare equal if and only if they have the same `(key,
    value)` pairs (regardless of ordering). Order comparisons (‘<’, ‘<=’, ‘>=’, ‘>’) raise
    [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"). To illustrate dictionary creation and equality,
    the following examples all return a dictionary equal to
    `{"one": 1, "two": 2, "three": 3}`:

    ```
    >>> a = dict(one=1, two=2, three=3)
    >>> b = {'one': 1, 'two': 2, 'three': 3}
    >>> c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    >>> d = dict([('two', 2), ('one', 1), ('three', 3)])
    >>> e = dict({'three': 3, 'one': 1, 'two': 2})
    >>> f = dict({'one': 1, 'three': 3}, two=2)
    >>> a == b == c == d == e == f
    True
    ```

    Providing keyword arguments as in the first example only works for keys that
    are valid Python identifiers. Otherwise, any valid keys can be used.

    Dictiona