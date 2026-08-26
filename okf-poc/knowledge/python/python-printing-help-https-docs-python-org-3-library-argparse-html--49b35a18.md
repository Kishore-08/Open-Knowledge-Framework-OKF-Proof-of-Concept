---
id: python-printing-help-https-docs-python-org-3-library-argparse-html--49b35a18
type: concept
title: Printing help[¶](https://docs.python.org/3/library/argparse.html#printing-help
  "Link to this heading")
description: In most typical applications, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args
  "argparse.ArgumentParser.parse_args") will take
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Printing help[¶](https://docs.python.org/3/library/argparse.html#printing-help "Link to this heading")

In most typical applications, [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") will take
care of formatting and printing any usage or error messages. However, several
formatting methods are available:

ArgumentParser.print\_usage(*file=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.print_usage "Link to this definition")
:   Print a brief description of how the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") should be
    invoked on the command line. If *file* is `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") is
    assumed.

ArgumentParser.print\_help(*file=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.print_help "Link to this definition")
:   Print a help message, including the program usage and information about the
    arguments registered with the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"). If *file* is
    `None`, [`sys.stdout`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") is assumed.

There are also variants of these methods that simply return a string instead of
printing it:

ArgumentParser.format\_usage()[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.format_usage "Link to this definition")
:   Return a string containing a brief description of how the
    [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") should be invoked on the command line.

ArgumentParser.format\_help()[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.format_help "Link to this definition")
:   Return a string containing a help message, including the program usage and
    information about the arguments registered with the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser").