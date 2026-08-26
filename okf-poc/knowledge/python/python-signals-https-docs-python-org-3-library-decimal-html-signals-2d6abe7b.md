---
id: python-signals-https-docs-python-org-3-library-decimal-html-signals-2d6abe7b
type: concept
title: Signals[¶](https://docs.python.org/3/library/decimal.html#signals "Link to
  this heading")
description: Signals represent conditions that arise during computation. Each corresponds
  to
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/decimal.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Signals[¶](https://docs.python.org/3/library/decimal.html#signals "Link to this heading")

Signals represent conditions that arise during computation. Each corresponds to
one context flag and one context trap enabler.

The context flag is set whenever the condition is encountered. After the
computation, flags may be checked for informational purposes (for instance, to
determine whether a computation was exact). After checking the flags, be sure to
clear all flags before starting the next computation.

If the context’s trap enabler is set for the signal, then the condition causes a
Python exception to be raised. For example, if the [`DivisionByZero`](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "decimal.DivisionByZero") trap
is set, then a [`DivisionByZero`](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "decimal.DivisionByZero") exception is raised upon encountering the
condition.

*class* decimal.Clamped[¶](https://docs.python.org/3/library/decimal.html#decimal.Clamped "Link to this definition")
:   Altered an exponent to fit representation constraints.

    Typically, clamping occurs when an exponent falls outside the context’s
    [`Emin`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emin "decimal.Context.Emin") and [`Emax`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "decimal.Context.Emax") limits. If possible, the exponent is reduced to
    fit by adding zeros to the coefficient.

*class* decimal.DecimalException[¶](https://docs.python.org/3/library/decimal.html#decimal.DecimalException "Link to this definition")
:   Base class for other signals and a subclass of [`ArithmeticError`](https://docs.python.org/3/library/exceptions.html#ArithmeticError "ArithmeticError").

*class* decimal.DivisionByZero[¶](https://docs.python.org/3/library/decimal.html#decimal.DivisionByZero "Link to this definition")
:   Signals the division of a non-infinite number by zero.

    Can occur with division, modulo division, or when raising a number to a negative
    power. If this signal is not trapped, returns `Infinity` or
    `-Infinity` with the sign determined by the inputs to the calculation.

*class* decimal.Inexact[¶](https://docs.python.org/3/library/decimal.html#decimal.Inexact "Link to this definition")
:   Indicates that rounding occurred and the result is not exact.

    Signals when non-zero digits were discarded during rounding. The rounded result
    is returned. The signal flag or trap is used to detect when results are
    inexact.

*class* decimal.InvalidOperation[¶](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "Link to this definition")
:   An invalid operation was performed.

    Indicates that an operation was requested that does not make sense. If not
    trapped, returns `NaN`. Possible causes include:

    ```
    Infinity - Infinity
    0 * Infinity
    Infinity / Infinity
    x % 0
    Infinity % x
    sqrt(-x) and x > 0
    0 ** 0
    x ** (non-integer)
    x ** Infinity
    ```

*class* decimal.Overflow[¶](https://docs.python.org/3/library/decimal.html#decimal.Overflow "Link to this definition")
:   Numerical overflow.

    Indicates the exponent is larger than [`Context.Emax`](https://docs.python.org/3/library/decimal.html#decimal.Context.Emax "decimal.Context.Emax") after rounding has
    occurred. If not trapped, the result depends on the rounding mode, either
    pulling inward to the largest representable finite number or rounding outward
    to `Infinity`. In either case, [`Inexact`](https://docs.python.org/3/library/decimal.html#decimal.Inexact "decimal.Inexact") and [`Rounded`](https://docs.python.org/3/library/decimal.html#decimal.Rounded "decimal.Rounded")
    are also signaled.

*class* decimal.Rounded[¶](https://docs.python.org/3/library/decimal.html#decimal.Rounded "Link to this definition")
:   Rounding occurred though possibly no information was lost.

    Signaled whenever rounding d