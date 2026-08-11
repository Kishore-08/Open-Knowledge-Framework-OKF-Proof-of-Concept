---
id: python-utilities-and-decorators-https-docs-python-org-3-library-enu-b4fa5b54
type: concept
title: Utilities and decorators[¶](https://docs.python.org/3/library/enum.html#utilities-and-decorators
  "Link to this heading")
description: '*class* enum.auto[¶](https://docs.python.org/3/library/enum.html#enum.auto
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/enum.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Utilities and decorators[¶](https://docs.python.org/3/library/enum.html#utilities-and-decorators "Link to this heading")

*class* enum.auto[¶](https://docs.python.org/3/library/enum.html#enum.auto "Link to this definition")
:   *auto* can be used in place of a value. If used, the *Enum* machinery will
    call an [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum")’s [`_generate_next_value_()`](https://docs.python.org/3/library/enum.html#enum.Enum._generate_next_value_ "enum.Enum._generate_next_value_") to get an appropriate value.
    For `Enum` and [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") that appropriate value will be the last value plus
    one; for [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") and [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") it will be the first power-of-two greater
    than the highest value; for [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum") it will be the lower-cased version of
    the member’s name. Care must be taken if mixing *auto()* with manually
    specified values.

    *auto* instances are only resolved when at the top level of an assignment, either by
    itself or as part of a tuple:

    - `FIRST = auto()` will work (auto() is replaced with `1`);
    - `SECOND = auto(), -2` will work (auto is replaced with `2`, so `2, -2` is
      used to create the `SECOND` enum member;
    - `THREE = [auto(), -3]` will *not* work (`[<auto instance>, -3]` is used to
      create the `THREE` enum member)

    Changed in version 3.11.1: In prior versions, `auto()` had to be the only thing
    on the assignment line to work properly.

    `_generate_next_value_` can be overridden to customize the values used by
    *auto*.

    Note

    in 3.13 the default `_generate_next_value_` will always return
    the highest member value incremented by 1, and will fail if any
    member is an incompatible type.

@enum.property[¶](https://docs.python.org/3/library/enum.html#enum.property "Link to this definition")
:   A decorator similar to the built-in [`@property`](https://docs.python.org/3/library/functions.html#property "property"), but specifically for
    enumerations. It allows member attributes to have the same names as members
    themselves.

    Note

    the *property* and the member must be defined in separate classes;
    for example, the *value* and *name* attributes are defined in the
    *Enum* class, and *Enum* subclasses can define members with the
    names `value` and `name`.

    Added in version 3.11.

@enum.unique[¶](https://docs.python.org/3/library/enum.html#enum.unique "Link to this definition")
:   A [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) decorator specifically for enumerations. It searches an
    enumeration’s [`__members__`](https://docs.python.org/3/library/enum.html#enum.EnumType.__members__ "enum.EnumType.__members__"), gathering any aliases it finds; if any are
    found [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised with the details:

    ```
    >>> from enum import Enum, unique
    >>> @unique
    ... class Mistake(Enum):
    ...     ONE = 1
    ...     TWO = 2
    ...     THREE = 3
    ...     FOUR = 3
    ...
    Traceback (most recent call last):
    ...
    ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
    ```

@enum.verify[¶](https://docs.python.org/3/library/enum.html#enum.verify "Link to this definition")
:   A [`class`](https://docs.python.org/3/reference/compound_stmts.html#class) decorator specifically for enumerations. Members from
    [`EnumCheck`](https://docs.python.org/3/library/enum.html#enum.EnumCheck "enum.EnumCheck") are used to specify which constraints should be checked
    on the decorated enumeration.

    Added in version 3.11.

@enum.member[¶](https://docs.python.org/3/librar