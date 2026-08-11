---
id: python-format-string-syntax-https-docs-python-org-3-library-string--9e9b5b39
type: concept
title: Format string syntax[¶](https://docs.python.org/3/library/string.html#format-string-syntax
  "Link to this heading")
description: The [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format
  "str.format") method and the [`Formatter`](https://docs.python.org/3/library/string.html#string.Formatter
  "string.Format
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/string.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Format string syntax[¶](https://docs.python.org/3/library/string.html#format-string-syntax "Link to this heading")

The [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") method and the [`Formatter`](https://docs.python.org/3/library/string.html#string.Formatter "string.Formatter") class share the same
syntax for format strings (although in the case of `Formatter`,
subclasses can define their own format string syntax). The syntax is
related to that of [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) and
[template string literals](https://docs.python.org/3/reference/lexical_analysis.html#t-strings), but it is less sophisticated
and, in particular, does not support arbitrary expressions in interpolations.

Format strings contain “replacement fields” surrounded by curly braces `{}`.
Anything that is not contained in braces is considered literal text, which is
copied unchanged to the output. If you need to include a brace character in the
literal text, it can be escaped by doubling: `{{` and `}}`.

The grammar for a replacement field is as follows:

```
replacement_field: "{" [field_name] ["!" conversion] [":" format_spec] "}"
field_name:        arg_name ("." attribute_name | "[" element_index "]")*
arg_name:          [identifier | digit+]
attribute_name:    identifier
element_index:     digit+ | index_string
index_string:      <any source character except "]"> +
conversion:        "r" | "s" | "a"
format_spec:       format-spec:format_spec
```

In less formal terms, the replacement field can start with a *field\_name* that specifies
the object whose value is to be formatted and inserted
into the output instead of the replacement field.
The *field\_name* is optionally followed by a *conversion* field, which is
preceded by an exclamation point `'!'`, and a *format\_spec*, which is preceded
by a colon `':'`. These specify a non-default format for the replacement value.

See also the [Format specification mini-language](https://docs.python.org/3/library/string.html#formatspec) section.

The *field\_name* itself begins with an *arg\_name* that is either a number or a
keyword. If it’s a number, it refers to a positional argument, and if it’s a keyword,
it refers to a named keyword argument. An *arg\_name* is treated as a number if
a call to [`str.isdecimal()`](https://docs.python.org/3/library/stdtypes.html#str.isdecimal "str.isdecimal") on the string would return true.
If the numerical arg\_names in a format string
are 0, 1, 2, … in sequence, they can all be omitted (not just some)
and the numbers 0, 1, 2, … will be automatically inserted in that order.
Because *arg\_name* is not quote-delimited, it is not possible to specify arbitrary
dictionary keys (e.g., the strings `'10'` or `':-]'`) within a format string.
The *arg\_name* can be followed by any number of index or
attribute expressions. An expression of the form `'.name'` selects the named
attribute using [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr"), while an expression of the form `'[index]'`
does an index lookup using [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__").

Changed in version 3.1: The positional argument specifiers can be omitted for [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format"),
so `'{} {}'.format(a, b)` is equivalent to `'{0} {1}'.format(a, b)`.

Changed in version 3.4: The positional argument specifiers can be omitted for [`Formatter`](https://docs.python.org/3/library/string.html#string.Formatter "string.Formatter").

Some simple format string examples:

```
"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argum