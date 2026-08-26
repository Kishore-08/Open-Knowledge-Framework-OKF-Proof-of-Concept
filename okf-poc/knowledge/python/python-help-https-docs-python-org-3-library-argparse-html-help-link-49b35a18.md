---
id: python-help-https-docs-python-org-3-library-argparse-html-help-link-49b35a18
type: concept
title: help[¶](https://docs.python.org/3/library/argparse.html#help "Link to this
  heading")
description: The `help` value is a string containing a brief description of the argument.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### help[¶](https://docs.python.org/3/library/argparse.html#help "Link to this heading")

The `help` value is a string containing a brief description of the argument.
When a user requests help (usually by using `-h` or `--help` at the
command line), these `help` descriptions will be displayed with each
argument.

The `help` strings can include various format specifiers to avoid repetition
of things like the program name or the argument [default](https://docs.python.org/3/library/argparse.html#default). The available
specifiers include the program name, `%(prog)s` and most keyword arguments to
[`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"), e.g. `%(default)s`, `%(type)s`, etc.:

```
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('bar', nargs='?', type=int, default=42,
...                     help='the bar to %(prog)s (default: %(default)s)')
>>> parser.print_help()
usage: frobble [-h] [bar]

positional arguments:
 bar     the bar to frobble (default: 42)

options:
 -h, --help  show this help message and exit
```

As the help string supports %-formatting, if you want a literal `%` to appear
in the help string, you must escape it as `%%`.

`argparse` supports silencing the help entry for certain options, by
setting the `help` value to `argparse.SUPPRESS`:

```
>>> parser = argparse.ArgumentParser(prog='frobble')
>>> parser.add_argument('--foo', help=argparse.SUPPRESS)
>>> parser.print_help()
usage: frobble [-h]

options:
  -h, --help  show this help message and exit
```