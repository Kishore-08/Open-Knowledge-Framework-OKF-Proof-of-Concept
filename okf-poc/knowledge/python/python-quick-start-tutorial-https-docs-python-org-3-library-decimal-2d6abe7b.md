---
id: python-quick-start-tutorial-https-docs-python-org-3-library-decimal-2d6abe7b
type: concept
title: Quick-start tutorial[¶](https://docs.python.org/3/library/decimal.html#quick-start-tutorial
  "Link to this heading")
description: The usual start to using decimals is importing the module, viewing the
  current
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/decimal.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Quick-start tutorial[¶](https://docs.python.org/3/library/decimal.html#quick-start-tutorial "Link to this heading")

The usual start to using decimals is importing the module, viewing the current
context with [`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") and, if necessary, setting new values for
precision, rounding, or enabled traps:

```
>>> from decimal import *
>>> getcontext()
Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999,
        capitals=1, clamp=0, flags=[], traps=[Overflow, DivisionByZero,
        InvalidOperation])

>>> getcontext().prec = 7       # Set a new precision
```

Decimal instances can be constructed from integers, strings, floats, or tuples.
Construction from an integer or a float performs an exact conversion of the
value of that integer or float. Decimal numbers include special values such as
`NaN` which stands for “Not a number”, positive and negative
`Infinity`, and `-0`:

```
>>> getcontext().prec = 28
>>> Decimal(10)
Decimal('10')
>>> Decimal('3.14')
Decimal('3.14')
>>> Decimal(3.14)
Decimal('3.140000000000000124344978758017532527446746826171875')
>>> Decimal((0, (3, 1, 4), -2))
Decimal('3.14')
>>> Decimal(str(2.0 ** 0.5))
Decimal('1.4142135623730951')
>>> Decimal(2) ** Decimal('0.5')
Decimal('1.414213562373095048801688724')
>>> Decimal('NaN')
Decimal('NaN')
>>> Decimal('-Infinity')
Decimal('-Infinity')
```

If the [`FloatOperation`](https://docs.python.org/3/library/decimal.html#decimal.FloatOperation "decimal.FloatOperation") signal is trapped, accidental mixing of
decimals and floats in constructors or ordering comparisons raises
an exception:

```
>>> c = getcontext()
>>> c.traps[FloatOperation] = True
>>> Decimal(3.14)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
>>> Decimal('3.5') < 3.7
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.FloatOperation: [<class 'decimal.FloatOperation'>]
>>> Decimal('3.5') == 3.5
True
```

Added in version 3.3.

The significance of a new Decimal is determined solely by the number of digits
input. Context precision and rounding only come into play during arithmetic
operations.

```
>>> getcontext().prec = 6
>>> Decimal('3.0')
Decimal('3.0')
>>> Decimal('3.1415926535')
Decimal('3.1415926535')
>>> Decimal('3.1415926535') + Decimal('2.7182818285')
Decimal('5.85987')
>>> getcontext().rounding = ROUND_UP
>>> Decimal('3.1415926535') + Decimal('2.7182818285')
Decimal('5.85988')
```

If the internal limits of the C version are exceeded, constructing
a decimal raises [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation"):

```
>>> Decimal("1e9999999999999999999")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
decimal.InvalidOperation: [<class 'decimal.InvalidOperation'>]
```

Changed in version 3.3.

Decimals interact well with much of the rest of Python. Here is a small decimal
floating-point flying circus:

```
>>> data = list(map(Decimal, '1.34 1.87 3.45 2.35 1.00 0.03 9.25'.split()))
>>> max(data)
Decimal('9.25')
>>> min(data)
Decimal('0.03')
>>> sorted(data)
[Decimal('0.03'), Decimal('1.00'), Decimal('1.34'), Decimal('1.87'),
 Decimal('2.35'), Decimal('3.45'), Decimal('9.25')]
>>> sum(data)
Decimal('19.29')
>>> a,b,c = data[:3]
>>> str(a)
'1.34'
>>> float(a)
1.34
>>> round(a, 1)
Decimal('1.3')
>>> int(a)
1
>>> a * 5
Decimal('6.70')
>>> a * b
Decimal('2.5058')
>>> c % a
Decimal('0.77')
```

Decimals can be formatted (with [`format()`](https://docs.python.org/3/library/functions.html#format "format") built-in or [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings)) in
fixed-point or scientific notation, using the same formatting syntax (see
[Format specification mini-language](https://docs.python.org/3/library/string.html#formatspec)) as builtin [`float`]