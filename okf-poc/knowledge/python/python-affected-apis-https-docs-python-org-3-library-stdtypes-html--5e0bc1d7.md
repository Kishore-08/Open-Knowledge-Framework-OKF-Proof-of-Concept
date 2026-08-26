---
id: python-affected-apis-https-docs-python-org-3-library-stdtypes-html--5e0bc1d7
type: concept
title: Affected APIs[¶](https://docs.python.org/3/library/stdtypes.html#affected-apis
  "Link to this heading")
description: The limitation only applies to potentially slow conversions between [`int`](https://docs.python.org/3/library/functions.html#int
  "int")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Affected APIs[¶](https://docs.python.org/3/library/stdtypes.html#affected-apis "Link to this heading")

The limitation only applies to potentially slow conversions between [`int`](https://docs.python.org/3/library/functions.html#int "int")
and [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes"):

- `int(string)` with default base 10.
- `int(string, base)` for all bases that are not a power of 2.
- `str(integer)`.
- `repr(integer)`.
- any other string conversion to base 10, for example `f"{integer}"`,
  `"{}".format(integer)`, or `b"%d" % integer`.

The limitations do not apply to functions with a linear algorithm:

- `int(string, base)` with base 2, 4, 8, 16, or 32.
- [`int.from_bytes()`](https://docs.python.org/3/library/stdtypes.html#int.from_bytes "int.from_bytes") and [`int.to_bytes()`](https://docs.python.org/3/library/stdtypes.html#int.to_bytes "int.to_bytes").
- [`hex()`](https://docs.python.org/3/library/functions.html#hex "hex"), [`oct()`](https://docs.python.org/3/library/functions.html#oct "oct"), [`bin()`](https://docs.python.org/3/library/functions.html#bin "bin").
- [Format specification mini-language](https://docs.python.org/3/library/string.html#formatspec) for hex, octal, and binary numbers.
- [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") to [`float`](https://docs.python.org/3/library/functions.html#float "float").
- [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") to [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal").