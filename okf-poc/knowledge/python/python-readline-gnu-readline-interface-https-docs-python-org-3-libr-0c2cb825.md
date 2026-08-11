---
id: python-readline-gnu-readline-interface-https-docs-python-org-3-libr-0c2cb825
type: concept
title: '`readline` — GNU readline interface[¶](https://docs.python.org/3/library/readlin'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/readline.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `readline` — GNU readline interface[¶](https://docs.python.org/3/library/readline.html#module-readline "Link to this heading")

---

The `readline` module defines a number of functions to facilitate
completion and reading/writing of history files from the Python interpreter.
This module can be used directly, or via the [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.") module, which
supports completion of Python identifiers at the interactive prompt. Settings
made using this module affect the behaviour of both the interpreter’s
interactive prompt and the prompts offered by the built-in [`input()`](https://docs.python.org/3/library/functions.html#input "input")
function.

Readline keybindings may be configured via an initialization file, typically
`.inputrc` in your home directory. See [Readline Init File](https://tiswww.cwru.edu/php/chet/readline/rluserman.html#Readline-Init-File)
in the GNU Readline manual for information about the format and
allowable constructs of that file, and the capabilities of the
Readline library in general.

[Availability](https://docs.python.org/3/library/intro.html#availability): not Android, not iOS, not WASI.

This module is not supported on [mobile platforms](https://docs.python.org/3/library/intro.html#mobile-availability)
or [WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability).

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).

[Availability](https://docs.python.org/3/library/intro.html#availability): Unix.

Note

The underlying Readline library API may be implemented by
the `editline` (`libedit`) library instead of GNU readline.
On macOS the `readline` module detects which library is being used
at run time.

The configuration file for `editline` is different from that
of GNU readline. If you programmatically load configuration strings
you can use [`backend`](https://docs.python.org/3/library/readline.html#readline.backend "readline.backend") to determine which library is being used.

If you use `editline`/`libedit` readline emulation on macOS, the
initialization file located in your home directory is named
`.editrc`. For example, the following content in `~/.editrc` will
turn ON *vi* keybindings and TAB completion:

```
python:bind -v
python:bind ^I rl_complete
```

Also note that different libraries may use different history file formats.
When switching the underlying library, existing history files may become
unusable.

readline.backend[¶](https://docs.python.org/3/library/readline.html#readline.backend "Link to this definition")
:   The name of the underlying Readline library being used, either
    `"readline"` or `"editline"`.

    Added in version 3.13.