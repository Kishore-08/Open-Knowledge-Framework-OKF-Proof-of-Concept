---
id: python-intermixed-parsing-https-docs-python-org-3-library-argparse--49b35a18
type: concept
title: Intermixed parsing[¶](https://docs.python.org/3/library/argparse.html#intermixed-parsing
  "Link to this heading")
description: ArgumentParser.parse\_intermixed\_args(*args=None*, *namespace=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Intermixed parsing[¶](https://docs.python.org/3/library/argparse.html#intermixed-parsing "Link to this heading")

ArgumentParser.parse\_intermixed\_args(*args=None*, *namespace=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "Link to this definition")

ArgumentParser.parse\_known\_intermixed\_args(*args=None*, *namespace=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_intermixed_args "Link to this definition")
:   A number of Unix commands allow the user to intermix optional arguments with
    positional arguments. The [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args")
    and `parse_known_intermixed_args()` methods
    support this parsing style.

    These parsers do not support all the `argparse` features, and will raise
    exceptions if unsupported features are used. In particular, subparsers,
    and mutually exclusive groups that include both
    optionals and positionals are not supported.

    The following example shows the difference between
    [`parse_known_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "argparse.ArgumentParser.parse_known_args") and
    [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args"): the former returns `['2',
    '3']` as unparsed arguments, while the latter collects all the positionals
    into `rest`.

    ```
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo')
    >>> parser.add_argument('cmd')
    >>> parser.add_argument('rest', nargs='*', type=int)
    >>> parser.parse_known_args('doit 1 --foo bar 2 3'.split())
    (Namespace(cmd='doit', foo='bar', rest=[1]), ['2', '3'])
    >>> parser.parse_intermixed_args('doit 1 --foo bar 2 3'.split())
    Namespace(cmd='doit', foo='bar', rest=[1, 2, 3])
    ```

    `parse_known_intermixed_args()` returns a two item tuple
    containing the populated namespace and the list of remaining argument strings.
    [`parse_intermixed_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args "argparse.ArgumentParser.parse_intermixed_args") raises an error if there are any
    remaining unparsed argument strings.

    Added in version 3.7.