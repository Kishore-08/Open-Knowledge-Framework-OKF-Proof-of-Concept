---
id: python-data-persistence-https-docs-python-org-3-library-persistence-d0458e23
type: concept
title: Data Persistence[¶](https://docs.python.org/3/library/persistence.html#data-pers
description: The modules described in this chapter support storing Python data in
  a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/persistence.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# Data Persistence[¶](https://docs.python.org/3/library/persistence.html#data-persistence "Link to this heading")

The modules described in this chapter support storing Python data in a
persistent form on disk. The [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and [`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") modules can turn
many Python data types into a stream of bytes and then recreate the objects from
the bytes. The various DBM-related modules support a family of hash-based file
formats that store a mapping of strings to other strings.

The list of modules described in this chapter is:

- [`pickle` — Python object serialization](https://docs.python.org/3/library/pickle.html)
  - [Relationship to other Python modules](https://docs.python.org/3/library/pickle.html#relationship-to-other-python-modules)
    - [Comparison with `marshal`](https://docs.python.org/3/library/pickle.html#comparison-with-marshal)
    - [Comparison with `json`](https://docs.python.org/3/library/pickle.html#comparison-with-json)
  - [Data stream format](https://docs.python.org/3/library/pickle.html#data-stream-format)
  - [Module Interface](https://docs.python.org/3/library/pickle.html#module-interface)
  - [What can be pickled and unpickled?](https://docs.python.org/3/library/pickle.html#what-can-be-pickled-and-unpickled)
  - [Pickling Class Instances](https://docs.python.org/3/library/pickle.html#pickling-class-instances)
    - [Persistence of External Objects](https://docs.python.org/3/library/pickle.html#persistence-of-external-objects)
    - [Dispatch Tables](https://docs.python.org/3/library/pickle.html#dispatch-tables)
    - [Handling Stateful Objects](https://docs.python.org/3/library/pickle.html#handling-stateful-objects)
  - [Custom Reduction for Types, Functions, and Other Objects](https://docs.python.org/3/library/pickle.html#custom-reduction-for-types-functions-and-other-objects)
  - [Out-of-band Buffers](https://docs.python.org/3/library/pickle.html#out-of-band-buffers)
    - [Provider API](https://docs.python.org/3/library/pickle.html#provider-api)
    - [Consumer API](https://docs.python.org/3/library/pickle.html#consumer-api)
    - [Example](https://docs.python.org/3/library/pickle.html#example)
  - [Restricting Globals](https://docs.python.org/3/library/pickle.html#restricting-globals)
  - [Performance](https://docs.python.org/3/library/pickle.html#performance)
  - [Examples](https://docs.python.org/3/library/pickle.html#examples)
  - [Command-line interface](https://docs.python.org/3/library/pickle.html#command-line-interface)
- [`copyreg` — Register `pickle` support functions](https://docs.python.org/3/library/copyreg.html)
  - [Example](https://docs.python.org/3/library/copyreg.html#example)
- [`shelve` — Python object persistence](https://docs.python.org/3/library/shelve.html)
  - [Restrictions](https://docs.python.org/3/library/shelve.html#restrictions)
  - [Example](https://docs.python.org/3/library/shelve.html#example)
- [`marshal` — Internal Python object serialization](https://docs.python.org/3/library/marshal.html)
- [`dbm` — Interfaces to Unix “databases”](https://docs.python.org/3/library/dbm.html)
  - [`dbm.sqlite3` — SQLite backend for dbm](https://docs.python.org/3/library/dbm.html#module-dbm.sqlite3)
  - [`dbm.gnu` — GNU database manager](https://docs.python.org/3/library/dbm.html#module-dbm.gnu)
  - [`dbm.ndbm` — New Database Manager](https://docs.python.org/3/library/dbm.html#module-dbm.ndbm)
  - [`dbm.dumb` — Portable DBM implementation](https://docs.python.org/3/library/dbm.html#module-dbm.dumb)
- [`sqlite3` — DB-API 2.0 interface for SQLite databases](https://docs.python.org/3/library/sqlite3.html)
  - [Tutorial](https://docs.python.org/3/library/sqlite3.html#tutorial)
  - [Reference](https://docs.python.or