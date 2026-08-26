---
id: python-context-objects-https-docs-python-org-3-library-decimal-html-2d6abe7b
type: concept
title: Context objects[¶](https://docs.python.org/3/library/decimal.html#context-objects
  "Link to this heading")
description: Contexts are environments for arithmetic operations. They govern precision,
  set
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/decimal.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Context objects[¶](https://docs.python.org/3/library/decimal.html#context-objects "Link to this heading")

Contexts are environments for arithmetic operations. They govern precision, set
rules for rounding, determine which signals are treated as exceptions, and limit
the range for exponents.

Each thread has its own current context which is accessed or changed using the
[`getcontext()`](https://docs.python.org/3/library/decimal.html#decimal.getcontext "decimal.getcontext") and [`setcontext()`](https://docs.python.org/3/library/decimal.html#decimal.setcontext "decimal.setcontext") functions:

decimal.getcontext()[¶](https://docs.python.org/3/library/decimal.html#decimal.getcontext "Link to this definition")
:   Return the current context for the active thread.

decimal.setcontext(*c*, */*)[¶](https://docs.python.org/3/library/decimal.html#decimal.setcontext "Link to this definition")
:   Set the current context for the active thread to *c*.

You can also use the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement and the [`localcontext()`](https://docs.python.org/3/library/decimal.html#decimal.localcontext "decimal.localcontext")
function to temporarily change the active context.

decimal.localcontext(*ctx=None*, *\*\*kwargs*)[¶](https://docs.python.org/3/library/decimal.html#decimal.localcontext "Link to this definition")
:   Return a context manager that will set the current context for the active thread
    to a copy of *ctx* on entry to the with-statement and restore the previous context
    when exiting the with-statement. If no context is specified, a copy of the
    current context is used. The *kwargs* argument is used to set the attributes
    of the new context.

    For example, the following code sets the current decimal precision to 42 places,
    performs a calculation, and then automatically restores the previous context:

    ```
    from decimal import localcontext

    with localcontext() as ctx:
        ctx.prec = 42   # Perform a high precision calculation
        s = calculate_something()
    s = +s  # Round the final result back to the default precision
    ```

    Using keyword arguments, the code would be the following:

    ```
    from decimal import localcontext

    with localcontext(prec=42) as ctx:
        s = calculate_something()
    s = +s
    ```

    Raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") if *kwargs* supplies an attribute that [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") doesn’t
    support. Raises either `TypeError` or [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") if *kwargs* supplies an
    invalid value for an attribute.

    Changed in version 3.11: `localcontext()` now supports setting context attributes through the use of keyword arguments.

decimal.IEEEContext(*bits*)[¶](https://docs.python.org/3/library/decimal.html#decimal.IEEEContext "Link to this definition")
:   Return a context object initialized to the proper values for one of the
    IEEE interchange formats. The argument must be a multiple of 32 and less
    than [`IEEE_CONTEXT_MAX_BITS`](https://docs.python.org/3/library/decimal.html#decimal.IEEE_CONTEXT_MAX_BITS "decimal.IEEE_CONTEXT_MAX_BITS").

    Added in version 3.14.

New contexts can also be created using the [`Context`](https://docs.python.org/3/library/decimal.html#decimal.Context "decimal.Context") constructor
described below. In addition, the module provides three pre-made contexts:

decimal.BasicContext[¶](https://docs.python.org/3/library/decimal.html#decimal.BasicContext "Link to this definition")
:   This is a standard context defined by the General Decimal Arithmetic
    Specification. Precision is set to nine. Rounding is set to
    [`ROUND_HALF_UP`](https://docs.python.org/3/library/decimal.html#decimal.ROUND_HALF_UP "decimal.ROUND_HALF_UP"). All flags are cleared. All traps are e