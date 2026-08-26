---
id: python-standard-option-types-https-docs-python-org-3-library-optpar-f59a6996
type: concept
title: Standard option types[¶](https://docs.python.org/3/library/optparse.html#standard-option-types
  "Link to this heading")
description: '`optparse` has five built-in option types: `"string"`, `"int"`,'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Standard option types[¶](https://docs.python.org/3/library/optparse.html#standard-option-types "Link to this heading")

`optparse` has five built-in option types: `"string"`, `"int"`,
`"choice"`, `"float"` and `"complex"`. If you need to add new
option types, see section [Extending optparse](https://docs.python.org/3/library/optparse.html#optparse-extending-optparse).

Arguments to string options are not checked or converted in any way: the text on
the command line is stored in the destination (or passed to the callback) as-is.

Integer arguments (type `"int"`) are parsed as follows:

- if the number starts with `0x`, it is parsed as a hexadecimal number
- if the number starts with `0`, it is parsed as an octal number
- if the number starts with `0b`, it is parsed as a binary number
- otherwise, the number is parsed as a decimal number

The conversion is done by calling [`int()`](https://docs.python.org/3/library/functions.html#int "int") with the appropriate base (2, 8,
10, or 16). If this fails, so will `optparse`, although with a more useful
error message.

`"float"` and `"complex"` option arguments are converted directly with
[`float()`](https://docs.python.org/3/library/functions.html#float "float") and [`complex()`](https://docs.python.org/3/library/functions.html#complex "complex"), with similar error-handling.

`"choice"` options are a subtype of `"string"` options. The
[`choices`](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "optparse.Option.choices") option attribute (a sequence of strings) defines the
set of allowed option arguments. `optparse.check_choice()` compares
user-supplied option arguments against this master list and raises
[`OptionValueError`](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError "optparse.OptionValueError") if an invalid string is given.