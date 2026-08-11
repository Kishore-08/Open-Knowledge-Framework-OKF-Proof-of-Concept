---
id: python-functions-https-docs-python-org-3-library-re-html-functions--02d619bb
type: concept
title: Functions[¶](https://docs.python.org/3/library/re.html#functions "Link to this
  heading")
description: re.compile(*pattern*, *flags=0*)[¶](https://docs.python.org/3/library/re.html#re.compile
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Functions[¶](https://docs.python.org/3/library/re.html#functions "Link to this heading")

re.compile(*pattern*, *flags=0*)[¶](https://docs.python.org/3/library/re.html#re.compile "Link to this definition")
:   Compile a regular expression pattern into a [regular expression object](https://docs.python.org/3/library/re.html#re-objects), which can be used for matching using its
    [`match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match"), [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") and other methods, described
    below.

    The expression’s behaviour can be modified by specifying a *flags* value.
    Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR
    (the `|` operator).

    The sequence

    ```
    prog = re.compile(pattern)
    result = prog.match(string)
    ```

    is equivalent to

    ```
    result = re.match(pattern, string)
    ```

    but using [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "re.compile") and saving the resulting regular expression
    object for reuse is more efficient when the expression will be used several
    times in a single program.

    Note

    The compiled versions of the most recent patterns passed to
    [`re.compile()`](https://docs.python.org/3/library/re.html#re.compile "re.compile") and the module-level matching functions are cached, so
    programs that use only a few regular expressions at a time needn’t worry
    about compiling regular expressions.

re.search(*pattern*, *string*, *flags=0*)[¶](https://docs.python.org/3/library/re.html#re.search "Link to this definition")
:   Scan through *string* looking for the first location where the regular expression
    *pattern* produces a match, and return a corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return
    `None` if no position in the string matches the pattern; note that this is
    different from finding a zero-length match at some point in the string.

    The expression’s behaviour can be modified by specifying a *flags* value.
    Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR
    (the `|` operator).

re.match(*pattern*, *string*, *flags=0*)[¶](https://docs.python.org/3/library/re.html#re.match "Link to this definition")
:   If zero or more characters at the beginning of *string* match the regular
    expression *pattern*, return a corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return
    `None` if the string does not match the pattern; note that this is
    different from a zero-length match.

    Note that even in [`MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE "re.MULTILINE") mode, [`re.match()`](https://docs.python.org/3/library/re.html#re.match "re.match") will only match
    at the beginning of the string and not at the beginning of each line.

    If you want to locate a match anywhere in *string*, use [`search()`](https://docs.python.org/3/library/re.html#re.search "re.search")
    instead (see also [search() vs. match()](https://docs.python.org/3/library/re.html#search-vs-match)).

    The expression’s behaviour can be modified by specifying a *flags* value.
    Values can be any of the [flags](https://docs.python.org/3/library/re.html#flags) variables, combined using bitwise OR
    (the `|` operator).

re.fullmatch(*pattern*, *string*, *flags=0*)[¶](https://docs.python.org/3/library/re.html#re.fullmatch "Link to this definition")
:   If the whole *string* matches the regular expression *pattern*, return a
    corresponding [`Match`](https://docs.python.org/3/library/re.html#re.Match "re.Match"). Return `None` if the string does not match
    the pattern; note that this is different from a zero-length match.

    The expression’s behaviour can be modified by spec