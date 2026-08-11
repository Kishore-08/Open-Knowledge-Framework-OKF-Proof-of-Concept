---
id: python-history-list-https-docs-python-org-3-library-readline-html-h-0c2cb825
type: concept
title: History list[¶](https://docs.python.org/3/library/readline.html#history-list
  "Link to this heading")
description: 'The following functions operate on a global history list:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/readline.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## History list[¶](https://docs.python.org/3/library/readline.html#history-list "Link to this heading")

The following functions operate on a global history list:

readline.clear\_history()[¶](https://docs.python.org/3/library/readline.html#readline.clear_history "Link to this definition")
:   Clear the current history. This calls `clear_history()` in the
    underlying library. The Python function only exists if Python was
    compiled for a version of the library that supports it.

readline.get\_current\_history\_length()[¶](https://docs.python.org/3/library/readline.html#readline.get_current_history_length "Link to this definition")
:   Return the number of items currently in the history. (This is different from
    [`get_history_length()`](https://docs.python.org/3/library/readline.html#readline.get_history_length "readline.get_history_length"), which returns the maximum number of lines that will
    be written to a history file.)

readline.get\_history\_item(*index*)[¶](https://docs.python.org/3/library/readline.html#readline.get_history_item "Link to this definition")
:   Return the current contents of history item at *index*. The item index
    is one-based. This calls `history_get()` in the underlying library.

readline.remove\_history\_item(*pos*)[¶](https://docs.python.org/3/library/readline.html#readline.remove_history_item "Link to this definition")
:   Remove history item specified by its position from the history.
    The position is zero-based. This calls `remove_history()` in
    the underlying library.

readline.replace\_history\_item(*pos*, *line*)[¶](https://docs.python.org/3/library/readline.html#readline.replace_history_item "Link to this definition")
:   Replace history item specified by its position with *line*.
    The position is zero-based. This calls `replace_history_entry()`
    in the underlying library.

readline.add\_history(*line*)[¶](https://docs.python.org/3/library/readline.html#readline.add_history "Link to this definition")
:   Append *line* to the history buffer, as if it was the last line typed.
    This calls `add_history()` in the underlying library.

readline.set\_auto\_history(*enabled*)[¶](https://docs.python.org/3/library/readline.html#readline.set_auto_history "Link to this definition")
:   Enable or disable automatic calls to `add_history()` when reading
    input via readline. The *enabled* argument should be a Boolean value
    that when true, enables auto history, and that when false, disables
    auto history.

    Added in version 3.6.

    **CPython implementation detail:** Auto history is enabled by default, and changes to this do not persist
    across multiple sessions.