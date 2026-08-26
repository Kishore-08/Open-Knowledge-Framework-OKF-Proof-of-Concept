---
id: python-copyreg-register-pickle-support-functions-https-docs-python--cdabdf24
type: concept
title: '`copyreg` — Register `pickle` support functions[¶](https://docs.python.org/3/lib'
description: '**Source code:** [Lib/copyreg.py](https://github.com/python/cpython/tree/3.14/Lib/copyreg.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/copyreg.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `copyreg` — Register `pickle` support functions[¶](https://docs.python.org/3/library/copyreg.html#module-copyreg "Link to this heading")

**Source code:** [Lib/copyreg.py](https://github.com/python/cpython/tree/3.14/Lib/copyreg.py)

---

The `copyreg` module offers a way to define functions used while pickling
specific objects. The [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and [`copy`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.") modules use those functions
when pickling/copying those objects. The module provides configuration
information about object constructors which are not classes.
Such constructors may be factory functions or class instances.

copyreg.constructor(*object*)[¶](https://docs.python.org/3/library/copyreg.html#copyreg.constructor "Link to this definition")
:   Declares *object* to be a valid constructor. If *object* is not callable (and
    hence not valid as a constructor), raises [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError").

copyreg.pickle(*type*, *function*, *constructor\_ob=None*)[¶](https://docs.python.org/3/library/copyreg.html#copyreg.pickle "Link to this definition")
:   Declares that *function* should be used as a “reduction” function for objects
    of type *type*. *function* must return either a string or a tuple
    containing between two and six elements. See the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table")
    for more details on the interface of *function*.

    The *constructor\_ob* parameter is a legacy feature and is now ignored, but if
    passed it must be a callable.

    Note that the [`dispatch_table`](https://docs.python.org/3/library/pickle.html#pickle.Pickler.dispatch_table "pickle.Pickler.dispatch_table") attribute of a pickler
    object or subclass of [`pickle.Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") can also be used for
    declaring reduction functions.