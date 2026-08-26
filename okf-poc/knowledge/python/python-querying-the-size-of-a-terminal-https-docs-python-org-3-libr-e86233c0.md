---
id: python-querying-the-size-of-a-terminal-https-docs-python-org-3-libr-e86233c0
type: concept
title: Querying the size of a terminal[¶](https://docs.python.org/3/library/os.html#querying-the-size-of-a-terminal
  "Link to this heading")
description: Added in version 3.3.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/os.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Querying the size of a terminal[¶](https://docs.python.org/3/library/os.html#querying-the-size-of-a-terminal "Link to this heading")

Added in version 3.3.

os.get\_terminal\_size(*fd=STDOUT\_FILENO*, */*)[¶](https://docs.python.org/3/library/os.html#os.get_terminal_size "Link to this definition")
:   Return the size of the terminal window as `(columns, lines)`,
    tuple of type [`terminal_size`](https://docs.python.org/3/library/os.html#os.terminal_size "os.terminal_size").

    The optional argument `fd` (default `STDOUT_FILENO`, or standard
    output) specifies which file descriptor should be queried.

    If the file descriptor is not connected to a terminal, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError")
    is raised.

    [`shutil.get_terminal_size()`](https://docs.python.org/3/library/shutil.html#shutil.get_terminal_size "shutil.get_terminal_size") is the high-level function which
    should normally be used, `os.get_terminal_size` is the low-level
    implementation.

    [Availability](https://docs.python.org/3/library/intro.html#availability): Unix, Windows.

*class* os.terminal\_size[¶](https://docs.python.org/3/library/os.html#os.terminal_size "Link to this definition")
:   A subclass of tuple, holding `(columns, lines)` of the terminal window size.

    columns[¶](https://docs.python.org/3/library/os.html#os.terminal_size.columns "Link to this definition")
    :   Width of the terminal window in characters.

    lines[¶](https://docs.python.org/3/library/os.html#os.terminal_size.lines "Link to this definition")
    :   Height of the terminal window in characters.