---
id: python-window-objects-https-docs-python-org-3-library-curses-html-w-4272fbc3
type: concept
title: Window objects[¶](https://docs.python.org/3/library/curses.html#window-objects
  "Link to this heading")
description: '*class* curses.window[¶](https://docs.python.org/3/library/curses.html#curses.window
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/curses.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Window objects[¶](https://docs.python.org/3/library/curses.html#window-objects "Link to this heading")

*class* curses.window[¶](https://docs.python.org/3/library/curses.html#curses.window "Link to this definition")
:   Window objects, as returned by [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr") and [`newwin()`](https://docs.python.org/3/library/curses.html#curses.newwin "curses.newwin") above, have
    the following methods and attributes:

window.addch(*ch*[, *attr*])[¶](https://docs.python.org/3/library/curses.html#curses.window.addch "Link to this definition")

window.addch(*y*, *x*, *ch*[, *attr*])
:   Paint character *ch* at `(y, x)` with attributes *attr*, overwriting any
    character previously painted at that location. By default, the character
    position and attributes are the current settings for the window object.

    Note

    Writing outside the window, subwindow, or pad raises a [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error").
    Attempting to write to the lower-right corner of a window, subwindow,
    or pad will cause an exception to be raised after the character is printed.

window.addnstr(*str*, *n*[, *attr*])[¶](https://docs.python.org/3/library/curses.html#curses.window.addnstr "Link to this definition")

window.addnstr(*y*, *x*, *str*, *n*[, *attr*])
:   Paint at most *n* characters of the character string *str* at
    `(y, x)` with attributes
    *attr*, overwriting anything previously on the display.

window.addstr(*str*[, *attr*])[¶](https://docs.python.org/3/library/curses.html#curses.window.addstr "Link to this definition")

window.addstr(*y*, *x*, *str*[, *attr*])
:   Paint the character string *str* at `(y, x)` with attributes
    *attr*, overwriting anything previously on the display.

    Note

    - Writing outside the window, subwindow, or pad raises [`curses.error`](https://docs.python.org/3/library/curses.html#curses.error "curses.error").
      Attempting to write to the lower-right corner of a window, subwindow,
      or pad will cause an exception to be raised after the string is printed.
    - A bug in ncurses, the backend for this Python module, could cause
      segfaults when resizing windows. This was fixed in ncurses-6.1-20190511.
      If you are stuck with an earlier ncurses, you can avoid triggering it by
      not calling `addstr()` with a *str* that has embedded newlines;
      instead, call `addstr()` separately for each line.

window.attroff(*attr*)[¶](https://docs.python.org/3/library/curses.html#curses.window.attroff "Link to this definition")
:   Remove attribute *attr* from the “background” set applied to all writes to the
    current window.

window.attron(*attr*)[¶](https://docs.python.org/3/library/curses.html#curses.window.attron "Link to this definition")
:   Add attribute *attr* to the “background” set applied to all writes to the
    current window.

window.attrset(*attr*)[¶](https://docs.python.org/3/library/curses.html#curses.window.attrset "Link to this definition")
:   Set the “background” set of attributes to *attr*. This set is initially
    `0` (no attributes).

window.bkgd(*ch*[, *attr*])[¶](https://docs.python.org/3/library/curses.html#curses.window.bkgd "Link to this definition")
:   Set the background property of the window to the character *ch*, with
    attributes *attr*. The change is then applied to every character position in
    that window:

    - The attribute of every character in the window is changed to the new
      background attribute.
    - Wherever the former background character appears, it is changed to the new
      background character.

window.bkgdset(*ch*[, *attr*])[¶](https://docs.python.org/3/library/curses.html#curses.window.bkgdset "Link to this definition")
:   Set the window’s background. A window’s background consists of a character and
    any combination of attributes. The attribute part of the background is combined
    (OR’ed