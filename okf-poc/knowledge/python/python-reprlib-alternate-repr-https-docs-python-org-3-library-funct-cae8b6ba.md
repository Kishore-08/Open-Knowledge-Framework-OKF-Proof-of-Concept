---
id: python-reprlib-alternate-repr-https-docs-python-org-3-library-funct-cae8b6ba
type: concept
title: '`reprlib` — Alternate [`repr()`](https://docs.python.org/3/library/functions.htm'
description: '**Source code:** [Lib/reprlib.py](https://github.com/python/cpython/tree/3.14/Lib/reprlib.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/reprlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `reprlib` — Alternate [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") implementation[¶](https://docs.python.org/3/library/reprlib.html#module-reprlib "Link to this heading")

**Source code:** [Lib/reprlib.py](https://github.com/python/cpython/tree/3.14/Lib/reprlib.py)

---

The `reprlib` module provides a means for producing object representations
with limits on the size of the resulting strings. This is used in the Python
debugger and may be useful in other contexts as well.

This module provides a class, an instance, and a function:

*class* reprlib.Repr(*\**, *maxlevel=6*, *maxtuple=6*, *maxlist=6*, *maxarray=5*, *maxdict=4*, *maxset=6*, *maxfrozenset=6*, *maxdeque=6*, *maxstring=30*, *maxlong=40*, *maxother=30*, *fillvalue='...'*, *indent=None*)[¶](https://docs.python.org/3/library/reprlib.html#reprlib.Repr "Link to this definition")
:   Class which provides formatting services useful in implementing functions
    similar to the built-in [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr"); size limits for different object types
    are added to avoid the generation of representations which are excessively long.

    The keyword arguments of the constructor can be used as a shortcut to set the
    attributes of the `Repr` instance. Which means that the following
    initialization:

    ```
    aRepr = reprlib.Repr(maxlevel=3)
    ```

    Is equivalent to:

    ```
    aRepr = reprlib.Repr()
    aRepr.maxlevel = 3
    ```

    See section [Repr Objects](https://docs.python.org/3/library/reprlib.html#id1) for more information about `Repr`
    attributes.

    Changed in version 3.12: Allow attributes to be set via keyword arguments.

reprlib.aRepr[¶](https://docs.python.org/3/library/reprlib.html#reprlib.aRepr "Link to this definition")
:   This is an instance of [`Repr`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr "reprlib.Repr") which is used to provide the
    [`repr()`](https://docs.python.org/3/library/reprlib.html#reprlib.repr "reprlib.repr") function described below. Changing the attributes of this
    object will affect the size limits used by `repr()` and the Python
    debugger.

reprlib.repr(*obj*)[¶](https://docs.python.org/3/library/reprlib.html#reprlib.repr "Link to this definition")
:   This is the [`repr()`](https://docs.python.org/3/library/reprlib.html#reprlib.Repr.repr "reprlib.Repr.repr") method of `aRepr`. It returns a string
    similar to that returned by the built-in function of the same name, but with
    limits on most sizes.

In addition to size-limiting tools, the module also provides a decorator for
detecting recursive calls to [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__") and substituting a
placeholder string instead.

@reprlib.recursive\_repr(*fillvalue='...'*)[¶](https://docs.python.org/3/library/reprlib.html#reprlib.recursive_repr "Link to this definition")
:   Decorator for [`__repr__()`](https://docs.python.org/3/reference/datamodel.html#object.__repr__ "object.__repr__") methods to detect recursive calls within the
    same thread. If a recursive call is made, the *fillvalue* is returned,
    otherwise, the usual `__repr__()` call is made. For example:

    ```
    >>> from reprlib import recursive_repr
    >>> class MyList(list):
    ...     @recursive_repr()
    ...     def __repr__(self):
    ...         return '<' + '|'.join(map(repr, self)) + '>'
    ...
    >>> m = MyList('abc')
    >>> m.append(m)
    >>> m.append('x')
    >>> print(m)
    <'a'|'b'|'c'|...|'x'>
    ```

    Added in version 3.2.