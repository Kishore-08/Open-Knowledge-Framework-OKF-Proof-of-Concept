---
id: python-metavar-https-docs-python-org-3-library-argparse-html-metava-49b35a18
type: concept
title: metavar[¶](https://docs.python.org/3/library/argparse.html#metavar "Link to
  this heading")
description: When [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") generates help messages, it needs some way to refer
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### metavar[¶](https://docs.python.org/3/library/argparse.html#metavar "Link to this heading")

When [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") generates help messages, it needs some way to refer
to each expected argument. By default, `ArgumentParser` objects use the [dest](https://docs.python.org/3/library/argparse.html#dest)
value as the “name” of each object. By default, for positional argument
actions, the [dest](https://docs.python.org/3/library/argparse.html#dest) value is used directly, and for optional argument actions,
the [dest](https://docs.python.org/3/library/argparse.html#dest) value is uppercased. So, a single positional argument with
`dest='bar'` will be referred to as `bar`. A single
optional argument `--foo` that should be followed by a single command-line argument
will be referred to as `FOO`. An example:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo FOO] bar

positional arguments:
 bar

options:
 -h, --help  show this help message and exit
 --foo FOO
```

An alternative name can be specified with `metavar`:

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', metavar='YYY')
>>> parser.add_argument('bar', metavar='XXX')
>>> parser.parse_args('X --foo Y'.split())
Namespace(bar='X', foo='Y')
>>> parser.print_help()
usage:  [-h] [--foo YYY] XXX

positional arguments:
 XXX

options:
 -h, --help  show this help message and exit
 --foo YYY
```

Note that `metavar` only changes the *displayed* name - the name of the
attribute on the [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") object is still determined
by the [dest](https://docs.python.org/3/library/argparse.html#dest) value.

Different values of `nargs` may cause the metavar to be used multiple times.
Providing a tuple to `metavar` specifies a different display for each of the
arguments:

```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-x', nargs=2)
>>> parser.add_argument('--foo', nargs=2, metavar=('bar', 'baz'))
>>> parser.print_help()
usage: PROG [-h] [-x X X] [--foo bar baz]

options:
 -h, --help     show this help message and exit
 -x X X
 --foo bar baz
```