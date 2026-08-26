---
id: python-curses-terminal-handling-for-character-cell-displays-https-d-4272fbc3
type: concept
title: '`curses` — Terminal handling for character-cell displays[¶](https://docs.python.'
description: '**Source code:** [Lib/curses](https://github.com/python/cpython/tree/3.14/Lib/curses)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/curses.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `curses` — Terminal handling for character-cell displays[¶](https://docs.python.org/3/library/curses.html#module-curses "Link to this heading")

**Source code:** [Lib/curses](https://github.com/python/cpython/tree/3.14/Lib/curses)

---

The `curses` module provides an interface to the curses library, the
de-facto standard for portable advanced terminal handling.

While curses is most widely used in the Unix environment, versions are available
for Windows, DOS, and possibly other systems as well. This extension module is
designed to match the API of ncurses, an open-source curses library hosted on
Linux and the BSD variants of Unix.

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

Whenever the documentation mentions a *character* it can be specified
as an integer, a one-character Unicode string or a one-byte byte string.

Whenever the documentation mentions a *character string* it can be specified
as a Unicode string or a byte string.

Note

Whether curses may be used from several threads
depends on the underlying library and how it was built.
In many implementations, including the default build of ncurses,
the screen state is shared and not thread-safe;
since the blocking and refresh methods
(such as [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch") and [`refresh()`](https://docs.python.org/3/library/curses.html#curses.window.refresh "curses.window.refresh"))
release the [GIL](https://docs.python.org/3/glossary.html#term-GIL),
unsynchronized use from several threads can then crash the interpreter.
Serialize the calls.

See also

Module [`curses.ascii`](https://docs.python.org/3/library/curses.ascii.html#module-curses.ascii "curses.ascii: Constants and set-membership functions for ASCII characters.")
:   Utilities for working with ASCII characters, regardless of your locale settings.

Module [`curses.panel`](https://docs.python.org/3/library/curses.panel.html#module-curses.panel "curses.panel: A panel stack extension that adds depth to curses windows.")
:   A panel stack extension that adds depth to curses windows.

Module [`curses.textpad`](https://docs.python.org/3/library/curses.html#module-curses.textpad "curses.textpad: Emacs-like input editing in a curses window.")
:   Editable text widget for curses supporting **Emacs**-like bindings.

[Curses Programming with Python](https://docs.python.org/3/howto/curses.html#curses-howto)
:   Tutorial material on using curses with Python, by Andrew Kuchling and Eric
    Raymond.