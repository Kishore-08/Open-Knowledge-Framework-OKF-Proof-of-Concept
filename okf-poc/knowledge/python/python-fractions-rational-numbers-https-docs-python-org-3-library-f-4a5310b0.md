---
id: python-fractions-rational-numbers-https-docs-python-org-3-library-f-4a5310b0
type: concept
title: '`fractions` — Rational numbers[¶](https://docs.python.org/3/library/fractions.ht'
description: '**Source code:** [Lib/fractions.py](https://github.com/python/cpython/tree/3.14/Lib/fractions.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/fractions.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `fractions` — Rational numbers[¶](https://docs.python.org/3/library/fractions.html#module-fractions "Link to this heading")

**Source code:** [Lib/fractions.py](https://github.com/python/cpython/tree/3.14/Lib/fractions.py)

---

The `fractions` module provides support for rational number arithmetic.

A Fraction instance can be constructed from a pair of rational numbers, from
a single number, or from a string.

*class* fractions.Fraction(*numerator=0*, *denominator=1*)[¶](https://docs.python.org/3/library/fractions.html#fractions.Fraction "Link to this definition")

*class* fractions.Fraction(*number*)

*class* fractions.Fraction(*string*)
:   The first version requires that *numerator* and *denominator* are instances
    of [`numbers.Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational") and returns a new `Fraction` instance
    with a value equal to `numerator/denominator`.
    If *denominator* is zero, it raises a [`ZeroDivisionError`](https://docs.python.org/3/library/exceptions.html#ZeroDivisionError "ZeroDivisionError").

    The second version requires that *number* is an instance of
    [`numbers.Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational") or has the `as_integer_ratio()` method
    (this includes [`float`](https://docs.python.org/3/library/functions.html#float "float") and [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")).
    It returns a `Fraction` instance with exactly the same value.
    Assumed, that the `as_integer_ratio()` method returns a pair
    of coprime integers and last one is positive.
    Note that due to the
    usual issues with binary point (see [Floating-Point Arithmetic: Issues and Limitations](https://docs.python.org/3/tutorial/floatingpoint.html#tut-fp-issues)), the
    argument to `Fraction(1.1)` is not exactly equal to 11/10, and so
    `Fraction(1.1)` does *not* return `Fraction(11, 10)` as one might expect.
    (But see the documentation for the [`limit_denominator()`](https://docs.python.org/3/library/fractions.html#fractions.Fraction.limit_denominator "fractions.Fraction.limit_denominator") method below.)

    The last version of the constructor expects a string.
    The usual form for this instance is:

    ```
    [sign] numerator ['/' denominator]
    ```

    where the optional `sign` may be either ‘+’ or ‘-’ and
    `numerator` and `denominator` (if present) are strings of
    decimal digits (underscores may be used to delimit digits as with
    integral literals in code). In addition, any string that represents a finite
    value and is accepted by the [`float`](https://docs.python.org/3/library/functions.html#float "float") constructor is also
    accepted by the `Fraction` constructor. In either form the
    input string may also have leading and/or trailing whitespace.
    Here are some examples:

    ```
    >>> from fractions import Fraction
    >>> Fraction(16, -10)
    Fraction(-8, 5)
    >>> Fraction(123)
    Fraction(123, 1)
    >>> Fraction()
    Fraction(0, 1)
    >>> Fraction('3/7')
    Fraction(3, 7)
    >>> Fraction(' -3/7 ')
    Fraction(-3, 7)
    >>> Fraction('1.414213 \t\n')
    Fraction(1414213, 1000000)
    >>> Fraction('-.125')
    Fraction(-1, 8)
    >>> Fraction('7e-6')
    Fraction(7, 1000000)
    >>> Fraction(2.25)
    Fraction(9, 4)
    >>> Fraction(1.1)
    Fraction(2476979795053773, 2251799813685248)
    >>> from decimal import Decimal
    >>> Fraction(Decimal('1.1'))
    Fraction(11, 10)
    ```

    The `Fraction` class inherits from the abstract base class
    [`numbers.Rational`](https://docs.python.org/3/library/numbers.html#numbers.Rational "numbers.Rational"), and implements all of the methods and
    operations from that class. `Fraction` instances are [hashable](https://docs.python.org/3/glossary.html#term-hashable),
    and should be treated as immutable. In addition,
    `Fraction` has the following pro