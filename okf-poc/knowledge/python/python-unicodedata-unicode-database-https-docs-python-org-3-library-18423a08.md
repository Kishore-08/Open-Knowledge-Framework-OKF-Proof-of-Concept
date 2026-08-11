---
id: python-unicodedata-unicode-database-https-docs-python-org-3-library-18423a08
type: concept
title: '`unicodedata` — Unicode Database[¶](https://docs.python.org/3/library/unicodedat'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/unicodedata.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `unicodedata` — Unicode Database[¶](https://docs.python.org/3/library/unicodedata.html#module-unicodedata "Link to this heading")

---

This module provides access to the Unicode Character Database (UCD) which
defines character properties for all Unicode characters. The data contained in
this database is compiled from the [UCD version 16.0.0](https://www.unicode.org/Public/16.0.0/ucd).

The module uses the same names and symbols as defined by Unicode
Standard Annex #44, [“Unicode Character Database”](https://www.unicode.org/reports/tr44/). It defines the
following functions:

See also

The [Unicode HOWTO](https://docs.python.org/3/howto/unicode.html#unicode-howto) for more information about Unicode and how to use
this module.

unicodedata.lookup(*name*)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.lookup "Link to this definition")
:   Look up character by name. If a character with the given name is found, return
    the corresponding character. If not found, [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "KeyError") is raised.
    For example:

    ```
    >>> unicodedata.lookup('LEFT CURLY BRACKET')
    '{'
    ```

    The characters returned by this function are the same as those produced by
    `\N` escape sequence in string literals. For example:

    ```
    >>> unicodedata.lookup('MIDDLE DOT') == '\N{MIDDLE DOT}'
    True
    ```

    Changed in version 3.3: Support for name aliases [[1]](https://docs.python.org/3/library/unicodedata.html#id3) and named sequences [[2]](https://docs.python.org/3/library/unicodedata.html#id4) has been added.

unicodedata.name(*chr*, *default=None*, */*)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.name "Link to this definition")
:   Returns the name assigned to the character *chr* as a string. If no
    name is defined, *default* is returned, or, if not given, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is
    raised. For example:

    ```
    >>> unicodedata.name('½')
    'VULGAR FRACTION ONE HALF'
    >>> unicodedata.name('\uFFFF', 'fallback')
    'fallback'
    ```

unicodedata.decimal(*chr*, *default=None*, */*)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.decimal "Link to this definition")
:   Returns the decimal value assigned to the character *chr* as integer.
    If no such value is defined, *default* is returned, or, if not given,
    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised. For example:

    ```
    >>> unicodedata.decimal('\N{ARABIC-INDIC DIGIT NINE}')
    9
    >>> unicodedata.decimal('\N{SUPERSCRIPT NINE}', -1)
    -1
    ```

unicodedata.digit(*chr*, *default=None*, */*)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.digit "Link to this definition")
:   Returns the digit value assigned to the character *chr* as integer.
    If no such value is defined, *default* is returned, or, if not given,
    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised:

    ```
    >>> unicodedata.digit('\N{SUPERSCRIPT NINE}')
    9
    ```

unicodedata.numeric(*chr*, *default=None*, */*)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.numeric "Link to this definition")
:   Returns the numeric value assigned to the character *chr* as float.
    If no such value is defined, *default* is returned, or, if not given,
    [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised:

    ```
    >>> unicodedata.numeric('½')
    0.5
    ```

unicodedata.category(*chr*)[¶](https://docs.python.org/3/library/unicodedata.html#unicodedata.category "Link to this definition")
:   Returns the general category assigned to the character *chr* as
    string. General category names consist of two letters.
    See the [General Category Values section of the Unicode Character
    Database documentatio