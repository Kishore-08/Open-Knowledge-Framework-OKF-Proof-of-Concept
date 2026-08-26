---
id: python-tomllib-parse-toml-files-https-docs-python-org-3-library-tom-00f2bfaf
type: concept
title: '`tomllib` — Parse TOML files[¶](https://docs.python.org/3/library/tomllib.html#m'
description: Added in version 3.11.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tomllib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `tomllib` — Parse TOML files[¶](https://docs.python.org/3/library/tomllib.html#module-tomllib "Link to this heading")

Added in version 3.11.

**Source code:** [Lib/tomllib](https://github.com/python/cpython/tree/3.14/Lib/tomllib)

---

This module provides an interface for parsing TOML 1.0.0 (Tom’s Obvious Minimal
Language, [https://toml.io](https://toml.io/en/)). This module does not
support writing TOML.

Warning

Be cautious when parsing data from untrusted sources.
A malicious TOML string may cause the decoder to consume considerable
CPU and memory resources.
Limiting the size of data to be parsed is recommended.

See also

The [Tomli-W package](https://pypi.org/project/tomli-w/)
is a TOML writer that can be used in conjunction with this module,
providing a write API familiar to users of the standard library
[`marshal`](https://docs.python.org/3/library/marshal.html#module-marshal "marshal: Convert Python objects to streams of bytes and back (with different constraints).") and [`pickle`](https://docs.python.org/3/library/pickle.html#module-pickle "pickle: Convert Python objects to streams of bytes and back.") modules.

See also

The [TOML Kit package](https://pypi.org/project/tomlkit/)
is a style-preserving TOML library with both read and write capability.
It is a recommended replacement for this module for editing already
existing TOML files.

This module defines the following functions:

tomllib.load(*fp*, */*, *\**, *parse\_float=float*)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.load "Link to this definition")
:   Read a TOML file. The first argument should be a readable and binary file object.
    Return a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"). Convert TOML types to Python using this
    [conversion table](https://docs.python.org/3/library/tomllib.html#toml-to-py-table).

    *parse\_float* will be called with the string of every TOML
    float to be decoded. By default, this is equivalent to `float(num_str)`.
    This can be used to use another datatype or parser for TOML floats
    (e.g. [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal")). The callable must not return a
    [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict") or a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list"), else a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is raised.

    A [`TOMLDecodeError`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "tomllib.TOMLDecodeError") will be raised on an invalid TOML document.

tomllib.loads(*s*, */*, *\**, *parse\_float=float*)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.loads "Link to this definition")
:   Load TOML from a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") object. Return a [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"). Convert TOML
    types to Python using this [conversion table](https://docs.python.org/3/library/tomllib.html#toml-to-py-table). The
    *parse\_float* argument has the same meaning as in [`load()`](https://docs.python.org/3/library/tomllib.html#tomllib.load "tomllib.load").

    A [`TOMLDecodeError`](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "tomllib.TOMLDecodeError") will be raised on an invalid TOML document.

The following exceptions are available:

*exception* tomllib.TOMLDecodeError(*msg*, *doc*, *pos*)[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError "Link to this definition")
:   Subclass of [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") with the following additional attributes:

    msg[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.msg "Link to this definition")
    :   The unformatted error message.

    doc[¶](https://docs.python.org/3/library/tomllib.html#tomllib.TOMLDecodeError.doc "