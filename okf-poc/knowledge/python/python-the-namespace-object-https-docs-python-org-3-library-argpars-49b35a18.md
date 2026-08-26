---
id: python-the-namespace-object-https-docs-python-org-3-library-argpars-49b35a18
type: concept
title: The Namespace object[¶](https://docs.python.org/3/library/argparse.html#the-namespace-object
  "Link to this heading")
description: '*class* argparse.Namespace[¶](https://docs.python.org/3/library/argparse.html#argparse.Namespace
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### The Namespace object[¶](https://docs.python.org/3/library/argparse.html#the-namespace-object "Link to this heading")

*class* argparse.Namespace[¶](https://docs.python.org/3/library/argparse.html#argparse.Namespace "Link to this definition")
:   Simple class used by default by [`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") to create
    an object holding attributes and return it.

    This class is deliberately simple, just an [`object`](https://docs.python.org/3/library/functions.html#object "object") subclass with a
    readable string representation. If you prefer to have dict-like view of the
    attributes, you can use the standard Python idiom, [`vars()`](https://docs.python.org/3/library/functions.html#vars "vars"):

    ```
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo')
    >>> args = parser.parse_args(['--foo', 'BAR'])
    >>> vars(args)
    {'foo': 'BAR'}
    ```

    It may also be useful to have an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") assign attributes to an
    already existing object, rather than a new `Namespace` object. This can
    be achieved by specifying the `namespace=` keyword argument:

    ```
    >>> class C:
    ...     pass
    ...
    >>> c = C()
    >>> parser = argparse.ArgumentParser()
    >>> parser.add_argument('--foo')
    >>> parser.parse_args(args=['--foo', 'BAR'], namespace=c)
    >>> c.foo
    'BAR'
    ```

## Other utilities[¶](https://docs.python.org/3/library/argparse.html#other-utilities "Link to this heading")