---
id: python-the-parse-args-method-https-docs-python-org-3-library-argpar-49b35a18
type: concept
title: The parse\_args() method[¶](https://docs.python.org/3/library/argparse.html#the-parse-args-method
  "Link to this heading")
description: ArgumentParser.parse\_args(*args=None*, *namespace=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## The parse\_args() method[¶](https://docs.python.org/3/library/argparse.html#the-parse-args-method "Link to this heading")

ArgumentParser.parse\_args(*args=None*, *namespace=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "Link to this definition")
:   Convert argument strings to objects and assign them as attributes of the
    namespace. Return the populated namespace.

    Previous calls to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") determine exactly what objects are
    created and how they are assigned. See the documentation for
    `add_argument()` for details.

    - [args](https://docs.python.org/3/library/argparse.html#args) - List of strings to parse. The default is taken from
      [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv").
    - [namespace](https://docs.python.org/3/library/argparse.html#namespace) - An object to take the attributes. The default is a new empty
      [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") object.