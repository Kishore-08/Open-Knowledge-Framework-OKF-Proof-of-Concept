---
id: python-ctypes-a-foreign-function-library-for-python-https-docs-pyth-07786b1c
type: concept
title: '`ctypes` — A foreign function library for Python[¶](https://docs.python.org/3/li'
description: '**Source code:** [Lib/ctypes](https://github.com/python/cpython/tree/3.14/Lib/ctypes)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/ctypes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `ctypes` — A foreign function library for Python[¶](https://docs.python.org/3/library/ctypes.html#module-ctypes "Link to this heading")

**Source code:** [Lib/ctypes](https://github.com/python/cpython/tree/3.14/Lib/ctypes)

---

`ctypes` is a foreign function library for Python. It provides C compatible
data types, and allows calling functions in DLLs or shared libraries. It can be
used to wrap these libraries in pure Python.

This is an [optional module](https://docs.python.org/3/glossary.html#term-optional-module).
If it is missing from your copy of CPython,
look for documentation from your distributor (that is,
whoever provided Python to you).
If you are the distributor, see [Requirements for optional modules](https://docs.python.org/3/using/configure.html#optional-module-requirements).

Warning

`ctypes` provides low-level access to native libraries and the
process’s memory, bypassing Python’s safety mechanisms and allowing
execution of arbitrary native code.
Incorrect use can corrupt data and objects, reveal sensitive information,
cause crashes, or otherwise compromise the running process.