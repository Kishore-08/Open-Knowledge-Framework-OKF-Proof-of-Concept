---
id: python-notes-https-docs-python-org-3-library-enum-html-notes-link-t-b4fa5b54
type: concept
title: Notes[¶](https://docs.python.org/3/library/enum.html#notes "Link to this heading")
description: '[`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum
  "enum.IntEnum"), [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum
  "enum.StrEnum"), and [`IntFlag`](https://docs'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/enum.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Notes[¶](https://docs.python.org/3/library/enum.html#notes "Link to this heading")

[`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum"), [`StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum "enum.StrEnum"), and [`IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag")

> These three enum types are designed to be drop-in replacements for existing
> integer- and string-based values; as such, they have extra limitations:
>
> - `__str__` uses the value and not the name of the enum member
> - `__format__`, because it uses `__str__`, will also use the value of
>   the enum member instead of its name
>
> If you do not need/want those limitations, you can either create your own
> base class by mixing in the `int` or `str` type yourself:
>
> ```
> >>> from enum import Enum
> >>> class MyIntEnum(int, Enum):
> ...     pass
> ```
>
> or you can reassign the appropriate [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str"), etc., in your enum:
>
> ```
> >>> from enum import Enum, IntEnum
> >>> class MyIntEnum(IntEnum):
> ...     __str__ = Enum.__str__
> ```