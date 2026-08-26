---
id: python-textbox-objects-https-docs-python-org-3-library-curses-html--4272fbc3
type: concept
title: Textbox objects[¶](https://docs.python.org/3/library/curses.html#textbox-objects
  "Link to this heading")
description: 'You can instantiate a [`Textbox`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox
  "curses.textpad.Textbox") object as follows:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/curses.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Textbox objects[¶](https://docs.python.org/3/library/curses.html#textbox-objects "Link to this heading")

You can instantiate a [`Textbox`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox "curses.textpad.Textbox") object as follows:

*class* curses.textpad.Textbox(*win*, *insert\_mode=False*)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox "Link to this definition")
:   Return a textbox widget object. The *win* argument should be a curses
    [window](https://docs.python.org/3/library/curses.html#curses-window-objects) object in which the textbox is to
    be contained. If *insert\_mode* is true, the textbox inserts typed
    characters, shifting existing text to the right, rather than overwriting it.
    The edit cursor of the textbox is initially located at the
    upper-left corner of the containing window, with coordinates `(0, 0)`.
    The instance’s [`stripspaces`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces") flag is initially on.

    `Textbox` objects have the following methods:

    edit(*validate=None*)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.edit "Link to this definition")
    :   This is the entry point you will normally use. It accepts editing
        keystrokes until one of the termination keystrokes is entered. If
        *validate* is supplied, it must be a function. It will be called for
        each keystroke entered with the keystroke as a parameter; command dispatch
        is done on the result. If it returns a false value, the keystroke is
        ignored. This method returns the window contents as a
        string; whether blanks in the window are included is affected by the
        [`stripspaces`](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.stripspaces "curses.textpad.Textbox.stripspaces") attribute.

    do\_command(*ch*)[¶](https://docs.python.org/3/library/curses.html#curses.textpad.Textbox.do_command "Link to this definition")
    :   Process a single command keystroke. Returns `1` to continue editing,
        or `0` if a termination keystroke was processed. Here are the supported
        special keystrokes:

        | Keystroke | Action |
        | --- | --- |
        | `Control`-`A` | Go to left edge of window. |
        | `Control`-`B` | Cursor left, wrapping to previous line if appropriate. |
        | `Control`-`D` | Delete character under cursor. |
        | `Control`-`E` | Go to right edge (stripspaces off) or end of line (stripspaces on). |
        | `Control`-`F` | Cursor right, wrapping to next line when appropriate. |
        | `Control`-`G` | Terminate, returning the window contents. |
        | `Control`-`H` | Delete character backward. |
        | `Control`-`J` | Terminate if the window is 1 line, otherwise move to the start of the next line. |
        | `Control`-`K` | If line is blank, delete it, otherwise clear to end of line. |
        | `Control`-`L` | Refresh screen. |
        | `Control`-`N` | Cursor down; move down one line. |
        | `Control`-`O` | Insert a blank line at cursor location. |
        | `Control`-`P` | Cursor up; move up one line. |

        Move operations do nothing if the cursor is at an edge where the movement
        is not possible. The following synonyms are supported where possible:

        | Constant | Keystroke |
        | --- | --- |
        | [`KEY_LEFT`](https://docs.python.org/3/library/curses.html#curses.KEY_LEFT "curses.KEY_LEFT") | `Control`-`B` |
        | [`KEY_RIGHT`](https://docs.python.org/3/library/curses.html#curses.KEY_RIGHT "curses.KEY_RIGHT") | `Control`-`F` |
        | [`KEY_UP`](https://docs.python.org/3/library/curses.html#curses.KEY_UP "curses.KEY_UP") | `Control`-`P` |
        | [`KEY_DOWN`](https://docs.python.org/3/library/curses.html#curses.KEY_DOWN "curses.KEY_DOWN") | `Control`-`N` |
        | [`KEY_BACKSPACE`](https://docs.python.org/3/library/cur