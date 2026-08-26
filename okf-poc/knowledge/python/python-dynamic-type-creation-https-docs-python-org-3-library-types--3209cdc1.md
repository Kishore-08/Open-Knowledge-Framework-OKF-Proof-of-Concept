---
id: python-dynamic-type-creation-https-docs-python-org-3-library-types--3209cdc1
type: concept
title: Dynamic Type Creation[¶](https://docs.python.org/3/library/types.html#dynamic-type-creation
  "Link to this heading")
description: types.new\_class(*name*, *bases=()*, *kwds=None*, *exec\_body=None*)[¶](https://docs.python.org/3/library/types.html#types.new_class
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/types.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Dynamic Type Creation[¶](https://docs.python.org/3/library/types.html#dynamic-type-creation "Link to this heading")

types.new\_class(*name*, *bases=()*, *kwds=None*, *exec\_body=None*)[¶](https://docs.python.org/3/library/types.html#types.new_class "Link to this definition")
:   Creates a class object dynamically using the appropriate metaclass.

    The first three arguments are the components that make up a class
    definition header: the class name, the base classes (in order), the
    keyword arguments (such as `metaclass`).

    The *exec\_body* argument is a callback that is used to populate the
    freshly created class namespace. It should accept the class namespace
    as its sole argument and update the namespace directly with the class
    contents. If no callback is provided, it has the same effect as passing
    in `lambda ns: None`.

    Added in version 3.3.

types.prepare\_class(*name*, *bases=()*, *kwds=None*)[¶](https://docs.python.org/3/library/types.html#types.prepare_class "Link to this definition")
:   Calculates the appropriate metaclass and creates the class namespace.

    The arguments are the components that make up a class definition header:
    the class name, the base classes (in order) and the keyword arguments
    (such as `metaclass`).

    The return value is a 3-tuple: `metaclass, namespace, kwds`

    *metaclass* is the appropriate metaclass, *namespace* is the
    prepared class namespace and *kwds* is an updated copy of the passed
    in *kwds* argument with any `'metaclass'` entry removed. If no *kwds*
    argument is passed in, this will be an empty dict.

    Added in version 3.3.

    Changed in version 3.6: The default value for the `namespace` element of the returned
    tuple has changed. Now an insertion-order-preserving mapping is
    used when the metaclass does not have a `__prepare__` method.

See also

[Metaclasses](https://docs.python.org/3/reference/datamodel.html#metaclasses)
:   Full details of the class creation process supported by these functions

[**PEP 3115**](https://peps.python.org/pep-3115/) - Metaclasses in Python 3000
:   Introduced the `__prepare__` namespace hook

types.resolve\_bases(*bases*)[¶](https://docs.python.org/3/library/types.html#types.resolve_bases "Link to this definition")
:   Resolve MRO entries dynamically as specified by [**PEP 560**](https://peps.python.org/pep-0560/).

    This function looks for items in *bases* that are not instances of
    [`type`](https://docs.python.org/3/library/functions.html#type "type"), and returns a tuple where each such object that has
    an [`__mro_entries__()`](https://docs.python.org/3/reference/datamodel.html#object.__mro_entries__ "object.__mro_entries__") method is replaced with an unpacked result of
    calling this method. If a *bases* item is an instance of `type`,
    or it doesn’t have an `__mro_entries__()` method, then it is included in
    the return tuple unchanged.

    Added in version 3.7.

types.get\_original\_bases(*cls*, */*)[¶](https://docs.python.org/3/library/types.html#types.get_original_bases "Link to this definition")
:   Return the tuple of objects originally given as the bases of *cls* before
    the [`__mro_entries__()`](https://docs.python.org/3/reference/datamodel.html#object.__mro_entries__ "object.__mro_entries__") method has been called on any bases
    (following the mechanisms laid out in [**PEP 560**](https://peps.python.org/pep-0560/)). This is useful for
    introspecting [Generics](https://docs.python.org/3/library/typing.html#user-defined-generics).

    For classes that have an `__orig_bases__` attribute, this
    function returns the value of `cls.__orig_bases__`.
    For classes without the `__orig_bases__` attribute,
    [`cls.__bases__`](https://docs.python.org/3/reference/datamodel.html#type.__bases__ "type.__bases__") is returned.

    Examples:

    ```
    from typing import TypeVar, Generic, NamedTuple, TypedDict

    T = TypeVar("T")
    class Foo(Generic[