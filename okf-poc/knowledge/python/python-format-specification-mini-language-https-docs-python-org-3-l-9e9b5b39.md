---
id: python-format-specification-mini-language-https-docs-python-org-3-l-9e9b5b39
type: concept
title: Format specification mini-language[¶](https://docs.python.org/3/library/string.html#format-specification-mini-language
  "Link to this heading")
description: “Format specifications” are used within replacement fields contained
  within a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/string.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Format specification mini-language[¶](https://docs.python.org/3/library/string.html#format-specification-mini-language "Link to this heading")

“Format specifications” are used within replacement fields contained within a
format string to define how individual values are presented (see
[Format string syntax](https://docs.python.org/3/library/string.html#formatstrings), [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings), and [t-strings](https://docs.python.org/3/reference/lexical_analysis.html#t-strings)).
They can also be passed directly to the built-in
[`format()`](https://docs.python.org/3/library/functions.html#format "format") function. Each formattable type may define how the format
specification is to be interpreted.

Most built-in types implement the following options for format specifications,
although some of the formatting options are only supported by the numeric types.

A general convention is that an empty format specification produces
the same result as if you had called [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") on the value. A
non-empty format specification typically modifies the result.

The general form of a *standard format specifier* is:

```
format_spec:             [options][width_and_precision][type]
options:                 [[fill]align][sign]["z"]["#"]["0"]
fill:                    <any character>
align:                   "<" | ">" | "=" | "^"
sign:                    "+" | "-" | " "
width_and_precision:     [width_with_grouping][precision_with_grouping]
width_with_grouping:     [width][grouping]
precision_with_grouping: "." [precision][grouping] | "." grouping
width:                   digit+
precision:               digit+
grouping:                "," | "_"
type:                    "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g"
                         | "G" | "n" | "o" | "s" | "x" | "X" | "%"
```

If a valid *align* value is specified, it can be preceded by a *fill*
character that can be any character and defaults to a space if omitted.
It is not possible to use a literal curly brace (”`{`” or “`}`”) as
the *fill* character in a [formatted string literal](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) or when using the [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format")
method. However, it is possible to insert a curly brace
with a nested replacement field. This limitation doesn’t
affect the [`format()`](https://docs.python.org/3/library/functions.html#format "format") function.

The meaning of the various alignment options is as follows:

| Option | Meaning |
| --- | --- |
| `'<'` | Forces the field to be left-aligned within the available space (this is the default for most objects). |
| `'>'` | Forces the field to be right-aligned within the available space (this is the default for numbers). |
| `'='` | Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types, excluding [`complex`](https://docs.python.org/3/library/functions.html#complex "complex"). It becomes the default for numbers when ‘0’ immediately precedes the field width. |
| `'^'` | Forces the field to be centered within the available space. |

Note that unless a minimum field width is defined, the field width will always
be the same size as the data to fill it, so that the alignment option has no
meaning in this case.

The *sign* option is only valid for number types, and can be one of the
following:

| Option | Meaning |
| --- | --- |
| `'+'` | Indicates that a sign should be used for both positive as well as negative numbers. |
| `'-'` | Indicates that a sign should be used only for negative numbers (this is the default behavior). |
| space | Indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers. |

The `'z'` option coerces negative zero