---
id: python-registering-custom-types-or-actions-https-docs-python-org-3--49b35a18
type: concept
title: Registering custom types or actions[¶](https://docs.python.org/3/library/argparse.html#registering-custom-types-or-actions
  "Link to this heading")
description: ArgumentParser.register(*registry\_name*, *value*, *object*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Registering custom types or actions[¶](https://docs.python.org/3/library/argparse.html#registering-custom-types-or-actions "Link to this heading")

ArgumentParser.register(*registry\_name*, *value*, *object*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register "Link to this definition")
:   Sometimes it’s desirable to use a custom string in error messages to provide
    more user-friendly output. In these cases, `register()` can be used to
    register custom actions or types with a parser and allow you to reference the
    type by their registered name instead of their callable name.

    The `register()` method accepts three arguments - a *registry\_name*,
    specifying the internal registry where the object will be stored (e.g.,
    `action`, `type`), *value*, which is the key under which the object will
    be registered, and object, the callable to be registered.

    The following example shows how to register a custom type with a parser:

    ```
    >>> import argparse
    >>> parser = argparse.ArgumentParser()
    >>> parser.register('type', 'hexadecimal integer', lambda s: int(s, 16))
    >>> parser.add_argument('--foo', type='hexadecimal integer')
    _StoreAction(option_strings=['--foo'], dest='foo', nargs=None, const=None, default=None, type='hexadecimal integer', choices=None, required=False, help=None, metavar=None, deprecated=False)
    >>> parser.parse_args(['--foo', '0xFA'])
    Namespace(foo=250)
    >>> parser.parse_args(['--foo', '1.2'])
    usage: PROG [-h] [--foo FOO]
    PROG: error: argument --foo: invalid 'hexadecimal integer' value: '1.2'
    ```