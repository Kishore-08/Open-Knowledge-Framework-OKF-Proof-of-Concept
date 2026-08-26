---
id: python-module-interface-https-docs-python-org-3-library-pickle-html-f2bc33b8
type: concept
title: Module Interface[¶](https://docs.python.org/3/library/pickle.html#module-interface
  "Link to this heading")
description: To serialize an object hierarchy, you simply call the [`dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps
  "pickle.dumps") function.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Module Interface[¶](https://docs.python.org/3/library/pickle.html#module-interface "Link to this heading")

To serialize an object hierarchy, you simply call the [`dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps "pickle.dumps") function.
Similarly, to de-serialize a data stream, you call the [`loads()`](https://docs.python.org/3/library/pickle.html#pickle.loads "pickle.loads") function.
However, if you want more control over serialization and de-serialization,
you can create a [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") or an [`Unpickler`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler "pickle.Unpickler") object, respectively.

The `pickle` module provides the following constants:

pickle.HIGHEST\_PROTOCOL[¶](https://docs.python.org/3/library/pickle.html#pickle.HIGHEST_PROTOCOL "Link to this definition")
:   An integer, the highest [protocol version](https://docs.python.org/3/library/pickle.html#pickle-protocols)
    available. This value can be passed as a *protocol* value to functions
    [`dump()`](https://docs.python.org/3/library/pickle.html#pickle.dump "pickle.dump") and [`dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps "pickle.dumps") as well as the [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler")
    constructor.

pickle.DEFAULT\_PROTOCOL[¶](https://docs.python.org/3/library/pickle.html#pickle.DEFAULT_PROTOCOL "Link to this definition")
:   An integer, the default [protocol version](https://docs.python.org/3/library/pickle.html#pickle-protocols) used
    for pickling. May be less than [`HIGHEST_PROTOCOL`](https://docs.python.org/3/library/pickle.html#pickle.HIGHEST_PROTOCOL "pickle.HIGHEST_PROTOCOL"). Currently the
    default protocol is 5, introduced in Python 3.8 and incompatible
    with previous versions. This version introduces support for out-of-band
    buffers, where [**PEP 3118**](https://peps.python.org/pep-3118/)-compatible data can be transmitted separately
    from the main pickle stream.

    Changed in version 3.0: The default protocol is 3.

    Changed in version 3.8: The default protocol is 4.

    Changed in version 3.14: The default protocol is 5.

The `pickle` module provides the following functions to make the pickling
process more convenient:

pickle.dump(*obj*, *file*, *protocol=None*, *\**, *fix\_imports=True*, *buffer\_callback=None*)[¶](https://docs.python.org/3/library/pickle.html#pickle.dump "Link to this definition")
:   Write the pickled representation of the object *obj* to the open
    [file object](https://docs.python.org/3/glossary.html#term-file-object) *file*. This is equivalent to
    `Pickler(file, protocol).dump(obj)`.

    Arguments *file*, *protocol*, *fix\_imports* and *buffer\_callback* have
    the same meaning as in the [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") constructor.

    Changed in version 3.8: The *buffer\_callback* argument was added.

pickle.dumps(*obj*, *protocol=None*, *\**, *fix\_imports=True*, *buffer\_callback=None*)[¶](https://docs.python.org/3/library/pickle.html#pickle.dumps "Link to this definition")
:   Return the pickled representation of the object *obj* as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object,
    instead of writing it to a file.

    Arguments *protocol*, *fix\_imports* and *buffer\_callback* have the same
    meaning as in the [`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") constructor.

    Changed in version 3.8: The *buffer\_callback* argument was added.

pickle.load(*file*, *\**, *fix\_imports=True*, *encoding='ASCII'*, *errors='strict'*, *buffers=None*)[¶](https://docs.python.org/3/library/pickle.html#pickle.load "Link to this definition")
:   Read the pickled representation of an object from the open [file object](https://docs.python.org/3/glossary.html#term-f