---
id: python-printf-style-string-formatting-https-docs-python-org-3-libra-5e0bc1d7
type: concept
title: '`printf`-style String Formatting[¶](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting
  "Link to this heading")'
description: Note
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### `printf`-style String Formatting[¶](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting "Link to this heading")

Note

The formatting operations described here exhibit a variety of quirks that
lead to a number of common errors (such as failing to display tuples and
dictionaries correctly).

Using [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings), the [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format")
interface, or [`string.Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template") may help avoid these errors.
Each of these alternatives provides their own trade-offs and benefits of
simplicity, flexibility, and/or extensibility.

String objects have one unique built-in operation: the `%` operator (modulo).
This is also known as the string *formatting* or *interpolation* operator.
Given `format % values` (where *format* is a string), `%` conversion
specifications in *format* are replaced with zero or more elements of *values*.
The effect is similar to using the `sprintf()` function in the C language.
For example:

```
>>> print('%s has %d quote types.' % ('Python', 2))
Python has 2 quote types.
```

If *format* requires a single argument, *values* may be a single non-tuple
object. [[5]](https://docs.python.org/3/library/stdtypes.html#id16) Otherwise, *values* must be a tuple with exactly the number of
items specified by the format string, or a single mapping object (for example, a
dictionary).

A conversion specifier contains two or more characters and has the following
components, which must occur in this order:

1. The `'%'` character, which marks the start of the specifier.
2. Mapping key (optional), consisting of a parenthesised sequence of characters
   (for example, `(somename)`).
3. Conversion flags (optional), which affect the result of some conversion
   types.
4. Minimum field width (optional). If specified as an `'*'` (asterisk), the
   actual width is read from the next element of the tuple in *values*, and the
   object to convert comes after the minimum field width and optional precision.
5. Precision (optional), given as a `'.'` (dot) followed by the precision. If
   specified as `'*'` (an asterisk), the actual precision is read from the next
   element of the tuple in *values*, and the value to convert comes after the
   precision.
6. Length modifier (optional).
7. Conversion type.

When the right argument is a dictionary (or other mapping type), then the
formats in the string *must* include a parenthesised mapping key into that
dictionary inserted immediately after the `'%'` character. The mapping key
selects the value to be formatted from the mapping. For example:

```
>>> print('%(language)s has %(number)03d quote types.' %
...       {'language': "Python", "number": 2})
Python has 002 quote types.
```

In this case no `*` specifiers may occur in a format (since they require a
sequential parameter list).

The conversion flag characters are:

| Flag | Meaning |
| --- | --- |
| `'#'` | The value conversion will use the “alternate form” (where defined below). |
| `'0'` | The conversion will be zero padded for numeric values. |
| `'-'` | The converted value is left adjusted (overrides the `'0'` conversion if both are given). |
| `' '` | (a space) A blank should be left before a positive number (or empty string) produced by a signed conversion. |
| `'+'` | A sign character (`'+'` or `'-'`) will precede the conversion (overrides a “space” flag). |

A length modifier (`h`, `l`, or `L`) may be present, but is ignored as it
is not necessary for Python – so e.g. `%ld` is identical to `%d`.

The conversion types are:

| Conversion | Meaning | Notes |
| --- | --- | --- |
| `'d'` | Signed integer decimal. |  |
| `'i'` | Signed integer decimal. |  |
| `'o'` | Signed octal value. | (1) |
| `'u'` | Obsolete type – it is identical to `'d'`. | (6) |
| `'x'` | Signed hexadecimal (low