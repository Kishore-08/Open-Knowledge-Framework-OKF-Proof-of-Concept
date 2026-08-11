---
id: python-data-types-https-docs-python-org-3-library-enum-html-data-ty-b4fa5b54
type: concept
title: Data types[¶](https://docs.python.org/3/library/enum.html#data-types "Link
  to this heading")
description: '*class* enum.EnumType[¶](https://docs.python.org/3/library/enum.html#enum.EnumType
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/enum.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Data types[¶](https://docs.python.org/3/library/enum.html#data-types "Link to this heading")

*class* enum.EnumType[¶](https://docs.python.org/3/library/enum.html#enum.EnumType "Link to this definition")
:   *EnumType* is the [metaclass](https://docs.python.org/3/glossary.html#term-metaclass) for *enum* enumerations. It is possible
    to subclass *EnumType* – see [Subclassing EnumType](https://docs.python.org/3/howto/enum.html#enumtype-examples)
    for details.

    `EnumType` is responsible for setting the correct `__repr__()`,
    `__str__()`, `__format__()`, and `__reduce__()` methods on the
    final *enum*, as well as creating the enum members, properly handling
    duplicates, providing iteration over the enum class, etc.

    Added in version 3.11: Before 3.11 `EnumType` was called `EnumMeta`, which is still available as an alias.

    \_\_call\_\_(*cls*, *value*, *names=None*, *\**, *module=None*, *qualname=None*, *type=None*, *start=1*, *boundary=None*)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__call__ "Link to this definition")
    :   This method is called in two different ways:

        - to look up an existing member:

          > cls:
          > :   The enum class being called.
          >
          > value:
          > :   The value to lookup.
        - to use the `cls` enum to create a new enum (only if the existing enum
          does not have any members):

          > cls:
          > :   The enum class being called.
          >
          > value:
          > :   The name of the new Enum to create.
          >
          > names:
          > :   The names/values of the members for the new Enum.
          >
          > module:
          > :   The name of the module the new Enum is created in.
          >
          > qualname:
          > :   The actual location in the module where this Enum can be found.
          >
          > type:
          > :   A mix-in type for the new Enum.
          >
          > start:
          > :   The first integer value for the Enum (used by [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto")).
          >
          > boundary:
          > :   How to handle out-of-range values from bit operations ([`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") only).

    \_\_contains\_\_(*cls*, *member*)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__contains__ "Link to this definition")
    :   Returns `True` if member belongs to the `cls`:

        ```
        >>> some_var = Color.RED
        >>> some_var in Color
        True
        >>> Color.RED.value in Color
        True
        ```

        Changed in version 3.12: Before Python 3.12, a `TypeError` is raised if a
        non-Enum-member is used in a containment check.

    \_\_dir\_\_(*cls*)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__dir__ "Link to this definition")
    :   Returns `['__class__', '__doc__', '__members__', '__module__']` and the
        names of the members in *cls*:

        ```
        >>> dir(Color)
        ['BLUE', 'GREEN', 'RED', '__class__', '__contains__', '__doc__', '__getitem__', '__init_subclass__', '__iter__', '__len__', '__members__', '__module__', '__name__', '__qualname__']
        ```

    \_\_getitem\_\_(*cls*, *name*)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__getitem__ "Link to this definition")
    :   Returns the Enum member in *cls* matching *name*, or raises a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError"):

        ```
        >>> Color['BLUE']
        <Color.BLUE: 3>
        ```

    \_\_iter\_\_(*cls*)[¶](https://docs.python.org/3/library/enum.html#enum.EnumType.__iter__ "Link to this definition")
    :   Returns each member in *cls* in definition order:

        ```
        >>> list(Color)
        [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
        ```

    \_\_len\_\_(*cls*)[¶](https://docs.python.org/3/library/enum.ht