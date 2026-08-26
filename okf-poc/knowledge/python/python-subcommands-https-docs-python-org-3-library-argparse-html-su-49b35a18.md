---
id: python-subcommands-https-docs-python-org-3-library-argparse-html-su-49b35a18
type: concept
title: Subcommands[¶](https://docs.python.org/3/library/argparse.html#subcommands
  "Link to this heading")
description: ArgumentParser.add\_subparsers(*\**[, *title*][, *description*][, *prog*][,
  *parser\_class*][, *action*][, *dest*][, *required*][, *help*][, *metavar*])[¶](https://docs.python.org/3/library/argparse.h
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Subcommands[¶](https://docs.python.org/3/library/argparse.html#subcommands "Link to this heading")

ArgumentParser.add\_subparsers(*\**[, *title*][, *description*][, *prog*][, *parser\_class*][, *action*][, *dest*][, *required*][, *help*][, *metavar*])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "Link to this definition")
:   Many programs split up their functionality into a number of subcommands,
    for example, the `svn` program can invoke subcommands like `svn
    checkout`, `svn update`, and `svn commit`. Splitting up functionality
    this way can be a particularly good idea when a program performs several
    different functions which require different kinds of command-line arguments.
    [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") supports the creation of such subcommands with the
    `add_subparsers()` method. The `add_subparsers()` method is normally
    called with no arguments and returns a special action object. This object
    has a single method, `add_parser()`, which takes a
    command name and any `ArgumentParser` constructor arguments, and
    returns an `ArgumentParser` object that can be modified as usual.

    Description of parameters:

    - *title* - title for the sub-parser group in help output; by default
      “subcommands” if description is provided, otherwise uses title for
      positional arguments
    - *description* - description for the sub-parser group in help output, by
      default `None`
    - *prog* - usage information that will be displayed with subcommand help,
      by default the name of the program and any positional arguments before the
      subparser argument
    - *parser\_class* - class which will be used to create sub-parser instances, by
      default the class of the current parser (e.g. [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"))
    - [action](https://docs.python.org/3/library/argparse.html#action) - the basic type of action to be taken when this argument is
      encountered at the command line
    - [dest](https://docs.python.org/3/library/argparse.html#dest) - name of the attribute under which subcommand name will be
      stored; by default `None` and no value is stored
    - [required](https://docs.python.org/3/library/argparse.html#required) - Whether or not a subcommand must be provided, by default
      `False` (added in 3.7)
    - [help](https://docs.python.org/3/library/argparse.html#help) - help for sub-parser group in help output, by default `None`
    - [metavar](https://docs.python.org/3/library/argparse.html#metavar) - string presenting available subcommands in help; by default it
      is `None` and presents subcommands in form {cmd1, cmd2, ..}

    Some example usage:

    ```
    >>> # create the top-level parser
    >>> parser = argparse.ArgumentParser(prog='PROG')
    >>> parser.add_argument('--foo', action='store_true', help='foo help')
    >>> subparsers = parser.add_subparsers(help='subcommand help')
    >>>
    >>> # create the parser for the "a" command
    >>> parser_a = subparsers.add_parser('a', help='a help')
    >>> parser_a.add_argument('bar', type=int, help='bar help')
    >>>
    >>> # create the parser for the "b" command
    >>> parser_b = subparsers.add_parser('b', help='b help')
    >>> parser_b.add_argument('--baz', choices=('X', 'Y', 'Z'), help='baz help')
    >>>
    >>> # parse some argument lists
    >>> parser.parse_args(['a', '12'])
    Namespace(bar=12, foo=False)
    >>> parser.parse_args(['--foo', 'b', '--baz', 'Z'])
    Namespace(baz='Z', foo=True)
    ```

    Note that the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") will only contain
    attributes for the main parser and the subparser that was selected by the
    co