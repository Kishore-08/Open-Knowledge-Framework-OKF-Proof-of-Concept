---
id: python-shelve-python-object-persistence-https-docs-python-org-3-lib-cdcf0600
type: concept
title: '`shelve` — Python object persistence[¶](https://docs.python.org/3/library/shelve'
description: '**Source code:** [Lib/shelve.py](https://github.com/python/cpython/tree/3.14/Lib/shelve.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shelve.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `shelve` — Python object persistence[¶](https://docs.python.org/3/library/shelve.html#module-shelve "Link to this heading")

**Source code:** [Lib/shelve.py](https://github.com/python/cpython/tree/3.14/Lib/shelve.py)

---

A “shelf” is a persistent, dictionary-like object. The difference with “dbm”
databases is that the values (not the keys!) in a shelf can be essentially
arbitrary Python objects — anything that the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") module can handle.
This includes most class instances, recursive data types, and objects containing
lots of shared sub-objects. The keys are ordinary strings.

shelve.open(*filename*, *flag='c'*, *protocol=None*, *writeback=False*)[¶](https://docs.python.org/3/library/shelve.html#shelve.open "Link to this definition")
:   Open a persistent dictionary. The filename specified is the base filename for
    the underlying database. As a side-effect, an extension may be added to the
    filename and more than one file may be created. By default, the underlying
    database file is opened for reading and writing. The optional *flag* parameter
    has the same interpretation as the *flag* parameter of [`dbm.open()`](https://docs.python.org/3/library/dbm.html#dbm.open "dbm.open").

    By default, pickles created with [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") are used
    to serialize values. The version of the pickle protocol can be specified
    with the *protocol* parameter.

    Because of Python semantics, a shelf cannot know when a mutable
    persistent-dictionary entry is modified. By default modified objects are
    written *only* when assigned to the shelf (see [Example](https://docs.python.org/3/library/shelve.html#shelve-example)). If the
    optional *writeback* parameter is set to `True`, all entries accessed are also
    cached in memory, and written back on [`sync()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync "shelve.Shelf.sync") and
    [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "shelve.Shelf.close"); this can make it handier to mutate mutable entries in
    the persistent dictionary, but, if many entries are accessed, it can consume
    vast amounts of memory for the cache, and it can make the close operation
    very slow since all accessed entries are written back (there is no way to
    determine which accessed entries are mutable, nor which ones were actually
    mutated).

    Changed in version 3.10: [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") is now used as the default pickle
    protocol.

    Changed in version 3.11: Accepts [path-like object](https://docs.python.org/3/glossary.html#term-path-like-object) for filename.

    Note

    Do not rely on the shelf being closed automatically; always call
    [`close()`](https://docs.python.org/3/library/shelve.html#shelve.Shelf.close "shelve.Shelf.close") explicitly when you don’t need it any more, or
    use `shelve.open()` as a context manager:

    ```
    with shelve.open('spam') as db:
        db['eggs'] = 'eggs'
    ```

Warning

Because the `shelve` module is backed by [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back."), it is insecure
to load a shelf from an untrusted source. Like with pickle, loading a shelf
can execute arbitrary code.

Shelf objects support most of the methods and operations supported by dictionaries
(except copying, constructors and operators `|` and `|=`). This eases the
transition from dictionary based scripts to those requiring persistent storage.

Two additional methods are supported:

Shelf.sync()[¶](https://docs.python.org/3/library/shelve.html#shelve.Shelf.sync "Link to this definition")