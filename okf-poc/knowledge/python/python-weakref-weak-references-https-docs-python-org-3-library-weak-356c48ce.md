---
id: python-weakref-weak-references-https-docs-python-org-3-library-weak-356c48ce
type: concept
title: '`weakref` — Weak references[¶](https://docs.python.org/3/library/weakref.html#mo'
description: '**Source code:** [Lib/weakref.py](https://github.com/python/cpython/tree/3.14/Lib/weakref.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/weakref.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

# `weakref` — Weak references[¶](https://docs.python.org/3/library/weakref.html#module-weakref "Link to this heading")

**Source code:** [Lib/weakref.py](https://github.com/python/cpython/tree/3.14/Lib/weakref.py)

---

The `weakref` module allows the Python programmer to create *weak
references* to objects.

In the following, the term *referent* means the object which is referred to
by a weak reference.

A weak reference to an object is not enough to keep the object alive: when the
only remaining references to a referent are weak references,
[garbage collection](https://docs.python.org/3/glossary.html#term-garbage-collection) is free to destroy the referent and reuse its memory
for something else. However, until the object is actually destroyed the weak
reference may return the object even if there are no strong references to it.

A primary use for weak references is to implement caches or
mappings holding large objects, where it’s desired that a large object not be
kept alive solely because it appears in a cache or mapping.

For example, if you have a number of large binary image objects, you may wish to
associate a name with each. If you used a Python dictionary to map names to
images, or images to names, the image objects would remain alive just because
they appeared as values or keys in the dictionaries. The
[`WeakKeyDictionary`](https://docs.python.org/3/library/weakref.html#weakref.WeakKeyDictionary "weakref.WeakKeyDictionary") and [`WeakValueDictionary`](https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary "weakref.WeakValueDictionary") classes supplied by
the `weakref` module are an alternative, using weak references to construct
mappings that don’t keep objects alive solely because they appear in the mapping
objects. If, for example, an image object is a value in a
`WeakValueDictionary`, then when the last remaining references to that
image object are the weak references held by weak mappings, garbage collection
can reclaim the object, and its corresponding entries in weak mappings are
simply deleted.

[`WeakKeyDictionary`](https://docs.python.org/3/library/weakref.html#weakref.WeakKeyDictionary "weakref.WeakKeyDictionary") and [`WeakValueDictionary`](https://docs.python.org/3/library/weakref.html#weakref.WeakValueDictionary "weakref.WeakValueDictionary") use weak references
in their implementation, setting up callback functions on the weak references
that notify the weak dictionaries when a key or value has been reclaimed by
garbage collection. [`WeakSet`](https://docs.python.org/3/library/weakref.html#weakref.WeakSet "weakref.WeakSet") implements the [`set`](https://docs.python.org/3/library/stdtypes.html#set "set") interface,
but keeps weak references to its elements, just like a
`WeakKeyDictionary` does.

[`finalize`](https://docs.python.org/3/library/weakref.html#weakref.finalize "weakref.finalize") provides a straight forward way to register a
cleanup function to be called when an object is garbage collected.
This is simpler to use than setting up a callback function on a raw
weak reference, since the module automatically ensures that the finalizer
remains alive until the object is collected.

Most programs should find that using one of these weak container types
or [`finalize`](https://docs.python.org/3/library/weakref.html#weakref.finalize "weakref.finalize") is all they need – it’s not usually necessary to
create your own weak references directly. The low-level machinery is
exposed by the `weakref` module for the benefit of advanced uses.

Not all objects can be weakly referenced. Objects which support weak references
include class instances, functions written in Python (but not in C), instance methods,
sets, frozensets, some [file objects](https://docs.python.org/3/glossary.html#term-file-object), [generators](https://docs.python.org/3/glossary.html#term-generator),
type objects, sockets, arrays, deques, regular expression pattern objects, and code
objects.

Changed in version 3.2: Add