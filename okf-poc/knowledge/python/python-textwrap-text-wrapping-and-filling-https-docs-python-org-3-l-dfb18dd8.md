---
id: python-textwrap-text-wrapping-and-filling-https-docs-python-org-3-l-dfb18dd8
type: concept
title: '`textwrap` — Text wrapping and filling[¶](https://docs.python.org/3/library/text'
description: '**Source code:** [Lib/textwrap.py](https://github.com/python/cpython/tree/3.14/Lib/textwrap.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/textwrap.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `textwrap` — Text wrapping and filling[¶](https://docs.python.org/3/library/textwrap.html#module-textwrap "Link to this heading")

**Source code:** [Lib/textwrap.py](https://github.com/python/cpython/tree/3.14/Lib/textwrap.py)

---

The `textwrap` module provides some convenience functions,
as well as [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper"), the class that does all the work.
If you’re just wrapping or filling one or two text strings, the convenience
functions should be good enough; otherwise, you should use an instance of
`TextWrapper` for efficiency.

textwrap.wrap(*text*, *width=70*, *\**, *initial\_indent=''*, *subsequent\_indent=''*, *expand\_tabs=True*, *replace\_whitespace=True*, *fix\_sentence\_endings=False*, *break\_long\_words=True*, *drop\_whitespace=True*, *break\_on\_hyphens=True*, *tabsize=8*, *max\_lines=None*, *placeholder=' [...]'*)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "Link to this definition")
:   Wraps the single paragraph in *text* (a string) so every line is at most
    *width* characters long. Returns a list of output lines, without final
    newlines.

    Optional keyword arguments correspond to the instance attributes of
    [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper"), documented below.

    See the [`TextWrapper.wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.wrap "textwrap.TextWrapper.wrap") method for additional details on how
    `wrap()` behaves.

textwrap.fill(*text*, *width=70*, *\**, *initial\_indent=''*, *subsequent\_indent=''*, *expand\_tabs=True*, *replace\_whitespace=True*, *fix\_sentence\_endings=False*, *break\_long\_words=True*, *drop\_whitespace=True*, *break\_on\_hyphens=True*, *tabsize=8*, *max\_lines=None*, *placeholder=' [...]'*)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.fill "Link to this definition")
:   Wraps the single paragraph in *text*, and returns a single string containing the
    wrapped paragraph. `fill()` is shorthand for

    ```
    "\n".join(wrap(text, ...))
    ```

    In particular, `fill()` accepts exactly the same keyword arguments as
    [`wrap()`](https://docs.python.org/3/library/textwrap.html#textwrap.wrap "textwrap.wrap").

textwrap.shorten(*text*, *width*, *\**, *fix\_sentence\_endings=False*, *break\_long\_words=True*, *break\_on\_hyphens=True*, *placeholder=' [...]'*)[¶](https://docs.python.org/3/library/textwrap.html#textwrap.shorten "Link to this definition")
:   Collapse and truncate the given *text* to fit in the given *width*.

    First the whitespace in *text* is collapsed (all whitespace is replaced by
    single spaces). If the result fits in the *width*, it is returned.
    Otherwise, enough words are dropped from the end so that the remaining words
    plus the *placeholder* fit within *width*:

    ```
    >>> textwrap.shorten("Hello  world!", width=12)
    'Hello world!'
    >>> textwrap.shorten("Hello  world!", width=11)
    'Hello [...]'
    >>> textwrap.shorten("Hello world", width=10, placeholder="...")
    'Hello...'
    ```

    Optional keyword arguments correspond to the instance attributes of
    [`TextWrapper`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper "textwrap.TextWrapper"), documented below. Note that the whitespace is
    collapsed before the text is passed to the `TextWrapper` [`fill()`](https://docs.python.org/3/library/textwrap.html#textwrap.fill "textwrap.fill")
    function, so changing the value of [`tabsize`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.tabsize "textwrap.TextWrapper.tabsize"), [`expand_tabs`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.expand_tabs "textwrap.TextWrapper.expand_tabs"),
    [`drop_whitespace`](https://docs.python.org/3/library/textwrap.html#textwrap.TextWrapper.drop_whitespace "textwrap.TextWrapper.drop_whit