---
id: python-history-file-https-docs-python-org-3-library-readline-html-h-0c2cb825
type: concept
title: History file[¶](https://docs.python.org/3/library/readline.html#history-file
  "Link to this heading")
description: 'The following functions operate on a history file:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/readline.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## History file[¶](https://docs.python.org/3/library/readline.html#history-file "Link to this heading")

The following functions operate on a history file:

readline.read\_history\_file([*filename*])[¶](https://docs.python.org/3/library/readline.html#readline.read_history_file "Link to this definition")
:   Load a readline history file, and append it to the history list.
    The default filename is `~/.history`. This calls
    `read_history()` in the underlying library
    and raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with the file
    name if given and `"~/.history"` otherwise.

    Changed in version 3.14: The auditing event was added.

readline.write\_history\_file([*filename*])[¶](https://docs.python.org/3/library/readline.html#readline.write_history_file "Link to this definition")
:   Save the history list to a readline history file, overwriting any
    existing file. The default filename is `~/.history`. This calls
    `write_history()` in the underlying library and raises an
    [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open` with the file name if given and
    `"~/.history"` otherwise.

    Changed in version 3.14: The auditing event was added.

readline.append\_history\_file(*nelements*[, *filename*])[¶](https://docs.python.org/3/library/readline.html#readline.append_history_file "Link to this definition")
:   Append the last *nelements* items of history to a file. The default filename is
    `~/.history`. The file must already exist. This calls
    `append_history()` in the underlying library. This function
    only exists if Python was compiled for a version of the library
    that supports it. It raises an [auditing event](https://docs.python.org/3/library/sys.html#auditing) `open`
    with the file name if given and `"~/.history"` otherwise.

    Added in version 3.5.

    Changed in version 3.14: The auditing event was added.

readline.get\_history\_length()[¶](https://docs.python.org/3/library/readline.html#readline.get_history_length "Link to this definition")

readline.set\_history\_length(*length*)[¶](https://docs.python.org/3/library/readline.html#readline.set_history_length "Link to this definition")
:   Set or return the desired number of lines to save in the history file.
    The [`write_history_file()`](https://docs.python.org/3/library/readline.html#readline.write_history_file "readline.write_history_file") function uses this value to truncate
    the history file, by calling `history_truncate_file()` in
    the underlying library. Negative values imply
    unlimited history file size.