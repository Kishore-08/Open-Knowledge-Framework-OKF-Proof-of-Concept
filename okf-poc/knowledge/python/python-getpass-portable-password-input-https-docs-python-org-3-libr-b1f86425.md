---
id: python-getpass-portable-password-input-https-docs-python-org-3-libr-b1f86425
type: concept
title: '`getpass` — Portable password input[¶](https://docs.python.org/3/library/getpass'
description: '**Source code:** [Lib/getpass.py](https://github.com/python/cpython/tree/3.14/Lib/getpass.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/getpass.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `getpass` — Portable password input[¶](https://docs.python.org/3/library/getpass.html#module-getpass "Link to this heading")

**Source code:** [Lib/getpass.py](https://github.com/python/cpython/tree/3.14/Lib/getpass.py)

---

[Availability](https://docs.python.org/3/library/intro.html#availability): not WASI.

This module does not work or is not available on WebAssembly. See
[WebAssembly platforms](https://docs.python.org/3/library/intro.html#wasm-availability) for more information.

The `getpass` module provides two functions:

getpass.getpass(*prompt='Password: '*, *stream=None*, *\**, *echo\_char=None*)[¶](https://docs.python.org/3/library/getpass.html#getpass.getpass "Link to this definition")
:   Prompt the user for a password without echoing. The user is prompted using
    the string *prompt*, which defaults to `'Password: '`. On Unix, the
    prompt is written to the file-like object *stream* using the replace error
    handler if needed. *stream* defaults to the controlling terminal
    (`/dev/tty`) or if that is unavailable to `sys.stderr` (this
    argument is ignored on Windows).

    The *echo\_char* argument controls how user input is displayed while typing.
    If *echo\_char* is `None` (default), input remains hidden. Otherwise,
    *echo\_char* must be a single printable ASCII character and each
    typed character is replaced by it. For example, `echo_char='*'` will
    display asterisks instead of the actual input.

    If echo free input is unavailable getpass() falls back to printing
    a warning message to *stream* and reading from `sys.stdin` and
    issuing a [`GetPassWarning`](https://docs.python.org/3/library/getpass.html#getpass.GetPassWarning "getpass.GetPassWarning").

    Note

    If you call getpass from within IDLE, the input may be done in the
    terminal you launched IDLE from rather than the idle window itself.

    Note

    On Unix systems, when *echo\_char* is set, the terminal will be
    configured to operate in
    *[noncanonical mode](https://manpages.debian.org/termios(3)#Canonical_and_noncanonical_mode)*.
    In particular, this means that line editing shortcuts such as
    `Ctrl`+`U` will not work and may insert unexpected characters into
    the input.

    Changed in version 3.14: Added the *echo\_char* parameter for keyboard feedback.

*exception* getpass.GetPassWarning[¶](https://docs.python.org/3/library/getpass.html#getpass.GetPassWarning "Link to this definition")
:   A [`UserWarning`](https://docs.python.org/3/library/exceptions.html#UserWarning "UserWarning") subclass issued when password input may be echoed.

getpass.getuser()[¶](https://docs.python.org/3/library/getpass.html#getpass.getuser "Link to this definition")
:   Return the “login name” of the user.

    This function checks the environment variables `LOGNAME`,
    `USER`, `LNAME` and `USERNAME`, in order, and
    returns the value of the first one which is set to a non-empty string. If
    none are set, the login name from the password database is returned on
    systems which support the [`pwd`](https://docs.python.org/3/library/pwd.html#module-pwd "pwd: The password database (getpwnam() and friends).") module, otherwise, an [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError")
    is raised.

    In general, this function should be preferred over [`os.getlogin()`](https://docs.python.org/3/library/os.html#os.getlogin "os.getlogin").

    Changed in version 3.13: Previously, various exceptions beyond just [`OSError`](https://docs.python.org/3/library/exceptions.html#OSError "OSError") were raised.