---
id: python-invalid-arguments-https-docs-python-org-3-library-argparse-h-49b35a18
type: concept
title: Invalid arguments[¶](https://docs.python.org/3/library/argparse.html#invalid-arguments
  "Link to this heading")
description: While parsing the command line, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
  "argparse.ArgumentParser.parse_args") checks for a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Invalid arguments[¶](https://docs.python.org/3/library/argparse.html#invalid-arguments "Link to this heading")

While parsing the command line, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") checks for a
variety of errors, including ambiguous options, invalid types, invalid options,
wrong number of positional arguments, etc. When it encounters such an error,
it exits and prints the error along with a usage message:

```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo', type=int)
>>> parser.add_argument('bar', nargs='?')

>>> # invalid type
>>> parser.parse_args(['--foo', 'spam'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: argument --foo: invalid int value: 'spam'

>>> # invalid option
>>> parser.parse_args(['--bar'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: unrecognized arguments: --bar

>>> # wrong number of arguments
>>> parser.parse_args(['spam', 'badger'])
usage: PROG [-h] [--foo FOO] [bar]
PROG: error: unrecognized arguments: badger
```