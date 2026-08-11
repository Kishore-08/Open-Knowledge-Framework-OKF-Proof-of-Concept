---
id: python-example-https-docs-python-org-3-library-readline-html-exampl-0c2cb825
type: concept
title: Example[¶](https://docs.python.org/3/library/readline.html#example "Link to
  this heading")
description: The following example demonstrates how to use the `readline` module’s
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/readline.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Example[¶](https://docs.python.org/3/library/readline.html#example "Link to this heading")

The following example demonstrates how to use the `readline` module’s
history reading and writing functions to automatically load and save a history
file named `.python_history` from the user’s home directory. The code
below would normally be executed automatically during interactive sessions
from the user’s [`PYTHONSTARTUP`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONSTARTUP) file.

```
import atexit
import os
import readline

histfile = os.path.join(os.path.expanduser("~"), ".python_history")
try:
    readline.read_history_file(histfile)
    # default history len is -1 (infinite), which may grow unruly
    readline.set_history_length(1000)
except FileNotFoundError:
    pass

atexit.register(readline.write_history_file, histfile)
```

This code is actually automatically run when Python is run in
[interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive) (see [Readline configuration](https://docs.python.org/3/library/site.html#rlcompleter-config)).

The following example achieves the same goal but supports concurrent interactive
sessions, by only appending the new history.

```
import atexit
import os
import readline
histfile = os.path.join(os.path.expanduser("~"), ".python_history")

try:
    readline.read_history_file(histfile)
    h_len = readline.get_current_history_length()
except FileNotFoundError:
    open(histfile, 'wb').close()
    h_len = 0

def save(prev_h_len, histfile):
    new_h_len = readline.get_current_history_length()
    readline.set_history_length(1000)
    readline.append_history_file(new_h_len - prev_h_len, histfile)
atexit.register(save, h_len, histfile)
```

The following example extends the [`code.InteractiveConsole`](https://docs.python.org/3/library/code.html#code.InteractiveConsole "code.InteractiveConsole") class to
support history save/restore.

```
import atexit
import code
import os
import readline

class HistoryConsole(code.InteractiveConsole):
    def __init__(self, locals=None, filename="<console>",
                 histfile=os.path.expanduser("~/.console-history")):
        code.InteractiveConsole.__init__(self, locals, filename)
        self.init_history(histfile)

    def init_history(self, histfile):
        readline.parse_and_bind("tab: complete")
        if hasattr(readline, "read_history_file"):
            try:
                readline.read_history_file(histfile)
            except FileNotFoundError:
                pass
            atexit.register(self.save_history, histfile)

    def save_history(self, histfile):
        readline.set_history_length(1000)
        readline.write_history_file(histfile)
```

Note

The new [REPL](https://docs.python.org/3/glossary.html#term-REPL) introduced in version 3.13 doesn’t support readline.
However, readline can still be used by setting the [`PYTHON_BASIC_REPL`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHON_BASIC_REPL)
environment variable.