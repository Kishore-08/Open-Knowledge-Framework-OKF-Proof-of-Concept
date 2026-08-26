---
id: python-bitwise-operations-on-integer-types-https-docs-python-org-3--5e0bc1d7
type: concept
title: Bitwise Operations on Integer Types[¶](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
  "Link to this heading")
description: Bitwise operations only make sense for integers. The result of bitwise
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Bitwise Operations on Integer Types[¶](https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types "Link to this heading")

Bitwise operations only make sense for integers. The result of bitwise
operations is calculated as though carried out in two’s complement with an
infinite number of sign bits.

The priorities of the binary bitwise operations are all lower than the numeric
operations and higher than the comparisons; the unary operation `~` has the
same priority as the other unary numeric operations (`+` and `-`).

This table lists the bitwise operations sorted in ascending priority:

| Operation | Result | Notes |
| --- | --- | --- |
| `x | y` | bitwise *or* of *x* and *y* | (4) |
| `x ^ y` | bitwise *exclusive or* of *x* and *y* | (4) |
| `x & y` | bitwise *and* of *x* and *y* | (4) |
| `x << n` | *x* shifted left by *n* bits | (1)(2) |
| `x >> n` | *x* shifted right by *n* bits | (1)(3) |
| `~x` | the bits of *x* inverted |  |

Notes:

1. Negative shift counts are illegal and cause a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") to be raised.
2. A left shift by *n* bits is equivalent to multiplication by `pow(2, n)`.
3. A right shift by *n* bits is equivalent to floor division by `pow(2, n)`.
4. Performing these calculations with at least one extra sign extension bit in
   a finite two’s complement representation (a working bit-width of
   `1 + max(x.bit_length(), y.bit_length())` or more) is sufficient to get the
   same result as if there were an infinite number of sign bits.