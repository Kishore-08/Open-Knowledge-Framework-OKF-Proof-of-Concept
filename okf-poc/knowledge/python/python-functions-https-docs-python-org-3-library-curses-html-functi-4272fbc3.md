---
id: python-functions-https-docs-python-org-3-library-curses-html-functi-4272fbc3
type: concept
title: Functions[¶](https://docs.python.org/3/library/curses.html#functions "Link
  to this heading")
description: 'The module `curses` defines the following exception:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/curses.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Functions[¶](https://docs.python.org/3/library/curses.html#functions "Link to this heading")

The module `curses` defines the following exception:

*exception* curses.error[¶](https://docs.python.org/3/library/curses.html#curses.error "Link to this definition")
:   Exception raised when a curses library function returns an error.

Note

Whenever *x* or *y* arguments to a function or a method are optional, they
default to the current cursor location. Whenever *attr* is optional, it defaults
to [`A_NORMAL`](https://docs.python.org/3/library/curses.html#curses.A_NORMAL "curses.A_NORMAL").

The module `curses` defines the following functions:

curses.assume\_default\_colors(*fg*, *bg*, */*)[¶](https://docs.python.org/3/library/curses.html#curses.assume_default_colors "Link to this definition")
:   Allow use of default values for colors on terminals supporting this feature.
    Use this to support transparency in your application.

    - Assign terminal default foreground/background colors to color number `-1`.
      So `init_pair(x, COLOR_RED, -1)` will initialize pair *x* as red
      on default background and `init_pair(x, -1, COLOR_BLUE)` will
      initialize pair *x* as default foreground on blue.
    - Change the definition of the color-pair `0` to `(fg, bg)`.

    This is an ncurses extension.

    Added in version 3.14.

curses.baudrate()[¶](https://docs.python.org/3/library/curses.html#curses.baudrate "Link to this definition")
:   Return the output speed of the terminal in bits per second. On software
    terminal emulators it will have a fixed high value. Included for historical
    reasons; in former times, it was used to write output loops for time delays and
    occasionally to change interfaces depending on the line speed.

curses.beep()[¶](https://docs.python.org/3/library/curses.html#curses.beep "Link to this definition")
:   Emit a short attention sound.

curses.can\_change\_color()[¶](https://docs.python.org/3/library/curses.html#curses.can_change_color "Link to this definition")
:   Return `True` or `False`, depending on whether the programmer can change the colors
    displayed by the terminal.

curses.cbreak()[¶](https://docs.python.org/3/library/curses.html#curses.cbreak "Link to this definition")
:   Enter cbreak mode. In cbreak mode (sometimes called “rare” mode) normal tty
    line buffering is turned off and characters are available to be read one by one.
    However, unlike raw mode, special characters (interrupt, quit, suspend, and flow
    control) retain their effects on the tty driver and calling program. Calling
    first [`raw()`](https://docs.python.org/3/library/curses.html#curses.raw "curses.raw") then `cbreak()` leaves the terminal in cbreak mode.

curses.color\_content(*color\_number*)[¶](https://docs.python.org/3/library/curses.html#curses.color_content "Link to this definition")
:   Return the intensity of the red, green, and blue (RGB) components in the color
    *color\_number*, which must be between `0` and `COLORS - 1`. Return a 3-tuple,
    containing the R,G,B values for the given color, which will be between
    `0` (no component) and `1000` (maximum amount of component). Raise an
    exception if the color is not supported.

curses.color\_pair(*pair\_number*)[¶](https://docs.python.org/3/library/curses.html#curses.color_pair "Link to this definition")
:   Return the attribute value for displaying text in the specified color pair.
    Only the first 256 color pairs are supported. This
    attribute value can be combined with [`A_STANDOUT`](https://docs.python.org/3/library/curses.html#curses.A_STANDOUT "curses.A_STANDOUT"), [`A_REVERSE`](https://docs.python.org/3/library/curses.html#curses.A_REVERSE "curses.A_REVERSE"),
    and the other `A_*` attributes. [`pair_number()`](https://docs.python.org/3/library/curses.html#curses.pair_number "curses.pair_number") is the counterpart
    to this function.

curses.curs\_set(*visibility*)[¶](https://docs.python.org/3/library/curses.html#cu