---
id: python-configparser-configuration-file-parser-https-docs-python-org-caa28eb2
type: concept
title: '`configparser` — Configuration file parser[¶](https://docs.python.org/3/library/'
description: '**Source code:** [Lib/configparser.py](https://github.com/python/cpython/tree/3.14/Lib/configparser.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `configparser` — Configuration file parser[¶](https://docs.python.org/3/library/configparser.html#module-configparser "Link to this heading")

**Source code:** [Lib/configparser.py](https://github.com/python/cpython/tree/3.14/Lib/configparser.py)

---

This module provides the [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser") class which implements a basic
configuration language which provides a structure similar to what’s found in
Microsoft Windows INI files. You can use this to write Python programs which
can be customized by end users easily.

Note

This library does *not* interpret or write the value-type prefixes used in
the Windows Registry extended version of INI syntax.

See also

Module [`tomllib`](https://docs.python.org/3/library/tomllib.html#module-tomllib "tomllib: Parse TOML files.")
:   TOML is a well-specified format for application configuration files.
    It is specifically designed to be an improved version of INI.

Module [`shlex`](https://docs.python.org/3/library/shlex.html#module-shlex "shlex: Simple lexical analysis for Unix shell-like languages.")
:   Support for creating Unix shell-like mini-languages which can also
    be used for application configuration files.

Module [`json`](https://docs.python.org/3/library/json.html#module-json "json: Encode and decode the JSON format.")
:   The `json` module implements a subset of JavaScript syntax which is
    sometimes used for configuration, but does not support comments.