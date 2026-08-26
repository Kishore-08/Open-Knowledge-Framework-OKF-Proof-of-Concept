---
id: python-argument-groups-https-docs-python-org-3-library-argparse-htm-49b35a18
type: concept
title: Argument groups[¶](https://docs.python.org/3/library/argparse.html#argument-groups
  "Link to this heading")
description: ArgumentParser.add\_argument\_group(*title=None*, *description=None*,
  *\**[, *argument\_default*][, *conflict\_handler*])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Argument groups[¶](https://docs.python.org/3/library/argparse.html#argument-groups "Link to this heading")

ArgumentParser.add\_argument\_group(*title=None*, *description=None*, *\**[, *argument\_default*][, *conflict\_handler*])[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "Link to this definition")
:   By default, [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") groups command-line arguments into
    “positional arguments” and “options” when displaying help
    messages. When there is a better conceptual grouping of arguments than this
    default one, appropriate groups can be created using the
    `add_argument_group()` method:

    ```
    >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
    >>> group = parser.add_argument_group('group')
    >>> group.add_argument('--foo', help='foo help')
    >>> group.add_argument('bar', help='bar help')
    >>> parser.print_help()
    usage: PROG [--foo FOO] bar

    group:
      bar    bar help
      --foo FOO  foo help
    ```

    The `add_argument_group()` method returns an argument group object which
    has an [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") method just like a regular
    [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"). When an argument is added to the group, the parser
    treats it just like a normal argument, but displays the argument in a
    separate group for help messages. The `add_argument_group()` method
    accepts *title* and *description* arguments which can be used to
    customize this display:

    ```
    >>> parser = argparse.ArgumentParser(prog='PROG', add_help=False)
    >>> group1 = parser.add_argument_group('group1', 'group1 description')
    >>> group1.add_argument('foo', help='foo help')
    >>> group2 = parser.add_argument_group('group2', 'group2 description')
    >>> group2.add_argument('--bar', help='bar help')
    >>> parser.print_help()
    usage: PROG [--bar BAR] foo

    group1:
      group1 description

      foo    foo help

    group2:
      group2 description

      --bar BAR  bar help
    ```

    The optional, keyword-only parameters [argument\_default](https://docs.python.org/3/library/argparse.html#argument-default) and [conflict\_handler](https://docs.python.org/3/library/argparse.html#conflict-handler)
    allow for finer-grained control of the behavior of the argument group. These
    parameters have the same meaning as in the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor,
    but apply specifically to the argument group rather than the entire parser.

    Note that any arguments not in your user-defined groups will end up back
    in the usual “positional arguments” and “optional arguments” sections.

    Within each argument group, arguments are displayed in help output in the
    order in which they are added.

    Deprecated since version 3.11, removed in version 3.14: Calling `add_argument_group()` on an argument group now raises an
    exception. This nesting was never supported, often failed to work
    correctly, and was unintentionally exposed through inheritance.

    Deprecated since version 3.14: Passing [prefix\_chars](https://docs.python.org/3/library/argparse.html#prefix-chars) to `add_argument_group()`
    is now deprecated.