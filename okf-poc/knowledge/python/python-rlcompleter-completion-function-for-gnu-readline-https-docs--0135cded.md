---
id: python-rlcompleter-completion-function-for-gnu-readline-https-docs--0135cded
type: concept
title: '`rlcompleter` — Completion function for GNU readline[¶](https://docs.python.org/'
description: '**Source code:** [Lib/rlcompleter.py](https://github.com/python/cpython/tree/3.14/Lib/rlcompleter.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/rlcompleter.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `rlcompleter` — Completion function for GNU readline[¶](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "Link to this heading")

**Source code:** [Lib/rlcompleter.py](https://github.com/python/cpython/tree/3.14/Lib/rlcompleter.py)

---

The `rlcompleter` module defines a completion function suitable to be
passed to [`set_completer()`](https://docs.python.org/3/library/readline.html#readline.set_completer "readline.set_completer") in the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module.

When this module is imported on a Unix platform with the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module
available, an instance of the [`Completer`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "rlcompleter.Completer") class is automatically created
and its [`complete()`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer.complete "rlcompleter.Completer.complete") method is set as the
[readline completer](https://docs.python.org/3/library/readline.html#readline-completion). The method provides
completion of valid Python [identifiers and keywords](https://docs.python.org/3/reference/lexical_analysis.html#identifiers).

Example:

```
>>> import rlcompleter
>>> import readline
>>> readline.parse_and_bind("tab: complete")
>>> readline. <TAB PRESSED>
readline.__doc__          readline.get_line_buffer(  readline.read_init_file(
readline.__file__         readline.insert_text(      readline.set_completer(
readline.__name__         readline.parse_and_bind(
>>> readline.
```

The `rlcompleter` module is designed for use with Python’s
[interactive mode](https://docs.python.org/3/tutorial/interpreter.html#tut-interactive). Unless Python is run with the
[`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) option, the module is automatically imported and configured
(see [Readline configuration](https://docs.python.org/3/library/site.html#rlcompleter-config)).

On platforms without [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python."), the [`Completer`](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "rlcompleter.Completer") class defined by
this module can still be used for custom purposes.

*class* rlcompleter.Completer[¶](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer "Link to this definition")
:   Completer objects have the following method:

    complete(*text*, *state*)[¶](https://docs.python.org/3/library/rlcompleter.html#rlcompleter.Completer.complete "Link to this definition")
    :   Return the next possible completion for *text*.

        When called by the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.") module, this method is called
        successively with `state == 0, 1, 2, ...` until the method returns
        `None`.

        If called for *text* that doesn’t include a period character (`'.'`), it will
        complete from names currently defined in [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``."), [`builtins`](https://docs.python.org/3/library/builtins.html#module-builtins "builtins: The module that provides the built-in namespace.") and
        keywords (as defined by the [`keyword`](https://docs.python.org/3/library/keyword.html#module-keyword "keyword: Test whether a string is a keyword in Python.") module).

        If called for a dotted name, it will try to evaluate anything without obvious
        side-effects (functions will not be evaluated, but it can generate calls to
        [`__getattr__()`](https://docs.python.org/3/refere