---
id: python-module-contents-https-docs-python-org-3-library-enum-html-mo-b4fa5b54
type: concept
title: Module contents[¶](https://docs.python.org/3/library/enum.html#module-contents
  "Link to this heading")
description: '> [`EnumType`](https://docs.python.org/3/library/enum.html#enum.EnumType
  "enum.EnumType")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/enum.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Module contents[¶](https://docs.python.org/3/library/enum.html#module-contents "Link to this heading")

> [`EnumType`](https://docs.python.org/3/library/enum.html#enum.EnumType "enum.EnumType")
>
> > The `type` for Enum and its subclasses.
>
> [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum")
>
> > Base class for creating enumerated constants.
>
> [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum")
>
> > Base class for creating enumerated constants that are also
> > subclasses of [`int`](https://docs.python.org/3/library/functions.html#int "int"). ([Notes](https://docs.python.org/3/library/enum.html#notes))
>
> [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum")
>
> > Base class for creating enumerated constants that are also
> > subclasses of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"). ([Notes](https://docs.python.org/3/library/enum.html#notes))
>
> [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag")
>
> > Base class for creating enumerated constants that can be combined using
> > the bitwise operations without losing their [`Flag`](https://docs.python.org/3/library/enum.html#enum.Flag "enum.Flag") membership.
>
> [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag")
>
> > Base class for creating enumerated constants that can be combined using
> > the bitwise operators without losing their [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") membership.
> > `IntFlag` members are also subclasses of [`int`](https://docs.python.org/3/library/functions.html#int "int"). ([Notes](https://docs.python.org/3/library/enum.html#notes))
>
> [`ReprEnum`](https://docs.python.org/3/library/enum.html#enum.ReprEnum "enum.ReprEnum")
>
> > Used by [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum"), [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum"), and [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag")
> > to keep the [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") of the mixed-in type.
>
> [`EnumCheck`](https://docs.python.org/3/library/enum.html#enum.EnumCheck "enum.EnumCheck")
>
> > An enumeration with the values `CONTINUOUS`, `NAMED_FLAGS`, and
> > `UNIQUE`, for use with [`verify()`](https://docs.python.org/3/library/enum.html#enum.verify "enum.verify") to ensure various constraints
> > are met by a given enumeration.
>
> [`FlagBoundary`](https://docs.python.org/3/library/enum.html#enum.FlagBoundary "enum.FlagBoundary")
>
> > An enumeration with the values `STRICT`, `CONFORM`, `EJECT`, and
> > `KEEP` which allows for more fine-grained control over how invalid values
> > are dealt with in an enumeration.
>
> [`EnumDict`](https://docs.python.org/3/library/enum.html#enum.EnumDict "enum.EnumDict")
>
> > A subclass of [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") for use when subclassing [`EnumType`](https://docs.python.org/3/library/enum.html#enum.EnumType "enum.EnumType").
>
> [`auto`](https://docs.python.org/3/library/enum.html#enum.auto "enum.auto")
>
> > Instances are replaced with an appropriate value for Enum members.
> > [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum") defaults to the lower-cased version of the member name,
> > while other Enums default to 1 and increase from there.
>
> [`@~enum.property`](https://docs.python.org/3/library/enum.html#enum.property "enum.property")
>
> > Allows [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") members to have attributes without conflicting with
> > member names. The `value` and `name` attributes are implemented this
> > way.
>
> [`@unique`](https://docs.python.org/3/library/enum.html#enum.unique "enum.unique")
>
> > Enum class decorator that ensures only one name is bound to any on