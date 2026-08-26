---
id: python-the-add-argument-method-https-docs-python-org-3-library-argp-49b35a18
type: concept
title: The add\_argument() method[¶](https://docs.python.org/3/library/argparse.html#the-add-argument-method
  "Link to this heading")
description: ArgumentParser.add\_argument(*name or flags...*, *\**[, *action*][, *nargs*][,
  *const*][, *default*][, *type*][, *choices*][, *required*][, *help*][, *metavar*][,
  *dest*][, *deprecated*])[¶](https://d
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## The add\_argument() method[¶](https://docs.python.org/3/library/argparse.html#the-add-argument-method "Link to this heading")

ArgumentParser.add\_argument(*name or flags...*, *\**[, *action*][, *nargs*][, *const*][, *default*][, *type*][, *choices*][, *required*][, *help*][, *metavar*][, *dest*][, *deprecated*])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "Link to this definition")
:   Define how a single command-line argument should be parsed. Each parameter
    has its own more detailed description below, but in short they are:

    - [name or flags](https://docs.python.org/3/library/argparse.html#name-or-flags) - Either a name or a list of option strings, e.g. `'foo'`
      or `'-f', '--foo'`.
    - [action](https://docs.python.org/3/library/argparse.html#action) - The basic type of action to be taken when this argument is
      encountered at the command line.
    - [nargs](https://docs.python.org/3/library/argparse.html#nargs) - The number of command-line arguments that should be consumed.
    - [const](https://docs.python.org/3/library/argparse.html#const) - A constant value required by some [action](https://docs.python.org/3/library/argparse.html#action) and [nargs](https://docs.python.org/3/library/argparse.html#nargs) selections.
    - [default](https://docs.python.org/3/library/argparse.html#default) - The value produced if the argument is absent from the
      command line and if it is absent from the namespace object.
    - [type](https://docs.python.org/3/library/argparse.html#type) - The type to which the command-line argument should be converted.
    - [choices](https://docs.python.org/3/library/argparse.html#choices) - A sequence of the allowable values for the argument.
    - [required](https://docs.python.org/3/library/argparse.html#required) - Whether or not the command-line option may be omitted
      (optionals only).
    - [help](https://docs.python.org/3/library/argparse.html#help) - A brief description of what the argument does.
    - [metavar](https://docs.python.org/3/library/argparse.html#metavar) - A name for the argument in usage messages.
    - [dest](https://docs.python.org/3/library/argparse.html#dest) - The name of the attribute to be added to the object returned by
      [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args").
    - [deprecated](https://docs.python.org/3/library/argparse.html#deprecated) - Whether or not use of the argument is deprecated.

    The method returns an [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action") object representing the argument.

The following sections describe how each of these are used.