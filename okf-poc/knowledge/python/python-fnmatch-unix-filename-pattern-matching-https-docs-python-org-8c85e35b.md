---
id: python-fnmatch-unix-filename-pattern-matching-https-docs-python-org-8c85e35b
type: concept
title: '`fnmatch` — Unix filename pattern matching[¶](https://docs.python.org/3/library/'
description: '**Source code:** [Lib/fnmatch.py](https://github.com/python/cpython/tree/3.14/Lib/fnmatch.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/fnmatch.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `fnmatch` — Unix filename pattern matching[¶](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "Link to this heading")

**Source code:** [Lib/fnmatch.py](https://github.com/python/cpython/tree/3.14/Lib/fnmatch.py)

---

This module provides support for Unix shell-style wildcards, which are *not* the
same as regular expressions (which are documented in the [`re`](https://docs.python.org/3/library/re.html#module-re "re: Regular expression operations.") module). The
special characters used in shell-style wildcards are:

| Pattern | Meaning |
| --- | --- |
| `*` | matches everything |
| `?` | matches any single character |
| `[seq]` | matches any character in *seq* |
| `[!seq]` | matches any character not in *seq* |

For a literal match, wrap the meta-characters in brackets.
For example, `'[?]'` matches the character `'?'`.

Note that the filename separator (`'/'` on Unix) is *not* special to this
module. See module [`glob`](https://docs.python.org/3/library/glob.html#module-glob "glob: Unix shell style pathname pattern expansion.") for pathname expansion (`glob` uses
[`filter()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "fnmatch.filter") to match pathname segments). Similarly, filenames starting with
a period are not special for this module, and are matched by the `*` and `?`
patterns.

Unless stated otherwise, “filename string” and “pattern string” either refer to
[`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or `ISO-8859-1` encoded [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects. Note that the
functions documented below do not allow to mix a `bytes` pattern with
a `str` filename, and vice-versa.

Finally, note that [`@functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache "functools.lru_cache") with a *maxsize* of 32768
is used to cache the (typed) compiled regex patterns in the following
functions: [`fnmatch()`](https://docs.python.org/3/library/fnmatch.html#module-fnmatch "fnmatch: Unix shell style filename pattern matching."), [`fnmatchcase()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase"), [`filter()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "fnmatch.filter"), [`filterfalse()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.filterfalse "fnmatch.filterfalse").

fnmatch.fnmatch(*name*, *pat*)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch "Link to this definition")
:   Test whether the filename string *name* matches the pattern string *pat*,
    returning `True` or `False`. Both parameters are case-normalized
    using [`os.path.normcase()`](https://docs.python.org/3/library/os.path.html#os.path.normcase "os.path.normcase"). [`fnmatchcase()`](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "fnmatch.fnmatchcase") can be used to perform a
    case-sensitive comparison, regardless of whether that’s standard for the
    operating system.

    This example will print all file names in the current directory with the
    extension `.txt`:

    ```
    import fnmatch
    import os

    for file in os.listdir('.'):
        if fnmatch.fnmatch(file, '*.txt'):
            print(file)
    ```

fnmatch.fnmatchcase(*name*, *pat*)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase "Link to this definition")
:   Test whether the filename string *name* matches the pattern string *pat*,
    returning `True` or `False`;
    the comparison is case-sensitive and does not apply [`os.path.normcase()`](https://docs.python.org/3/library/os.path.html#os.path.normcase "os.path.normcase").

fnmatch.filter(*names*, *pat*)[¶](https://docs.python.org/3/library/fnmatch.html#fnmatch.filter "Link to this definition")
:   Construct a list from those elements of the [iterable](https://docs.python.org/3/glossary.html#term-iterable) of filename
    strings *names* that match the pattern string *pat*.
    It is t