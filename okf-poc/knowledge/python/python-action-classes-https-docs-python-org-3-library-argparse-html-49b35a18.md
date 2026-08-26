---
id: python-action-classes-https-docs-python-org-3-library-argparse-html-49b35a18
type: concept
title: Action classes[¶](https://docs.python.org/3/library/argparse.html#action-classes
  "Link to this heading")
description: '`Action` classes implement the Action API, a callable which returns
  a callable'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Action classes[¶](https://docs.python.org/3/library/argparse.html#action-classes "Link to this heading")

`Action` classes implement the Action API, a callable which returns a callable
which processes arguments from the command-line. Any object which follows
this API may be passed as the `action` parameter to
[`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument").

*class* argparse.Action(*option\_strings*, *dest*, *nargs=None*, *const=None*, *default=None*, *type=None*, *choices=None*, *required=False*, *help=None*, *metavar=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.Action "Link to this definition")
:   `Action` objects are used by an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") to represent the information
    needed to parse a single argument from one or more strings from the
    command line. The `Action` class must accept the two positional arguments
    plus any keyword arguments passed to [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument")
    except for the `action` itself.

    Instances of `Action` (or return value of any callable to the
    `action` parameter) should have attributes `dest`,
    `option_strings`, `default`, `type`, `required`,
    `help`, etc. defined. The easiest way to ensure these attributes
    are defined is to call `Action.__init__()`.

    \_\_call\_\_(*parser*, *namespace*, *values*, *option\_string=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.Action.__call__ "Link to this definition")
    :   `Action` instances should be callable, so subclasses must override the
        `__call__()` method, which should accept four parameters:

        - *parser* - The [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") object which contains this action.
        - *namespace* - The [`Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") object that will be returned by
          [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"). Most actions add an attribute to this
          object using [`setattr()`](https://docs.python.org/3/library/functions.html#setattr "setattr").
        - *values* - The associated command-line arguments, with any type conversions
          applied. Type conversions are specified with the [type](https://docs.python.org/3/library/argparse.html#type) keyword argument to
          [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument").
        - *option\_string* - The option string that was used to invoke this action.
          The `option_string` argument is optional, and will be absent if the action
          is associated with a positional argument.

        The `__call__()` method may perform arbitrary actions, but will typically set
        attributes on the `namespace` based on `dest` and `values`.

    format\_usage()[¶](https://docs.python.org/3/library/argparse.html#argparse.Action.format_usage "Link to this definition")
    :   `Action` subclasses can define a `format_usage()` method that takes no argument
        and return a string which will be used when printing the usage of the program.
        If such method is not provided, a sensible default will be used.

*class* argparse.BooleanOptionalAction[¶](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction "Link to this definition")
:   A subclass of [`Action`](https://docs.python.org/3/library/argparse.html#argparse.Action "argparse.Action") for handling boolean flags with positive
    and negative opti