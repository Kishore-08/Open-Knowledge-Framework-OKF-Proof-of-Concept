---
id: python-supported-dunder-names-https-docs-python-org-3-library-enum--b4fa5b54
type: concept
title: Supported `__dunder__` names[¶](https://docs.python.org/3/library/enum.html#supported-dunder-names
  "Link to this heading")
description: '[`__members__`](https://docs.python.org/3/library/enum.html#enum.EnumType.__members__
  "enum.EnumType.__members__") is a read-only ordered mapping of `member_name`:`member`'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/enum.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Supported `__dunder__` names[¶](https://docs.python.org/3/library/enum.html#supported-dunder-names "Link to this heading")

[`__members__`](https://docs.python.org/3/library/enum.html#enum.EnumType.__members__ "enum.EnumType.__members__") is a read-only ordered mapping of `member_name`:`member`
items. It is only available on the class.

[`__new__()`](https://docs.python.org/3/library/enum.html#enum.Enum.__new__ "enum.Enum.__new__"), if specified, must create and return the enum members;
it is also a very good idea to set the member’s [`_value_`](https://docs.python.org/3/library/enum.html#enum.Enum._value_ "enum.Enum._value_") appropriately.
Once all the members are created it is no longer used.