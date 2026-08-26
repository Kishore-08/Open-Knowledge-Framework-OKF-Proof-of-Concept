---
id: python-name-or-flags-https-docs-python-org-3-library-argparse-html--49b35a18
type: concept
title: name or flags[¶](https://docs.python.org/3/library/argparse.html#name-or-flags
  "Link to this heading")
description: The [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
  "argparse.ArgumentParser.add_argument") method must know whether an optional
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### name or flags[¶](https://docs.python.org/3/library/argparse.html#name-or-flags "Link to this heading")

The [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") method must know whether an optional
argument, like `-f` or `--foo`, or a positional argument, like a list of
filenames, is expected. The first arguments passed to
`add_argument()` must therefore be either a series of
flags, or a simple argument name.

For example, an optional argument could be created like:

```
>>> parser.add_argument('-f', '--foo')
```

while a positional argument could be created like:

```
>>> parser.add_argument('bar')
```

When [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") is called, optional arguments will be
identified by the `-` prefix, and the remaining arguments will be assumed to
be positional:

```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('-f', '--foo')
>>> parser.add_argument('bar')
>>> parser.parse_args(['BAR'])
Namespace(bar='BAR', foo=None)
>>> parser.parse_args(['BAR', '--foo', 'FOO'])
Namespace(bar='BAR', foo='FOO')
>>> parser.parse_args(['--foo', 'FOO'])
usage: PROG [-h] [-f FOO] bar
PROG: error: the following arguments are required: bar
```

By default, `argparse` automatically handles the internal naming and
display names of arguments, simplifying the process without requiring
additional configuration.
As such, you do not need to specify the [dest](https://docs.python.org/3/library/argparse.html#dest) and [metavar](https://docs.python.org/3/library/argparse.html#metavar) parameters.
For optional arguments, the [dest](https://docs.python.org/3/library/argparse.html#dest) parameter defaults to the argument name, with
underscores `_` replacing hyphens `-`. The [metavar](https://docs.python.org/3/library/argparse.html#metavar) parameter defaults to
the upper-cased name. For example:

```
>>> parser = argparse.ArgumentParser(prog='PROG')
>>> parser.add_argument('--foo-bar')
>>> parser.parse_args(['--foo-bar', 'FOO-BAR'])
Namespace(foo_bar='FOO-BAR')
>>> parser.print_help()
usage:  [-h] [--foo-bar FOO-BAR]

optional arguments:
 -h, --help  show this help message and exit
 --foo-bar FOO-BAR
```