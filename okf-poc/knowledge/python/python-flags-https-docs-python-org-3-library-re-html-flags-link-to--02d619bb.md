---
id: python-flags-https-docs-python-org-3-library-re-html-flags-link-to--02d619bb
type: concept
title: Flags[¶](https://docs.python.org/3/library/re.html#flags "Link to this heading")
description: 'Changed in version 3.6: Flag constants are now instances of [`RegexFlag`](https://docs.python.org/3/library/re.html#re.RegexFlag
  "re.RegexFlag"), which is a subclass of'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Flags[¶](https://docs.python.org/3/library/re.html#flags "Link to this heading")

Changed in version 3.6: Flag constants are now instances of [`RegexFlag`](https://docs.python.org/3/library/re.html#re.RegexFlag "re.RegexFlag"), which is a subclass of
[`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag").

*class* re.RegexFlag[¶](https://docs.python.org/3/library/re.html#re.RegexFlag "Link to this definition")
:   An [`enum.IntFlag`](https://docs.python.org/3/library/enum.html#enum.IntFlag "enum.IntFlag") class containing the regex options listed below.

    Added in version 3.11: - added to `__all__`

re.A[¶](https://docs.python.org/3/library/re.html#re.A "Link to this definition")

re.ASCII[¶](https://docs.python.org/3/library/re.html#re.ASCII "Link to this definition")
:   Make `\w`, `\W`, `\b`, `\B`, `\d`, `\D`, `\s` and `\S`
    perform ASCII-only matching instead of full Unicode matching. This is only
    meaningful for Unicode (str) patterns, and is ignored for bytes patterns.

    Corresponds to the inline flag `(?a)`.

    Note

    The [`U`](https://docs.python.org/3/library/re.html#re.U "re.U") flag still exists for backward compatibility,
    but is redundant in Python 3 since
    matches are Unicode by default for `str` patterns,
    and Unicode matching isn’t allowed for bytes patterns.
    [`UNICODE`](https://docs.python.org/3/library/re.html#re.UNICODE "re.UNICODE") and the inline flag `(?u)` are similarly redundant.

re.DEBUG[¶](https://docs.python.org/3/library/re.html#re.DEBUG "Link to this definition")
:   Display debug information about compiled expression.

    No corresponding inline flag.

re.I[¶](https://docs.python.org/3/library/re.html#re.I "Link to this definition")

re.IGNORECASE[¶](https://docs.python.org/3/library/re.html#re.IGNORECASE "Link to this definition")
:   Perform case-insensitive matching;
    expressions like `[A-Z]` will also match lowercase letters.
    Full Unicode matching (such as `Ü` matching `ü`)
    also works unless the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag
    is used to disable non-ASCII matches.
    The current locale does not change the effect of this flag
    unless the [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") flag is also used.

    Corresponds to the inline flag `(?i)`.

    Note that when the Unicode patterns `[a-z]` or `[A-Z]` are used in
    combination with the [`IGNORECASE`](https://docs.python.org/3/library/re.html#re.IGNORECASE "re.IGNORECASE") flag, they will match the 52 ASCII
    letters and 4 additional non-ASCII letters: ‘İ’ (U+0130, Latin capital
    letter I with dot above), ‘ı’ (U+0131, Latin small letter dotless i),
    ‘ſ’ (U+017F, Latin small letter long s) and ‘K’ (U+212A, Kelvin sign).
    If the [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII") flag is used, only letters ‘a’ to ‘z’
    and ‘A’ to ‘Z’ are matched.

re.L[¶](https://docs.python.org/3/library/re.html#re.L "Link to this definition")

re.LOCALE[¶](https://docs.python.org/3/library/re.html#re.LOCALE "Link to this definition")
:   Make `\w`, `\W`, `\b`, `\B` and case-insensitive matching
    dependent on the current locale.
    This flag can be used only with bytes patterns.

    Corresponds to the inline flag `(?L)`.

    Warning

    This flag is discouraged; consider Unicode matching instead.
    The locale mechanism is very unreliable
    as it only handles one “culture” at a time
    and only works with 8-bit locales.
    Unicode matching is enabled by default for Unicode (str) patterns
    and it is able to handle different locales and languages.

    Changed in version 3.6: [`LOCALE`](https://docs.python.org/3/library/re.html#re.LOCALE "re.LOCALE") can be used only with bytes patterns
    and is not compatible with [`ASCII`](https://docs.python.org/3/library/re.html#re.ASCII "re.ASCII").

    Changed in version 3.7: Compiled regular expression obje