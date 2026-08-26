---
id: python-tutorial-https-docs-python-org-3-library-optparse-html-tutor-f59a6996
type: concept
title: Tutorial[¶](https://docs.python.org/3/library/optparse.html#tutorial "Link
  to this heading")
description: While `optparse` is quite flexible and powerful, it’s also straightforward
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Tutorial[¶](https://docs.python.org/3/library/optparse.html#tutorial "Link to this heading")

While `optparse` is quite flexible and powerful, it’s also straightforward
to use in most cases. This section covers the code patterns that are common to
any `optparse`-based program.

First, you need to import the OptionParser class; then, early in the main
program, create an OptionParser instance:

```
from optparse import OptionParser
...
parser = OptionParser()
```

Then you can start defining options. The basic syntax is:

```
parser.add_option(opt_str, ...,
                  attr=value, ...)
```

Each option has one or more option strings, such as `-f` or `--file`,
and several option attributes that tell `optparse` what to expect and what
to do when it encounters that option on the command line.

Typically, each option will have one short option string and one long option
string, e.g.:

```
parser.add_option("-f", "--file", ...)
```

You’re free to define as many short option strings and as many long option
strings as you like (including zero), as long as there is at least one option
string overall.

The option strings passed to [`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option") are effectively
labels for the
option defined by that call. For brevity, we will frequently refer to
*encountering an option* on the command line; in reality, `optparse`
encounters *option strings* and looks up options from them.

Once all of your options are defined, instruct `optparse` to parse your
program’s command line:

```
(options, args) = parser.parse_args()
```

(If you like, you can pass a custom argument list to [`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args"), but
that’s rarely necessary: by default it uses `sys.argv[1:]`.)

[`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args") returns two values:

- `options`, an object containing values for all of your options—e.g. if
  `--file` takes a single string argument, then `options.file` will be the
  filename supplied by the user, or `None` if the user did not supply that
  option
- `args`, the list of positional arguments leftover after parsing options

This tutorial section only covers the four most important option attributes:
[`action`](https://docs.python.org/3/library/optparse.html#optparse.Option.action "optparse.Option.action"), [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type"), [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")
(destination), and [`help`](https://docs.python.org/3/library/optparse.html#optparse.Option.help "optparse.Option.help"). Of these, `action` is the
most fundamental.