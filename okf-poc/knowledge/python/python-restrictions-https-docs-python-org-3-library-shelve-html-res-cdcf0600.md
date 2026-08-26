---
id: python-restrictions-https-docs-python-org-3-library-shelve-html-res-cdcf0600
type: concept
title: Restrictions[¶](https://docs.python.org/3/library/shelve.html#restrictions
  "Link to this heading")
description: '- The choice of which database package will be used (such as [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm
  "dbm.ndbm: The New Database Manager") or'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shelve.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Restrictions[¶](https://docs.python.org/3/library/shelve.html#restrictions "Link to this heading")

- The choice of which database package will be used (such as [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") or
  [`dbm.gnu`](https://docs.python.org/3/library/dbm.html#module-dbm.gnu "dbm.gnu: GNU database manager")) depends on which interface is available. Therefore it is not
  safe to open the database directly using [`dbm`](https://docs.python.org/3/library/dbm.html#module-dbm "dbm: Interfaces to various Unix \"database\" formats."). The database is also
  (unfortunately) subject to the limitations of `dbm`, if it is used —
  this means that (the pickled representation of) the objects stored in the
  database should be fairly small, and in rare cases key collisions may cause
  the database to refuse updates.
- The `shelve` module does not support *concurrent* read/write access to
  shelved objects. (Multiple simultaneous read accesses are safe.) When a
  program has a shelf open for writing, no other program should have it open for
  reading or writing. Unix file locking can be used to solve this, but this
  differs across Unix versions and requires knowledge about the database
  implementation used.
- On macOS [`dbm.ndbm`](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm "dbm.ndbm: The New Database Manager") can silently corrupt the database file on updates,
  which can cause hard crashes when trying to read from the database.

*class* shelve.Shelf(*dict*, *protocol=None*, *writeback=False*, *keyencoding='utf-8'*)[¶](https://docs.python.org/3/library/shelve.html#shelve.Shelf "Link to this definition")
:   A subclass of [`collections.abc.MutableMapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.MutableMapping "collections.abc.MutableMapping") which stores pickled
    values in the *dict* object.

    By default, pickles created with [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") are used
    to serialize values. The version of the pickle protocol can be specified
    with the *protocol* parameter. See the [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") documentation for a
    discussion of the pickle protocols.

    If the *writeback* parameter is `True`, the object will hold a cache of all
    entries accessed and write them back to the *dict* at sync and close times.
    This allows natural operations on mutable entries, but can consume much more
    memory and make sync and close take a long time.

    The *keyencoding* parameter is the encoding used to encode keys before they
    are used with the underlying dict.

    A `Shelf` object can also be used as a context manager, in which
    case it will be automatically closed when the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) block ends.

    Changed in version 3.2: Added the *keyencoding* parameter; previously, keys were always encoded in
    UTF-8.

    Changed in version 3.4: Added context manager support.

    Changed in version 3.10: [`pickle.DEFAULT_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "pickle.DEFAULT_PROTOCOL") is now used as the default pickle
    protocol.

*class* shelve.BsdDbShelf(*dict*, *protocol=None*, *writeback=False*, *keyencoding='utf-8'*)[¶](https://docs.python.org/3/library/shelve.html#shelve.BsdDbShelf "Link to this definition")
:   A subclass of [`Shelf`](https://docs.python.org/3/library/shelve.html#shelve.Shelf "shelve.Shelf") which exposes `first()`, `next()`,
    `previous()`, `last()` and `set_location()` methods.
    These are available
    in the third-party `bsddb` module from [pybsddb](https://www.jcea.es/programacion/pybsddb.htm) but not in other database
    modules. The *dict* object passed to the constr