---
id: python-parser-defaults-https-docs-python-org-3-library-argparse-htm-49b35a18
type: concept
title: Parser defaults[¶](https://docs.python.org/3/library/argparse.html#parser-defaults
  "Link to this heading")
description: ArgumentParser.set\_defaults(*\*\*kwargs*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Parser defaults[¶](https://docs.python.org/3/library/argparse.html#parser-defaults "Link to this heading")

ArgumentParser.set\_defaults(*\*\*kwargs*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "Link to this definition")
:   Most of the time, the attributes of the object returned by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args")
    will be fully determined by inspecting the command-line arguments and the argument
    actions. `set_defaults()` allows some additional
    attributes that are determined without any inspection of the command line to
    be added:

    ```
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('foo', type=int)
    >>> parser.set_defaults(bar=42, baz='badger')
    >>> parser.parse_args(['736'])
    Namespace(bar=42, baz='badger', foo=736)
    ```

    Note that defaults can be set at both the parser level using `set_defaults()`
    and at the argument level using [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"). If both are called for the
    same argument, the last default set for an argument is used:

    ```
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo', default='bar')
    >>> parser.set_defaults(foo='spam')
    >>> parser.parse_args([])
    Namespace(foo='spam')
    ```

    Parser-level defaults can be particularly useful when working with multiple
    parsers. See the [`add_subparsers()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers "argparse.ArgumentParser.add_subparsers") method for an
    example of this type.

ArgumentParser.get\_default(*dest*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.get_default "Link to this definition")
:   Get the default value for a namespace attribute, as set by either
    [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") or by
    [`set_defaults()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.set_defaults "argparse.ArgumentParser.set_defaults"):

    ```
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo', default='badger')
    >>> parser.get_default('foo')
    'badger'
    ```