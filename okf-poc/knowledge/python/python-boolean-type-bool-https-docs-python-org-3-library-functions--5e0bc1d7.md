---
id: python-boolean-type-bool-https-docs-python-org-3-library-functions--5e0bc1d7
type: concept
title: Boolean Type - [`bool`](https://docs.python.org/3/library/functions.html#bool
  "bool")[¶](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool "Link
  to this heading")
description: Booleans represent truth values. The [`bool`](https://docs.python.org/3/library/functions.html#bool
  "bool") type has exactly two
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Boolean Type - [`bool`](https://docs.python.org/3/library/functions.html#bool "bool")[¶](https://docs.python.org/3/library/stdtypes.html#boolean-type-bool "Link to this heading")

Booleans represent truth values. The [`bool`](https://docs.python.org/3/library/functions.html#bool "bool") type has exactly two
constant instances: `True` and `False`.

The built-in function [`bool()`](https://docs.python.org/3/library/functions.html#bool "bool") converts any value to a boolean, if the
value can be interpreted as a truth value (see section [Truth Value Testing](https://docs.python.org/3/library/stdtypes.html#truth) above).

For logical operations, use the [boolean operators](https://docs.python.org/3/library/stdtypes.html#boolean) `and`,
`or` and `not`.
When applying the bitwise operators `&`, `|`, `^` to two booleans, they
return a bool equivalent to the logical operations “and”, “or”, “xor”. However,
the logical operators `and`, `or` and `!=` should be preferred
over `&`, `|` and `^`.

Deprecated since version 3.12: The use of the bitwise inversion operator `~` is deprecated and will
raise an error in Python 3.16.

[`bool`](https://docs.python.org/3/library/functions.html#bool "bool") is a subclass of [`int`](https://docs.python.org/3/library/functions.html#int "int") (see [Numeric Types — int, float, complex](https://docs.python.org/3/library/stdtypes.html#typesnumeric)). In
many numeric contexts, `False` and `True` behave like the integers 0 and 1, respectively.
However, relying on this is discouraged; explicitly convert using [`int()`](https://docs.python.org/3/library/functions.html#int "int")
instead.