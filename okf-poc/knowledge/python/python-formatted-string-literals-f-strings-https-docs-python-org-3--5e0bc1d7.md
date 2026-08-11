---
id: python-formatted-string-literals-f-strings-https-docs-python-org-3--5e0bc1d7
type: concept
title: Formatted String Literals (f-strings)[¶](https://docs.python.org/3/library/stdtypes.html#formatted-string-literals-f-strings
  "Link to this heading")
description: Added in version 3.6.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Formatted String Literals (f-strings)[¶](https://docs.python.org/3/library/stdtypes.html#formatted-string-literals-f-strings "Link to this heading")

Added in version 3.6.

Changed in version 3.7: The [`await`](https://docs.python.org/3/reference/expressions.html#await) and [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for) can be used in expressions
within f-strings.

Changed in version 3.8: Added the debug specifier (`=`)

Changed in version 3.12: Many restrictions on expressions within f-strings have been removed.
Notably, nested strings, comments, and backslashes are now permitted.

An *f-string* (formally a *formatted string literal*) is
a string literal that is prefixed with `f` or `F`.
This type of string literal allows embedding the results of arbitrary Python
expressions within *replacement fields*, which are delimited by curly
brackets (`{}`).
Each replacement field must contain an expression, optionally followed by:

- a *debug specifier* – an equal sign (`=`);
- a *conversion specifier* – `!s`, `!r` or `!a`; and/or
- a *format specifier* prefixed with a colon (`:`).

See the [Lexical Analysis section on f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) for details
on the syntax of these fields.

#### Debug specifier[¶](https://docs.python.org/3/library/stdtypes.html#debug-specifier "Link to this heading")

Added in version 3.8.

If a debug specifier – an equal sign (`=`) – appears after the replacement
field expression, the resulting f-string will contain the expression’s source,
the equal sign, and the value of the expression.
This is often useful for debugging:

```
>>> number = 14.3
>>> f'{number=}'
'number=14.3'
```

Whitespace before, inside and after the expression, as well as whitespace
after the equal sign, is significant — it is retained in the result:

```
>>> f'{ number  -  4  = }'
' number  -  4  = 10.3'
```

#### Conversion specifier[¶](https://docs.python.org/3/library/stdtypes.html#conversion-specifier "Link to this heading")

By default, the value of a replacement field expression is converted to
a string using [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str"):

```
>>> from fractions import Fraction
>>> one_third = Fraction(1, 3)
>>> f'{one_third}'
'1/3'
```

When a debug specifier but no format specifier is used, the default conversion
instead uses [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr"):

```
>>> f'{one_third = }'
'one_third = Fraction(1, 3)'
```

The conversion can be specified explicitly using one of these specifiers:

- `!s` for [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str")
- `!r` for [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr")
- `!a` for [`ascii()`](https://docs.python.org/3/library/functions.html#ascii "ascii")

For example:

```
>>> str(one_third)
'1/3'
>>> repr(one_third)
'Fraction(1, 3)'

>>> f'{one_third!s} is {one_third!r}'
'1/3 is Fraction(1, 3)'

>>> string = "¡kočka 😸!"
>>> ascii(string)
"'\\xa1ko\\u010dka \\U0001f638!'"

>>> f'{string = !a}'
"string = '\\xa1ko\\u010dka \\U0001f638!'"
```

#### Format specifier[¶](https://docs.python.org/3/library/stdtypes.html#format-specifier "Link to this heading")

After the expression has been evaluated, and possibly converted using an
explicit conversion specifier, it is formatted using the [`format()`](https://docs.python.org/3/library/functions.html#format "format") function.
If the replacement field includes a *format specifier* introduced by a colon
(`:`), the specifier is passed to `format()` as the second argument.
The result of `format()` is then used as the final value for the
replacement field. For example:

```
>>> from fractions import Fraction
>>> one_third = Fraction(1, 3)
>>> f'{one_third:.6f}'
'0.333333'
>>> f'{one_third:_^+10}'
'___+1/3___'
>>> >>> f'{one_third!r:_^20}'
'___Fraction(1, 3)___'
>>> f'{one_third = :~>10}~'
'one_third = ~~~~~~~1/3~'
```