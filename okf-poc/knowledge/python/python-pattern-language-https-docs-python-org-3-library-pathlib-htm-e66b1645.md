---
id: python-pattern-language-https-docs-python-org-3-library-pathlib-htm-e66b1645
type: concept
title: Pattern language[¶](https://docs.python.org/3/library/pathlib.html#pattern-language
  "Link to this heading")
description: The following wildcards are supported in patterns for
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pathlib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Pattern language[¶](https://docs.python.org/3/library/pathlib.html#pattern-language "Link to this heading")

The following wildcards are supported in patterns for
[`full_match()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.full_match "pathlib.PurePath.full_match"), [`glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob") and [`rglob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob "pathlib.Path.rglob"):

`**` (entire segment)
:   Matches any number of file or directory segments, including zero.

`*` (entire segment)
:   Matches one file or directory segment.

`*` (part of a segment)
:   Matches any number of non-separator characters, including zero.

`?`
:   Matches one non-separator character.

`[seq]`
:   Matches one character in *seq*, where *seq* is a sequence of characters.
    Range expressions are supported; for example, `[a-z]` matches any lowercase ASCII letter.
    Multiple ranges can be combined: `[a-zA-Z0-9_]` matches any ASCII letter, digit, or underscore.

`[!seq]`
:   Matches one character not in *seq*, where *seq* follows the same rules as above.

For a literal match, wrap the meta-characters in brackets.
For example, `"[?]"` matches the character `"?"`.

The “`**`” wildcard enables recursive globbing. A few examples:

| Pattern | Meaning |
| --- | --- |
| “`**/*`” | Any path with at least one segment. |
| “`**/*.py`” | Any path with a final segment ending “`.py`”. |
| “`assets/**`” | Any path starting with “`assets/`”. |
| “`assets/**/*`” | Any path starting with “`assets/`”, excluding “`assets/`” itself. |

Note

Globbing with the “`**`” wildcard visits every directory in the tree.
Large directory trees may take a long time to search.

Changed in version 3.13: Globbing with a pattern that ends with “`**`” returns both files and
directories. In previous versions, only directories were returned.

In [`Path.glob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.glob "pathlib.Path.glob") and [`rglob()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rglob "pathlib.Path.rglob"), a trailing slash may be added to
the pattern to match only directories.

Changed in version 3.11: Globbing with a pattern that ends with a pathname components separator
([`sep`](https://docs.python.org/3/library/os.html#os.sep "os.sep") or [`altsep`](https://docs.python.org/3/library/os.html#os.altsep "os.altsep")) returns only directories.