---
id: python-partial-parsing-https-docs-python-org-3-library-argparse-htm-49b35a18
type: concept
title: Partial parsing[¶](https://docs.python.org/3/library/argparse.html#partial-parsing
  "Link to this heading")
description: ArgumentParser.parse\_known\_args(*args=None*, *namespace=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Partial parsing[¶](https://docs.python.org/3/library/argparse.html#partial-parsing "Link to this heading")

ArgumentParser.parse\_known\_args(*args=None*, *namespace=None*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "Link to this definition")
:   Sometimes a script only needs to handle a specific set of command-line
    arguments, leaving any unrecognized arguments for another script or program.
    In these cases, the `parse_known_args()` method can be
    useful.

    This method works similarly to [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args"), but it does
    not raise an error for extra, unrecognized arguments. Instead, it parses the
    known arguments and returns a two item tuple that contains the populated
    namespace and the list of any unrecognized arguments.

    ```
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo', action='store_true')
    >>> parser.add_argument('bar')
    >>> parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
    (Namespace(bar='BAR', foo=True), ['--badger', 'spam'])
    ```

Warning

[Prefix matching](https://docs.python.org/3/library/argparse.html#prefix-matching) rules apply to
[`parse_known_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_known_args "argparse.ArgumentParser.parse_known_args"). The parser may consume an option even if it’s just
a prefix of one of its known options, instead of leaving it in the remaining
arguments list.