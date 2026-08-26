---
id: python-template-string-literals-t-strings-https-docs-python-org-3-l-5e0bc1d7
type: concept
title: Template String Literals (t-strings)[¶](https://docs.python.org/3/library/stdtypes.html#template-string-literals-t-strings
  "Link to this heading")
description: A *t-string* (formally a *template string literal*) is
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Template String Literals (t-strings)[¶](https://docs.python.org/3/library/stdtypes.html#template-string-literals-t-strings "Link to this heading")

A *t-string* (formally a *template string literal*) is
a string literal that is prefixed with `t` or `T`.

These strings follow the same syntax and evaluation rules as
[formatted string literals](https://docs.python.org/3/library/stdtypes.html#stdtypes-fstrings),
with the following differences:

- Rather than evaluating to a `str` object, template string literals evaluate
  to a [`string.templatelib.Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template") object.
- The [`format()`](https://docs.python.org/3/library/functions.html#format "format") protocol is not used.
  Instead, the format specifier and conversions (if any) are passed to
  a new [`Interpolation`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation") object that is created
  for each evaluated expression.
  It is up to code that processes the resulting [`Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template")
  object to decide how to handle format specifiers and conversions.
- Format specifiers containing nested replacement fields are evaluated eagerly,
  prior to being passed to the [`Interpolation`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation") object.
  For instance, an interpolation of the form `{amount:.{precision}f}` will
  evaluate the inner expression `{precision}` to determine the value of the
  `format_spec` attribute.
  If `precision` were to be `2`, the resulting format specifier
  would be `'.2f'`.
- When the equals sign `'='` is provided in an interpolation expression,
  the text of the expression is appended to the literal string that precedes
  the relevant interpolation.
  This includes the equals sign and any surrounding whitespace.
  The `Interpolation` instance for the expression will be created as
  normal, except that [`conversion`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation.conversion "string.templatelib.Interpolation.conversion") will
  be set to ‘`r`’ ([`repr()`](https://docs.python.org/3/library/functions.html#repr "repr")) by default.
  If an explicit conversion or format specifier is provided,
  this will override the default behaviour.