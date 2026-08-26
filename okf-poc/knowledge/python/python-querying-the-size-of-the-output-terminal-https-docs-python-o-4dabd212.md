---
id: python-querying-the-size-of-the-output-terminal-https-docs-python-o-4dabd212
type: concept
title: Querying the size of the output terminal[¶](https://docs.python.org/3/library/shutil.html#querying-the-size-of-the-output-terminal
  "Link to this heading")
description: shutil.get\_terminal\_size(*fallback=(columns, lines)*)[¶](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shutil.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Querying the size of the output terminal[¶](https://docs.python.org/3/library/shutil.html#querying-the-size-of-the-output-terminal "Link to this heading")

shutil.get\_terminal\_size(*fallback=(columns, lines)*)[¶](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size "Link to this definition")
:   Get the size of the terminal window.

    For each of the two dimensions, the environment variable, `COLUMNS`
    and `LINES` respectively, is checked. If the variable is defined and
    the value is a positive integer, it is used.

    When `COLUMNS` or `LINES` is not defined, which is the common case,
    the terminal connected to [`sys.__stdout__`](https://docs.python.org/3/library/sys.html#sys.__stdout__ "sys.__stdout__") is queried
    by invoking [`os.get_terminal_size()`](https://docs.python.org/3/library/os.html#os.get_terminal_size "os.get_terminal_size").

    If the terminal size cannot be successfully queried, either because
    the system doesn’t support querying, or because we are not
    connected to a terminal, the value given in `fallback` parameter
    is used. `fallback` defaults to `(80, 24)` which is the default
    size used by many terminal emulators.

    The value returned is a named tuple of type [`os.terminal_size`](https://docs.python.org/3/library/os.html#os.terminal_size "os.terminal_size").

    See also: The Single UNIX Specification, Version 2,
    [Other Environment Variables](https://pubs.opengroup.org/onlinepubs/7908799/xbd/envvar.html#tag_002_003).

    Added in version 3.3.

    Changed in version 3.11: The `fallback` values are also used if [`os.get_terminal_size()`](https://docs.python.org/3/library/os.html#os.get_terminal_size "os.get_terminal_size")
    returns zeroes.