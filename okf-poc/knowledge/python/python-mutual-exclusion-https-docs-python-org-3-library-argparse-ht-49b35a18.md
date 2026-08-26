---
id: python-mutual-exclusion-https-docs-python-org-3-library-argparse-ht-49b35a18
type: concept
title: Mutual exclusion[¶](https://docs.python.org/3/library/argparse.html#mutual-exclusion
  "Link to this heading")
description: ArgumentParser.add\_mutually\_exclusive\_group(*required=False*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Mutual exclusion[¶](https://docs.python.org/3/library/argparse.html#mutual-exclusion "Link to this heading")

ArgumentParser.add\_mutually\_exclusive\_group(*required=False*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group "Link to this definition")
:   Create a mutually exclusive group. `argparse` will make sure that only
    one of the arguments in the mutually exclusive group was present on the
    command line:

    ```
    >>> parser = argparse.ArgumentParser(prog='PROG')
    >>> group = parser.add_mutually_exclusive_group()
    >>> group.add_argument('--foo', action='store_true')
    >>> group.add_argument('--bar', action='store_false')
    >>> parser.parse_args(['--foo'])
    Namespace(bar=True, foo=True)
    >>> parser.parse_args(['--bar'])
    Namespace(bar=False, foo=False)
    >>> parser.parse_args(['--foo', '--bar'])
    usage: PROG [-h] [--foo | --bar]
    PROG: error: argument --bar: not allowed with argument --foo
    ```

    The `add_mutually_exclusive_group()` method also accepts a *required*
    argument, to indicate that at least one of the mutually exclusive arguments
    is required:

    ```
    >>> parser = argparse.ArgumentParser(prog='PROG')
    >>> group = parser.add_mutually_exclusive_group(required=True)
    >>> group.add_argument('--foo', action='store_true')
    >>> group.add_argument('--bar', action='store_false')
    >>> parser.parse_args([])
    usage: PROG [-h] (--foo | --bar)
    PROG: error: one of the arguments --foo --bar is required
    ```

    Note that currently mutually exclusive argument groups do not support the
    *title* and *description* arguments of
    [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group"). However, a mutually exclusive
    group can be added to an argument group that has a title and description.
    For example:

    ```
    >>> parser = argparse.ArgumentParser(prog='PROG')
    >>> group = parser.add_argument_group('Group title', 'Group description')
    >>> exclusive_group = group.add_mutually_exclusive_group(required=True)
    >>> exclusive_group.add_argument('--foo', help='foo help')
    >>> exclusive_group.add_argument('--bar', help='bar help')
    >>> parser.print_help()
    usage: PROG [-h] (--foo FOO | --bar BAR)

    options:
      -h, --help  show this help message and exit

    Group title:
      Group description

      --foo FOO   foo help
      --bar BAR   bar help
    ```

    Deprecated since version 3.11, removed in version 3.14: Calling [`add_argument_group()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument_group "argparse.ArgumentParser.add_argument_group") or `add_mutually_exclusive_group()`
    on a mutually exclusive group now raises an exception. This nesting was
    never supported, often failed to work correctly, and was unintentionally
    exposed through inheritance.