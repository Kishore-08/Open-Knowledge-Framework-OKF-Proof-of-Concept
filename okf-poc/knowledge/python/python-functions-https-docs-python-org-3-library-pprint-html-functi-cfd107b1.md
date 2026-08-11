---
id: python-functions-https-docs-python-org-3-library-pprint-html-functi-cfd107b1
type: concept
title: Functions[¶](https://docs.python.org/3/library/pprint.html#functions "Link
  to this heading")
description: pprint.pp(*object*, *stream=None*, *indent=1*, *width=80*, *depth=None*,
  *\**, *compact=False*, *sort\_dicts=False*, *underscore\_numbers=False*)[¶](https://docs.python.org/3/library/pprint.html#pprin
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pprint.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Functions[¶](https://docs.python.org/3/library/pprint.html#functions "Link to this heading")

pprint.pp(*object*, *stream=None*, *indent=1*, *width=80*, *depth=None*, *\**, *compact=False*, *sort\_dicts=False*, *underscore\_numbers=False*)[¶](https://docs.python.org/3/library/pprint.html#pprint.pp "Link to this definition")
:   Prints the formatted representation of *object*, followed by a newline.
    This function may be used in the interactive interpreter
    instead of the [`print()`](https://docs.python.org/3/library/functions.html#print "print") function for inspecting values.
    Tip: you can reassign `print = pprint.pp` for use within a scope.

    Parameters:
    :   - **object** – The object to be printed.
        - **stream** ([file-like object](https://docs.python.org/3/glossary.html#term-file-like-object) | None) – A file-like object to which the output will be written
          by calling its `write()` method.
          If `None` (the default), [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") is used.
        - **indent** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The amount of indentation added for each nesting level.
        - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "int")) – The desired maximum number of characters per line in the output.
          If a structure cannot be formatted within the width constraint,
          a best effort will be made.
        - **depth** ([*int*](https://docs.python.org/3/library/functions.html#int "int") *|* *None*) – The number of nesting levels which may be printed.
          If the data structure being printed is too deep,
          the next contained level is replaced by `...`.
          If `None` (the default), there is no constraint
          on the depth of the objects being formatted.
        - **compact** ([*bool*](https://docs.python.org/3/library/functions.html#bool "bool")) – Control the way long [sequences](https://docs.python.org/3/glossary.html#term-sequence) are formatted.
          If `False` (the default),
          each item of a sequence will be formatted on a separate line,
          otherwise as many items as will fit within the *width*
          will be formatted on each output line.
        - **sort\_dicts** ([*bool*](https://docs.python.org/3/library/functions.html#bool "bool")) – If `True`, dictionaries will be formatted with
          their keys sorted, otherwise
          they will be displayed in insertion order (the default).
        - **underscore\_numbers** ([*bool*](https://docs.python.org/3/library/functions.html#bool "bool")) – If `True`,
          integers will be formatted with the `_` character for a thousands separator,
          otherwise underscores are not displayed (the default).

    ```
    >>> import pprint
    >>> stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
    >>> stuff.insert(0, stuff)
    >>> pprint.pp(stuff)
    [<Recursion on list with id=...>,
     'spam',
     'eggs',
     'lumberjack',
     'knights',
     'ni']
    ```

    Added in version 3.8.

pprint.pprint(*object*, *stream=None*, *indent=1*, *width=80*, *depth=None*, *\**, *compact=False*, *sort\_dicts=True*, *underscore\_numbers=False*)[¶](https://docs.python.org/3/library/pprint.html#pprint.pprint "Link to this definition")
:   Alias for [`pp()`](https://docs.python.org/3/library/pprint.html#pprint.pp "pprint.pp") with *sort\_dicts* set to `True` by default,
    which would automatically sort the dictionaries’ keys,
    you might want to use `pp()` instead where it is `False` by default.

pprint.pformat(*object*, *indent=1*, *width=80*, *depth=None*, *\**, *compact=False*, *sort\_dicts=True*, *underscore\_numbers=False*)[¶](https://docs.python.org/3/library/pprint.html#pprint.pformat "Link to this definition")
:   Return the formatted representation of *object* as a string. *indent*,
    *width*, *depth*, *compact*, *sort\_dicts* and *underscore\_numbers* are