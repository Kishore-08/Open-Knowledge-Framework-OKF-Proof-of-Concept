---
id: python-decimal-objects-https-docs-python-org-3-library-decimal-html-2d6abe7b
type: concept
title: Decimal objects[¶](https://docs.python.org/3/library/decimal.html#decimal-objects
  "Link to this heading")
description: '*class* decimal.Decimal(*value=''0''*, *context=None*)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/decimal.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Decimal objects[¶](https://docs.python.org/3/library/decimal.html#decimal-objects "Link to this heading")

*class* decimal.Decimal(*value='0'*, *context=None*)[¶](https://docs.python.org/3/library/decimal.html#decimal.Decimal "Link to this definition")
:   Construct a new `Decimal` object based from *value*.

    *value* can be an integer, string, tuple, [`float`](https://docs.python.org/3/library/functions.html#float "float"), or another `Decimal`
    object. If no *value* is given, returns `Decimal('0')`. If *value* is a
    string, it should conform to the decimal numeric string syntax after leading
    and trailing whitespace characters, as well as underscores throughout, are removed:

    ```
    sign           ::=  '+' | '-'
    digit          ::=  '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    indicator      ::=  'e' | 'E'
    digits         ::=  digit [digit]...
    decimal-part   ::=  digits '.' [digits] | ['.'] digits
    exponent-part  ::=  indicator [sign] digits
    infinity       ::=  'Infinity' | 'Inf'
    nan            ::=  'NaN' [digits] | 'sNaN' [digits]
    numeric-value  ::=  decimal-part [exponent-part] | infinity
    numeric-string ::=  [sign] numeric-value | [sign] nan
    ```

    Other Unicode decimal digits are also permitted where `digit`
    appears above. These include decimal digits from various other
    alphabets (for example, Arabic-Indic and Devanāgarī digits) along
    with the fullwidth digits `'\uff10'` through `'\uff19'`.
    Case is not significant, so, for example, `inf`, `Inf`, `INFINITY`,
    and `iNfINity` are all acceptable spellings for positive infinity.

    If *value* is a [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), it should have three components, a sign
    (`0` for positive or `1` for negative), a `tuple` of
    digits, and an integer exponent. For example, `Decimal((0, (1, 4, 1, 4), -3))`
    returns `Decimal('1.414')`.

    If *value* is a [`float`](https://docs.python.org/3/library/functions.html#float "float"), the binary floating-point value is losslessly
    converted to its exact decimal equivalent. This conversion can often require
    53 or more digits of precision. For example, `Decimal(float('1.1'))`
    converts to
    `Decimal('1.100000000000000088817841970012523233890533447265625')`.

    The *context* precision does not affect how many digits are stored. That is
    determined exclusively by the number of digits in *value*. For example,
    `Decimal('3.00000')` records all five zeros even if the context precision is
    only three.

    The purpose of the *context* argument is determining what to do if *value* is a
    malformed string. If the context traps [`InvalidOperation`](https://docs.python.org/3/library/decimal.html#decimal.InvalidOperation "decimal.InvalidOperation"), an exception
    is raised; otherwise, the constructor returns a new Decimal with the value of
    `NaN`.

    Once constructed, `Decimal` objects are immutable.

    Changed in version 3.2: The argument to the constructor is now permitted to be a [`float`](https://docs.python.org/3/library/functions.html#float "float")
    instance.

    Changed in version 3.3: [`float`](https://docs.python.org/3/library/functions.html#float "float") arguments raise an exception if the [`FloatOperation`](https://docs.python.org/3/library/decimal.html#decimal.FloatOperation "decimal.FloatOperation")
    trap is set. By default the trap is off.

    Changed in version 3.6: Underscores are allowed for grouping, as with integral and floating-point
    literals in code.

    Decimal floating-point objects share many properties with the other built-in
    numeric types such as [`float`](https://docs.python.org/3/library/functions.html#float "float") and [`int`](https://docs.python.org/3/library/functions.html#int "int"). All of the usual math
    operations and special methods apply. Likewise, decimal objects can be
    copied, pickled, printed, used as dictionar