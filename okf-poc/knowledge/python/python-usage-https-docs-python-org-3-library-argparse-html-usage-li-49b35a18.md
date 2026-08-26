---
id: python-usage-https-docs-python-org-3-library-argparse-html-usage-li-49b35a18
type: concept
title: usage[¶](https://docs.python.org/3/library/argparse.html#usage "Link to this
  heading")
description: By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser
  "argparse.ArgumentParser") calculates the usage message from the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### usage[¶](https://docs.python.org/3/library/argparse.html#usage "Link to this heading")

By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") calculates the usage message from the
arguments it contains. The default message can be overridden with the
`usage=` keyword argument:

```
>>> parser = argparse.ArgumentParser(prog='PROG', usage='%(prog)s [options]')
>>> parser.add_argument('--foo', nargs='?', help='foo help')
>>> parser.add_argument('bar', nargs='+', help='bar help')
>>> parser.print_help()
usage: PROG [options]

positional arguments:
 bar          bar help

options:
 -h, --help   show this help message and exit
 --foo [FOO]  foo help
```

The `%(prog)s` format specifier is available to fill in the program name in
your usage messages.

When a custom usage message is specified for the main parser, you may also want to
consider passing the `prog` argument to [`add_subparsers()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "argparse.ArgumentParser.add_subparsers")
or the `prog` and the `usage` arguments to
`add_parser()`, to ensure consistent command prefixes and
usage information across subparsers.