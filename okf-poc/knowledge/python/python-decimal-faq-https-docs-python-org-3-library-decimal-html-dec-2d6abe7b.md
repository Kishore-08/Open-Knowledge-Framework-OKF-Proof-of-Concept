---
id: python-decimal-faq-https-docs-python-org-3-library-decimal-html-dec-2d6abe7b
type: concept
title: Decimal FAQ[¶](https://docs.python.org/3/library/decimal.html#decimal-faq "Link
  to this heading")
description: 'Q: It is cumbersome to type `decimal.Decimal(''1234.5'')`. Is there
  a way to'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/decimal.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Decimal FAQ[¶](https://docs.python.org/3/library/decimal.html#decimal-faq "Link to this heading")

Q: It is cumbersome to type `decimal.Decimal('1234.5')`. Is there a way to
minimize typing when using the interactive interpreter?

A: Some users abbreviate the constructor to just a single letter:

```
>>> D = decimal.Decimal
>>> D('1.23') + D('3.45')
Decimal('4.68')
```

Q: In a fixed-point application with two decimal places, some inputs have many
places and need to be rounded. Others are not supposed to have excess digits
and need to be validated. What methods should be used?

A: The [`quantize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "decimal.Decimal.quantize") method rounds to a fixed number of decimal places. If
the [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact") trap is set, it is also useful for validation:

```
>>> TWOPLACES = Decimal(10) ** -2       # same as Decimal('0.01')
```

```
>>> # Round to two places
>>> Decimal('3.214').quantize(TWOPLACES)
Decimal('3.21')
```

```
>>> # Validate that a number does not exceed two places
>>> Decimal('3.21').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Decimal('3.21')
```

```
>>> Decimal('3.214').quantize(TWOPLACES, context=Context(traps=[Inexact]))
Traceback (most recent call last):
   ...
Inexact: None
```

Q: Once I have valid two place inputs, how do I maintain that invariant
throughout an application?

A: Some operations like addition, subtraction, and multiplication by an integer
will automatically preserve fixed point. Others operations, like division and
non-integer multiplication, will change the number of decimal places and need to
be followed-up with a [`quantize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "decimal.Decimal.quantize") step:

```
>>> a = Decimal('102.72')           # Initial fixed-point values
>>> b = Decimal('3.17')
>>> a + b                           # Addition preserves fixed-point
Decimal('105.89')
>>> a - b
Decimal('99.55')
>>> a * 42                          # So does integer multiplication
Decimal('4314.24')
>>> (a * b).quantize(TWOPLACES)     # Must quantize non-integer multiplication
Decimal('325.62')
>>> (b / a).quantize(TWOPLACES)     # And quantize division
Decimal('0.03')
```

In developing fixed-point applications, it is convenient to define functions
to handle the [`quantize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.quantize "decimal.Decimal.quantize") step:

```
>>> def mul(x, y, fp=TWOPLACES):
...     return (x * y).quantize(fp)
...
>>> def div(x, y, fp=TWOPLACES):
...     return (x / y).quantize(fp)
```

```
>>> mul(a, b)                       # Automatically preserve fixed-point
Decimal('325.62')
>>> div(b, a)
Decimal('0.03')
```

Q: There are many ways to express the same value. The numbers `200`,
`200.000`, `2E2`, and `.02E+4` all have the same value at
various precisions. Is there a way to transform them to a single recognizable
canonical value?

A: The [`normalize()`](https://docs.python.org/3/library/decimal.html#decimal.Decimal.normalize "decimal.Decimal.normalize") method maps all equivalent values to a single
representative:

```
>>> values = map(Decimal, '200 200.000 2E2 .02E+4'.split())
>>> [v.normalize() for v in values]
[Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2'), Decimal('2E+2')]
```

Q: When does rounding occur in a computation?

A: It occurs *after* the computation. The philosophy of the decimal
specification is that numbers are considered exact and are created
independent of the current context. They can even have greater
precision than current context. Computations process with those
exact inputs and then rounding (or other context operations) is
applied to the *result* of the computation:

```
>>> getcontext().prec = 5
>>> pi = Decimal('3.1415926535')   # More than 5 digits
>>> pi                             # All digits are retained
Decimal('3.1415926535')
>>>