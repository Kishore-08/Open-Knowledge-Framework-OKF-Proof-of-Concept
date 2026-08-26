---
id: python-constants-https-docs-python-org-3-library-curses-html-consta-4272fbc3
type: concept
title: Constants[¶](https://docs.python.org/3/library/curses.html#constants "Link
  to this heading")
description: 'The `curses` module defines the following data members:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/curses.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Constants[¶](https://docs.python.org/3/library/curses.html#constants "Link to this heading")

The `curses` module defines the following data members:

curses.ERR[¶](https://docs.python.org/3/library/curses.html#curses.ERR "Link to this definition")
:   Some curses routines that return an integer, such as [`getch()`](https://docs.python.org/3/library/curses.html#curses.window.getch "curses.window.getch"), return
    [`ERR`](https://docs.python.org/3/library/curses.html#curses.ERR "curses.ERR") upon failure.

curses.OK[¶](https://docs.python.org/3/library/curses.html#curses.OK "Link to this definition")
:   Some curses routines that return an integer, such as [`napms()`](https://docs.python.org/3/library/curses.html#curses.napms "curses.napms"), return
    [`OK`](https://docs.python.org/3/library/curses.html#curses.OK "curses.OK") upon success.

curses.version[¶](https://docs.python.org/3/library/curses.html#curses.version "Link to this definition")
:   A bytes object representing the current version of the module.

curses.ncurses\_version[¶](https://docs.python.org/3/library/curses.html#curses.ncurses_version "Link to this definition")
:   A named tuple containing the three components of the ncurses library
    version: *major*, *minor*, and *patch*. All values are integers. The
    components can also be accessed by name, so `curses.ncurses_version[0]`
    is equivalent to `curses.ncurses_version.major` and so on.

    Availability: if the ncurses library is used.

    Added in version 3.8.

curses.COLORS[¶](https://docs.python.org/3/library/curses.html#curses.COLORS "Link to this definition")
:   The maximum number of colors the terminal can support.
    It is defined only after the call to [`start_color()`](https://docs.python.org/3/library/curses.html#curses.start_color "curses.start_color").

curses.COLOR\_PAIRS[¶](https://docs.python.org/3/library/curses.html#curses.COLOR_PAIRS "Link to this definition")
:   The maximum number of color pairs the terminal can support.
    It is defined only after the call to [`start_color()`](https://docs.python.org/3/library/curses.html#curses.start_color "curses.start_color").

curses.COLS[¶](https://docs.python.org/3/library/curses.html#curses.COLS "Link to this definition")
:   The width of the screen, that is, the number of columns.
    It is defined only after the call to [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr").
    Updated by [`update_lines_cols()`](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "curses.update_lines_cols"), [`resizeterm()`](https://docs.python.org/3/library/curses.html#curses.resizeterm "curses.resizeterm") and
    [`resize_term()`](https://docs.python.org/3/library/curses.html#curses.resize_term "curses.resize_term").

curses.LINES[¶](https://docs.python.org/3/library/curses.html#curses.LINES "Link to this definition")
:   The height of the screen, that is, the number of lines.
    It is defined only after the call to [`initscr()`](https://docs.python.org/3/library/curses.html#curses.initscr "curses.initscr").
    Updated by [`update_lines_cols()`](https://docs.python.org/3/library/curses.html#curses.update_lines_cols "curses.update_lines_cols"), [`resizeterm()`](https://docs.python.org/3/library/curses.html#curses.resizeterm "curses.resizeterm") and
    [`resize_term()`](https://docs.python.org/3/library/curses.html#curses.resize_term "curses.resize_term").

Some constants are available to specify character cell attributes.
The exact constants available are system dependent.

| Attribute | Meaning |
| --- | --- |
| curses.A\_ALTCHARSET[¶](https://docs.python.org/3/library/curses.html#curses.A_ALTCHARSET "Link to this definition") | Alternate character set mode |
| curses.A\_BLINK[¶](https://docs.python.org/3/library/curses.html#curses.A_BLINK "Link to this definition") | Blink mode |
| curses.A\_BOLD[¶](https://docs.python.org/3/library/curses.html#curses.A_BOLD "Link to this definitio