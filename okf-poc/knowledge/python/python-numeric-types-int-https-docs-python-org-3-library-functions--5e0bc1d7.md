---
id: python-numeric-types-int-https-docs-python-org-3-library-functions--5e0bc1d7
type: concept
title: Numeric Types — [`int`](https://docs.python.org/3/library/functions.html#int
  "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"),
  [`complex`](https://docs.python.org/3/library/functions.html#complex "complex")[¶](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
  "Link to this heading")
description: 'There are three distinct numeric types: *integers*, *floating-point'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Numeric Types — [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`complex`](https://docs.python.org/3/library/functions.html#complex "complex")[¶](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex "Link to this heading")

There are three distinct numeric types: *integers*, *floating-point
numbers*, and *complex numbers*. In addition, Booleans are a
subtype of integers. Integers have unlimited precision. Floating-point
numbers are usually implemented using double in C; information
about the precision and internal representation of floating-point
numbers for the machine on which your program is running is available
in [`sys.float_info`](https://docs.python.org/3/library/sys.html#sys.float_info "sys.float_info"). Complex numbers have a real and imaginary
part, which are each a floating-point number. To extract these parts
from a complex number *z*, use `z.real` and `z.imag`. (The standard
library includes the additional numeric types [`fractions.Fraction`](https://docs.python.org/3/library/fractions.html#fractions.Fraction "fractions.Fraction"), for
rationals, and [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal"), for floating-point numbers with
user-definable precision.)

Numbers are created by numeric literals or as the result of built-in functions
and operators. Unadorned integer literals (including hex, octal and binary
numbers) yield integers. Numeric literals containing a decimal point or an
exponent sign yield floating-point numbers. Appending `'j'` or `'J'` to a
numeric literal yields an imaginary number (a complex number with a zero real
part) which you can add to an integer or float to get a complex number with real
and imaginary parts.

The constructors [`int()`](https://docs.python.org/3/library/functions.html#int "int"), [`float()`](https://docs.python.org/3/library/functions.html#float "float"), and
[`complex()`](https://docs.python.org/3/library/functions.html#complex "complex") can be used to produce numbers of a specific type.

Python fully supports mixed arithmetic: when a binary arithmetic operator has
operands of different built-in numeric types, the operand with the “narrower”
type is widened to that of the other:

- If both arguments are complex numbers, no conversion is performed;
- if either argument is a complex or a floating-point number, the other is
  converted to a floating-point number;
- otherwise, both must be integers and no conversion is necessary.

Arithmetic with complex and real operands is defined by the usual mathematical
formula, for example:

```
x + complex(u, v) = complex(x + u, v)
x * complex(u, v) = complex(x * u, x * v)
```

A comparison between numbers of different types behaves as though the exact
values of those numbers were being compared. [[2]](https://docs.python.org/3/library/stdtypes.html#id13)

All numeric types (except complex) support the following operations (for priorities of
the operations, see [Operator precedence](https://docs.python.org/3/reference/expressions.html#operator-summary)):

| Operation | Result | Notes | Full documentation |
| --- | --- | --- | --- |
| `x + y` | sum of *x* and *y* |  |  |
| `x - y` | difference of *x* and *y* |  |  |
| `x * y` | product of *x* and *y* |  |  |
| `x / y` | quotient of *x* and *y* |  |  |
| `x // y` | floored quotient of *x* and *y* | (1)(2) |  |
| `x % y` | remainder of `x / y` | (2) |  |
| `-x` | *x* negated |  |  |
| `+x` | *x* unchanged |  |  |
| `abs(x)` | absolute value or magnitude of *x* |  | [`abs()`](https://docs.python.org/3/library/functions.html#abs "abs") |
| `int(x)` | *x* converted to integer | (3)(6) | [`int()`](https://docs.python.org/3/library/functions.html#int "int") |
| `float(x)` | *x* converted to floating point | (4)(6) | [`float()`](https://docs.python.org/3/library/functions.html#float "float") |
| `complex(re, im)` | a c