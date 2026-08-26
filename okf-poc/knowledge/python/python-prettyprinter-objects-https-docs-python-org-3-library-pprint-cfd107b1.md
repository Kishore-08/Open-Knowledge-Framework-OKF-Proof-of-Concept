---
id: python-prettyprinter-objects-https-docs-python-org-3-library-pprint-cfd107b1
type: concept
title: PrettyPrinter Objects[¶](https://docs.python.org/3/library/pprint.html#prettyprinter-objects
  "Link to this heading")
description: '*class* pprint.PrettyPrinter(*indent=1*, *width=80*, *depth=None*, *stream=None*,
  *\**, *compact=False*, *sort\_dicts=True*, *underscore\_numbers=False*)[¶](https://docs.python.org/3/library/pprint.ht'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pprint.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## PrettyPrinter Objects[¶](https://docs.python.org/3/library/pprint.html#prettyprinter-objects "Link to this heading")

*class* pprint.PrettyPrinter(*indent=1*, *width=80*, *depth=None*, *stream=None*, *\**, *compact=False*, *sort\_dicts=True*, *underscore\_numbers=False*)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "Link to this definition")
:   Construct a `PrettyPrinter` instance.

    Arguments have the same meaning as for [`pp()`](https://docs.python.org/3/library/pprint.html#pprint.pp "pprint.pp").
    Note that they are in a different order, and that *sort\_dicts* defaults to `True`.

    ```
    >>> import pprint
    >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    >>> stuff.insert(0, stuff[:])
    >>> pp = pprint.PrettyPrinter(indent=4)
    >>> pp.pprint(stuff)
    [   ['spam', 'eggs', 'lumberjack', 'knights', 'ni'],
        'spam',
        'eggs',
        'lumberjack',
        'knights',
        'ni']
    >>> pp = pprint.PrettyPrinter(width=41, compact=True)
    >>> pp.pprint(stuff)
    [['spam', 'eggs', 'lumberjack',
      'knights', 'ni'],
     'spam', 'eggs', 'lumberjack', 'knights',
     'ni']
    >>> tup = ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead',
    ... ('parrot', ('fresh fruit',))))))))
    >>> pp = pprint.PrettyPrinter(depth=6)
    >>> pp.pprint(tup)
    ('spam', ('eggs', ('lumberjack', ('knights', ('ni', ('dead', (...)))))))
    ```

    Changed in version 3.4: Added the *compact* parameter.

    Changed in version 3.8: Added the *sort\_dicts* parameter.

    Changed in version 3.10: Added the *underscore\_numbers* parameter.

    Changed in version 3.11: No longer attempts to write to `sys.stdout` if it is `None`.

[`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") instances have the following methods:

PrettyPrinter.pformat(*object*)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.pformat "Link to this definition")
:   Return the formatted representation of *object*. This takes into account the
    options passed to the [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") constructor.

PrettyPrinter.pprint(*object*)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.pprint "Link to this definition")
:   Print the formatted representation of *object* on the configured stream,
    followed by a newline.

The following methods provide the implementations for the corresponding
functions of the same names. Using these methods on an instance is slightly
more efficient since new [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") objects don’t need to be
created.

PrettyPrinter.isreadable(*object*)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.isreadable "Link to this definition")
:   Determine if the formatted representation of the object is “readable,” or can be
    used to reconstruct the value using [`eval()`](https://docs.python.org/3/library/functions.html#eval "eval"). Note that this returns
    `False` for recursive objects. If the *depth* parameter of the
    [`PrettyPrinter`](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter "pprint.PrettyPrinter") is set and the object is deeper than allowed, this
    returns `False`.

PrettyPrinter.isrecursive(*object*)[¶](https://docs.python.org/3/library/pprint.html#pprint.PrettyPrinter.isrecursive "Link to this definition")
:   Determine if the object requires a recursive representation.

This method is provided as a hook to allow subclasses to modify the way objects
are converted to strings. The default implementation uses the internals of the
[`saferepr()`](https://docs.python.org/3/library/pprint.html#pprint.saferepr "pprint.saferepr") implementation.

PrettyPrinter.format(*object*, *context*, *maxlevels*, *level*)[¶](https://docs.python.org/3/library/p