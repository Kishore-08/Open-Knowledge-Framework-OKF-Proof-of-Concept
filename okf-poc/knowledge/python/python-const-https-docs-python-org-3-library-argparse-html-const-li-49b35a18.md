---
id: python-const-https-docs-python-org-3-library-argparse-html-const-li-49b35a18
type: concept
title: const[¶](https://docs.python.org/3/library/argparse.html#const "Link to this
  heading")
description: The `const` argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
  "argparse.ArgumentParser.add_argument") is used to hold
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### const[¶](https://docs.python.org/3/library/argparse.html#const "Link to this heading")

The `const` argument of [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") is used to hold
constant values that are not read from the command line but are required for
the various [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") actions. The two most common uses of it are:

- When [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") is called with
  `action='store_const'` or `action='append_const'`. These actions add the
  `const` value to one of the attributes of the object returned by
  [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). See the [action](https://docs.python.org/3/library/argparse.html#action) description for examples.
  If `const` is not provided to `add_argument()`, it will
  receive a default value of `None`.
- When [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") is called with option strings
  (like `-f` or `--foo`) and `nargs='?'`. This creates an optional
  argument that can be followed by zero or one command-line arguments.
  When parsing the command line, if the option string is encountered with no
  command-line argument following it, the value from `const` will be used.
  See the [nargs](https://docs.python.org/3/library/argparse.html#nargs) description for examples.

Changed in version 3.11: `const=None` by default, including when `action='append_const'` or
`action='store_const'`.