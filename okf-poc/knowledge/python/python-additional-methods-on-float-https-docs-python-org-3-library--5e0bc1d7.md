---
id: python-additional-methods-on-float-https-docs-python-org-3-library--5e0bc1d7
type: concept
title: Additional Methods on Float[¶](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float
  "Link to this heading")
description: The float type implements the [`numbers.Real`](https://docs.python.org/3/library/numbers.html#numbers.Real
  "numbers.Real") [abstract base
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Additional Methods on Float[¶](https://docs.python.org/3/library/stdtypes.html#additional-methods-on-float "Link to this heading")

The float type implements the [`numbers.Real`](https://docs.python.org/3/library/numbers.html#numbers.Real "numbers.Real") [abstract base
class](https://docs.python.org/3/glossary.html#term-abstract-base-class). float also has the following additional methods.

*classmethod* float.from\_number(*x*)[¶](https://docs.python.org/3/library/stdtypes.html#float.from_number "Link to this definition")
:   Class method to return a floating-point number constructed from a number *x*.

    If the argument is an integer or a floating-point number, a
    floating-point number with the same value (within Python’s floating-point
    precision) is returned. If the argument is outside the range of a Python
    float, an [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") will be raised.

    For a general Python object `x`, `float.from_number(x)` delegates to
    `x.__float__()`.
    If [`__float__()`](https://docs.python.org/3/reference/datamodel.html#object.__float__ "object.__float__") is not defined then it falls back
    to [`__index__()`](https://docs.python.org/3/reference/datamodel.html#object.__index__ "object.__index__").

    Added in version 3.14.

float.as\_integer\_ratio()[¶](https://docs.python.org/3/library/stdtypes.html#float.as_integer_ratio "Link to this definition")
:   Return a pair of integers whose ratio is exactly equal to the
    original float. The ratio is in lowest terms and has a positive denominator. Raises
    [`OverflowError`](https://docs.python.org/3/library/exceptions.html#OverflowError "OverflowError") on infinities and a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") on
    NaNs.

float.is\_integer()[¶](https://docs.python.org/3/library/stdtypes.html#float.is_integer "Link to this definition")
:   Return `True` if the float instance is finite with integral
    value, and `False` otherwise:

    ```
    >>> (-2.0).is_integer()
    True
    >>> (3.2).is_integer()
    False
    ```

Two methods support conversion to
and from hexadecimal strings. Since Python’s floats are stored
internally as binary numbers, converting a float to or from a
*decimal* string usually involves a small rounding error. In
contrast, hexadecimal strings allow exact representation and
specification of floating-point numbers. This can be useful when
debugging, and in numerical work.

float.hex()[¶](https://docs.python.org/3/library/stdtypes.html#float.hex "Link to this definition")
:   Return a representation of a floating-point number as a hexadecimal
    string. For finite floating-point numbers, this representation
    will always include a leading `0x` and a trailing `p` and
    exponent.

*classmethod* float.fromhex(*s*)[¶](https://docs.python.org/3/library/stdtypes.html#float.fromhex "Link to this definition")
:   Class method to return the float represented by a hexadecimal
    string *s*. The string *s* may have leading and trailing
    whitespace.

Note that [`float.hex()`](https://docs.python.org/3/library/stdtypes.html#float.hex "float.hex") is an instance method, while
[`float.fromhex()`](https://docs.python.org/3/library/stdtypes.html#float.fromhex "float.fromhex") is a class method.

A hexadecimal string takes the form:

```
[sign] ['0x'] integer ['.' fraction] ['p' exponent]
```

where the optional `sign` may be either `+` or `-`, `integer`
and `fraction` are strings of hexadecimal digits, and `exponent`
is a decimal integer with an optional leading sign. Case is not
significant, and there must be at least one hexadecimal digit in
either the integer or the fraction. This syntax is similar to the
syntax specified in section 6.4.4.2 of the C99 standard, and also to
the syntax used in Java 1.5 onwards. In particular, the output of
[`float.hex()`](https://docs.python.org/3/library/stdtypes.html#float.hex "