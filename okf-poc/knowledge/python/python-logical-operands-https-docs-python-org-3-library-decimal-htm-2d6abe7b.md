---
id: python-logical-operands-https-docs-python-org-3-library-decimal-htm-2d6abe7b
type: concept
title: Logical operands[¶](https://docs.python.org/3/library/decimal.html#logical-operands
  "Link to this heading")
description: The [`logical_and()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_and
  "decimal.Decimal.logical_and"), [`logical_invert()`](https://docs.python.org/3/library/decimal.html#dec
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/decimal.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Logical operands[¶](https://docs.python.org/3/library/decimal.html#logical-operands "Link to this heading")

The [`logical_and()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_and "decimal.Decimal.logical_and"), [`logical_invert()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_invert "decimal.Decimal.logical_invert"), [`logical_or()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_or "decimal.Decimal.logical_or"),
and [`logical_xor()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.logical_xor "decimal.Decimal.logical_xor") methods expect their arguments to be *logical
operands*. A *logical operand* is a [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") instance whose
exponent and sign are both zero, and whose digits are all either
`0` or `1`.