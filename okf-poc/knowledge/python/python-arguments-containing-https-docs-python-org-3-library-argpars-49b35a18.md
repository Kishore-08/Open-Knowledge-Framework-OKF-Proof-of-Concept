---
id: python-arguments-containing-https-docs-python-org-3-library-argpars-49b35a18
type: concept
title: Arguments containing `-`[¶](https://docs.python.org/3/library/argparse.html#arguments-containing
  "Link to this heading")
description: The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
  "argparse.ArgumentParser.parse_args") method attempts to give errors whenever
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Arguments containing `-`[¶](https://docs.python.org/3/library/argparse.html#arguments-containing "Link to this heading")

The [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method attempts to give errors whenever
the user has clearly made a mistake, but some situations are inherently
ambiguous. For example, the command-line argument `-1` could either be an
attempt to specify an option or an attempt to provide a positional argument.
The `parse_args()` method is cautious here: positional
arguments may only begin with `-` if they look like negative numbers and
there are no options in the parser that look like negative numbers:

```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x')
>>> parser.add_argument('foo', nargs='?')

>>> # no negative number options, so -1 is a positional argument
>>> parser.parse_args(['-x', '-1'])
Namespace(foo=None, x='-1')

>>> # no negative number options, so -1 and -5 are positional arguments
>>> parser.parse_args(['-x', '-1', '-5'])
Namespace(foo='-5', x='-1')

>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-1', dest='one')
>>> parser.add_argument('foo', nargs='?')

>>> # negative number options present, so -1 is an option
>>> parser.parse_args(['-1', 'X'])
Namespace(foo=None, one='X')

>>> # negative number options present, so -2 is an option
>>> parser.parse_args(['-2'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: unrecognized arguments: -2

>>> # negative number options present, so both -1s are options
>>> parser.parse_args(['-1', '-1'])
usage: PROG [-h] [-1 ONE] [foo]
PROG: error: argument -1: expected one argument
```

If you have positional arguments that must begin with `-` and don’t look
like negative numbers, you can insert the pseudo-argument `'--'` which tells
[`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") that everything after that is a positional
argument:

```
>>> parser.parse_args(['--', '-f'])
Namespace(foo='-f', one=None)
```

See also [the argparse howto on ambiguous arguments](https://docs.python.org/3/howto/argparse.html#specifying-ambiguous-arguments)
for more details.

Changed in version 3.14: Negative-number matching was expanded to include numbers in scientific
notation (`-2.5e-6`), numbers containing underscores (`-1_234.5`),
and complex numbers (`-1.2e-3j`).