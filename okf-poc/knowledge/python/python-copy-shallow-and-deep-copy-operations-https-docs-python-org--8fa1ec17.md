---
id: python-copy-shallow-and-deep-copy-operations-https-docs-python-org--8fa1ec17
type: concept
title: '`copy` — Shallow and deep copy operations[¶](https://docs.python.org/3/library/c'
description: '**Source code:** [Lib/copy.py](https://github.com/python/cpython/tree/3.14/Lib/copy.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/copy.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `copy` — Shallow and deep copy operations[¶](https://docs.python.org/3/library/copy.html#module-copy "Link to this heading")

**Source code:** [Lib/copy.py](https://github.com/python/cpython/tree/3.14/Lib/copy.py)

---

Assignment statements in Python do not copy objects, they create bindings
between a target and an object. For collections that are mutable or contain
mutable items, a copy is sometimes needed so one can change one copy without
changing the other. This module provides generic shallow and deep copy
operations (explained below).

Interface summary:

copy.copy(*obj*)[¶](https://docs.python.org/3/library/copy.html#copy.copy "Link to this definition")
:   Return a shallow copy of *obj*.

copy.deepcopy(*obj*[, *memo*])[¶](https://docs.python.org/3/library/copy.html#copy.deepcopy "Link to this definition")
:   Return a deep copy of *obj*.

copy.replace(*obj*, */*, *\*\*changes*)[¶](https://docs.python.org/3/library/copy.html#copy.replace "Link to this definition")
:   Creates a new object of the same type as *obj*, replacing fields with values
    from *changes*.

    Added in version 3.13.

*exception* copy.Error[¶](https://docs.python.org/3/library/copy.html#copy.Error "Link to this definition")
:   Raised for module specific errors.

The difference between shallow and deep copying is only relevant for compound
objects (objects that contain other objects, like lists or class instances):

- A *shallow copy* constructs a new compound object and then (to the extent
  possible) inserts *references* into it to the objects found in the original.
- A *deep copy* constructs a new compound object and then, recursively, inserts
  *copies* into it of the objects found in the original.

Two problems often exist with deep copy operations that don’t exist with shallow
copy operations:

- Recursive objects (compound objects that, directly or indirectly, contain a
  reference to themselves) may cause a recursive loop.
- Because deep copy copies everything it may copy too much, such as data
  which is intended to be shared between copies.

The [`deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "copy.deepcopy") function avoids these problems by:

- keeping a `memo` dictionary of objects already copied during the current
  copying pass; and
- letting user-defined classes override the copying operation or the set of
  components copied.

This module does not copy types like module, method, stack trace, stack frame,
file, socket, window, or any similar types. It does “copy” functions and
classes (shallow and deeply), by returning the original object unchanged; this
is compatible with the way these are treated by the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module.

Shallow copies of many collections can be made using the corresponding
`copy()` method (such as [`list.copy()`](https://docs.python.org/3/library/stdtypes.html#list.copy "list.copy"), [`dict.copy()`](https://docs.python.org/3/library/stdtypes.html#dict.copy "dict.copy") or
[`set.copy()`](https://docs.python.org/3/library/stdtypes.html#set.copy "set.copy")), and of sequences (such as lists or bytearrays) by making
a slice of the entire sequence (`sequence[:]`).
However, these methods and slicing can create an instance of the base type
when copying an instance of a subclass, whereas [`copy.copy()`](https://docs.python.org/3/library/copy.html#copy.copy "copy.copy") normally
returns an instance of the same type.

Classes can use the same interfaces to control copying that they use to control
pickling. See the description of module [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") for information on these
methods. In fact, the `copy` module uses the registered
pickle functions from the [`copyreg`](https://docs.python.org/3/library/copyreg.html#module-copyreg "copyreg: Register pickl