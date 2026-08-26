---
id: python-string-methods-https-docs-python-org-3-library-stdtypes-html-5e0bc1d7
type: concept
title: String Methods[¶](https://docs.python.org/3/library/stdtypes.html#string-methods
  "Link to this heading")
description: Strings implement all of the [common](https://docs.python.org/3/library/stdtypes.html#typesseq-common)
  sequence
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/stdtypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### String Methods[¶](https://docs.python.org/3/library/stdtypes.html#string-methods "Link to this heading")

Strings implement all of the [common](https://docs.python.org/3/library/stdtypes.html#typesseq-common) sequence
operations, along with the additional methods described below.

Strings also support two styles of string formatting, one providing a large
degree of flexibility and customization (see [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format"),
[Format string syntax](https://docs.python.org/3/library/string.html#formatstrings) and [Custom string formatting](https://docs.python.org/3/library/string.html#string-formatting)) and the other based on C
`printf` style formatting that handles a narrower range of types and is
slightly harder to use correctly, but is often faster for the cases it can
handle ([printf-style String Formatting](https://docs.python.org/3/library/stdtypes.html#old-string-formatting)).

The [Text Processing Services](https://docs.python.org/3/library/text.html#textservices) section of the standard library covers a number of
other modules that provide various text related utilities (including regular
expression support in the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.") module).

str.capitalize()[¶](https://docs.python.org/3/library/stdtypes.html#str.capitalize "Link to this definition")
:   Return a copy of the string with its first character capitalized and the
    rest lowercased.

    Changed in version 3.8: The first character is now put into titlecase rather than uppercase.
    This means that characters like digraphs will only have their first
    letter capitalized, instead of the full character.

str.casefold()[¶](https://docs.python.org/3/library/stdtypes.html#str.casefold "Link to this definition")
:   Return a casefolded copy of the string. Casefolded strings may be used for
    caseless matching.

    Casefolding is similar to lowercasing but more aggressive because it is
    intended to remove all case distinctions in a string. For example, the German
    lowercase letter `'ß'` is equivalent to `"ss"`. Since it is already
    lowercase, [`lower()`](https://docs.python.org/3/library/stdtypes.html#str.lower "str.lower") would do nothing to `'ß'`; `casefold()`
    converts it to `"ss"`.
    For example:

    ```
    >>> 'straße'.lower()
    'straße'
    >>> 'straße'.casefold()
    'strasse'
    ```

    The casefolding algorithm is
    [described in section 3.13 ‘Default Case Folding’ of the Unicode Standard](https://www.unicode.org/versions/Unicode16.0.0/core-spec/chapter-3/#G33992).

    Added in version 3.3.

str.center(*width*, *fillchar=' '*, */*)[¶](https://docs.python.org/3/library/stdtypes.html#str.center "Link to this definition")
:   Return centered in a string of length *width*. Padding is done using the
    specified *fillchar* (default is an ASCII space). The original string is
    returned if *width* is less than or equal to `len(s)`. For example:

    ```
    >>> 'Python'.center(10)
    '  Python  '
    >>> 'Python'.center(10, '-')
    '--Python--'
    >>> 'Python'.center(4)
    'Python'
    ```

str.count(*sub*[, *start*[, *end*]])[¶](https://docs.python.org/3/library/stdtypes.html#str.count "Link to this definition")
:   Return the number of non-overlapping occurrences of substring *sub* in the
    range [*start*, *end*]. Optional arguments *start* and *end* are
    interpreted as in slice notation.

    If *sub* is empty, returns the number of empty strings between characters
    which is the length of the string plus one. For example:

    ```
    >>> 'spam, spam, spam'.count('spam')
    3
    >>> 'spam, spam, spam'.count('spam', 5)
    2
    >>> 'spam, spam, spam'.count('spam', 5, 10)
    1
    >>> 'spam, spam, spam'.count('eggs')
    0
    >>> 'spam, spam, spam'.count('')
    17
    ```

str.encode(*encoding='utf-8'*, *errors='strict'*)[¶](https://docs.python.org/3/library/stdtype