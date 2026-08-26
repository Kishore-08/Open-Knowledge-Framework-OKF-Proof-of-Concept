---
id: python-template-strings-strings-https-docs-python-org-3-library-str-9e9b5b39
type: concept
title: Template strings ($-strings)[¶](https://docs.python.org/3/library/string.html#template-strings-strings
  "Link to this heading")
description: Note
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/string.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Template strings ($-strings)[¶](https://docs.python.org/3/library/string.html#template-strings-strings "Link to this heading")

Note

The feature described here was introduced in Python 2.4;
a simple templating method based upon regular expressions.
It predates [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format"), [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings),
and [template string literals](https://docs.python.org/3/library/string.templatelib.html#template-strings).

It is unrelated to template string literals (t-strings),
which were introduced in Python 3.14.
These evaluate to [`string.templatelib.Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template") objects,
found in the [`string.templatelib`](https://docs.python.org/3/library/string.templatelib.html#module-string.templatelib "string.templatelib: Support for template string literals.") module.

Template strings provide simpler string substitutions as described in
[**PEP 292**](https://peps.python.org/pep-0292/). A primary use case for template strings is for
internationalization (i18n) since in that context, the simpler syntax and
functionality makes it easier to translate than other built-in string
formatting facilities in Python. As an example of a library built on template
strings for i18n, see the
[flufl.i18n](https://flufli18n.readthedocs.io/en/latest/) package.

Template strings support `$`-based substitutions, using the following rules:

- `$$` is an escape; it is replaced with a single `$`.
- `$identifier` names a substitution placeholder matching a mapping key of
  `"identifier"`. By default, `"identifier"` is restricted to any
  case-insensitive ASCII alphanumeric string (including underscores) that
  starts with an underscore or ASCII letter. The first non-identifier
  character after the `$` character terminates this placeholder
  specification.
- `${identifier}` is equivalent to `$identifier`. It is required when
  valid identifier characters follow the placeholder but are not part of the
  placeholder, such as `"${noun}ification"`.

Any other appearance of `$` in the string will result in a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError")
being raised.

The `string` module provides a [`Template`](https://docs.python.org/3/library/string.html#string.Template "string.Template") class that implements
these rules. The methods of `Template` are:

*class* string.Template(*template*)[¶](https://docs.python.org/3/library/string.html#string.Template "Link to this definition")
:   The constructor takes a single argument which is the template string.

    substitute(*mapping={}*, */*, *\*\*kwds*)[¶](https://docs.python.org/3/library/string.html#string.Template.substitute "Link to this definition")
    :   Performs the template substitution, returning a new string. *mapping* is
        any dictionary-like object with keys that match the placeholders in the
        template. Alternatively, you can provide keyword arguments, where the
        keywords are the placeholders. When both *mapping* and *kwds* are given
        and there are duplicates, the placeholders from *kwds* take precedence.

    safe\_substitute(*mapping={}*, */*, *\*\*kwds*)[¶](https://docs.python.org/3/library/string.html#string.Template.safe_substitute "Link to this definition")
    :   Like [`substitute()`](https://docs.python.org/3/library/string.html#string.Template.substitute "string.Template.substitute"), except that if placeholders are missing from
        *mapping* and *kwds*, instead of raising a [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") exception, the
        original placeholder will appear in the resulting string intact. Also,
        unlike with `substitute()`, any other appearances of the `$` will
        simply return `$` instead of raising [`Valu