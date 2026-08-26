---
id: python-defining-a-callback-option-https-docs-python-org-3-library-o-f59a6996
type: concept
title: Defining a callback option[¶](https://docs.python.org/3/library/optparse.html#defining-a-callback-option
  "Link to this heading")
description: As always, the easiest way to define a callback option is by using the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Defining a callback option[¶](https://docs.python.org/3/library/optparse.html#defining-a-callback-option "Link to this heading")

As always, the easiest way to define a callback option is by using the
[`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option") method. Apart from [`action`](https://docs.python.org/3/library/optparse.html#optparse.Option.action "optparse.Option.action"), the
only option attribute you must specify is `callback`, the function to call:

```
parser.add_option("-c", action="callback", callback=my_callback)
```

`callback` is a function (or other callable object), so you must have already
defined `my_callback()` when you create this callback option. In this simple
case, `optparse` doesn’t even know if `-c` takes any arguments,
which usually means that the option takes no arguments—the mere presence of
`-c` on the command-line is all it needs to know. In some
circumstances, though, you might want your callback to consume an arbitrary
number of command-line arguments. This is where writing callbacks gets tricky;
it’s covered later in this section.

`optparse` always passes four particular arguments to your callback, and it
will only pass additional arguments if you specify them via
[`callback_args`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_args "optparse.Option.callback_args") and [`callback_kwargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_kwargs "optparse.Option.callback_kwargs"). Thus, the
minimal callback function signature is:

```
def my_callback(option, opt, value, parser):
```

The four arguments to a callback are described below.

There are several other option attributes that you can supply when you define a
callback option:

[`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type")
:   has its usual meaning: as with the `"store"` or `"append"` actions, it
    instructs `optparse` to consume one argument and convert it to
    [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"). Rather than storing the converted value(s) anywhere,
    though, `optparse` passes it to your callback function.

[`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs")
:   also has its usual meaning: if it is supplied and > 1, `optparse` will
    consume [`nargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "optparse.Option.nargs") arguments, each of which must be convertible to
    [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"). It then passes a tuple of converted values to your
    callback.

[`callback_args`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_args "optparse.Option.callback_args")
:   a tuple of extra positional arguments to pass to the callback

[`callback_kwargs`](https://docs.python.org/3/library/optparse.html#optparse.Option.callback_kwargs "optparse.Option.callback_kwargs")
:   a dictionary of extra keyword arguments to pass to the callback