---
id: python-marshal-internal-python-object-serialization-https-docs-pyth-2f9bf5fb
type: concept
title: '`marshal` — Internal Python object serialization[¶](https://docs.python.org/3/li'
description: '---'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/marshal.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `marshal` — Internal Python object serialization[¶](https://docs.python.org/3/library/marshal.html#module-marshal "Link to this heading")

---

This module contains functions that can read and write Python values in a binary
format. The format is specific to Python, but independent of machine
architecture issues (e.g., you can write a Python value to a file on a PC,
transport the file to a Mac, and read it back there). Details of the format are
undocumented on purpose; it may change between Python versions (although it
rarely does). [[1]](https://docs.python.org/3/library/marshal.html#id2)

This is not a general “persistence” module. For general persistence and
transfer of Python objects through RPC calls, see the modules [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") and
[`shelve`](https://docs.python.org/3/library/shelve.html#module-shelve "shelve: Python object persistence."). The `marshal` module exists mainly to support reading and
writing the “pseudo-compiled” code for Python modules of `.pyc` files.
Therefore, the Python maintainers reserve the right to modify the marshal format
in backward incompatible ways should the need arise.
The format of code objects is not compatible between Python versions,
even if the version of the format is the same.
De-serializing a code object in the incorrect Python version has undefined behavior.
If you’re serializing and
de-serializing Python objects, use the `pickle` module instead – the
performance is comparable, version independence is guaranteed, and pickle
supports a substantially wider range of objects than marshal.

Warning

The `marshal` module is not intended to be secure against erroneous or
maliciously constructed data. Never unmarshal data received from an
untrusted or unauthenticated source.

There are functions that read/write files as well as functions operating on
bytes-like objects.

Not all Python object types are supported; in general, only objects whose value
is independent from a particular invocation of Python can be written and read by
this module. The following types are supported:

- Numeric types: [`int`](https://docs.python.org/3/library/functions.html#int "int"), [`bool`](https://docs.python.org/3/library/functions.html#bool "bool"), [`float`](https://docs.python.org/3/library/functions.html#float "float"), [`complex`](https://docs.python.org/3/library/functions.html#complex "complex").
- Strings ([`str`](https://docs.python.org/3/library/stdtypes.html#str "str")) and [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes").
  [Bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) like [`bytearray`](https://docs.python.org/3/library/stdtypes.html#bytearray "bytearray") are
  marshalled as `bytes`.
- Containers: [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple"), [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), [`set`](https://docs.python.org/3/library/stdtypes.html#set "set"), [`frozenset`](https://docs.python.org/3/library/stdtypes.html#frozenset "frozenset"),
  and (since [`version`](https://docs.python.org/3/library/marshal.html#marshal.version "marshal.version") 5), [`slice`](https://docs.python.org/3/library/functions.html#slice "slice").
  It should be understood that these are supported only if the values contained
  therein are themselves supported.
  Recursive containers are supported since `version` 3.
- The singletons [`None`](https://docs.python.org/3/library/constants.html#None "None"), [`Ellipsis`](https://docs.python.org/3/library/constants.html#Ellipsis "Ellipsis") and [`StopIteration`](https://docs.python.org/3/library/exceptions.html#StopIteration "StopIteration").
- [`code`](https://docs.python.org/3/library/code.html#module-code "code: Facilities to implement read-eval-print loops.") objects, if *allow\_code* is true. See note above about
  version dependence.

C