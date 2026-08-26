---
id: python-parents-https-docs-python-org-3-library-argparse-html-parent-49b35a18
type: concept
title: parents[¶](https://docs.python.org/3/library/argparse.html#parents "Link to
  this heading")
description: Sometimes, several parsers share a common set of arguments. Rather than
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### parents[¶](https://docs.python.org/3/library/argparse.html#parents "Link to this heading")

Sometimes, several parsers share a common set of arguments. Rather than
repeating the definitions of these arguments, a single parser with all the
shared arguments and passed to `parents=` argument to [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser")
can be used. The `parents=` argument takes a list of `ArgumentParser`
objects, collects all the positional and optional actions from them, and adds
these actions to the `ArgumentParser` object being constructed:

```
>>> parent_parser = argparse.ArgumentParser(add_help=False)
>>> parent_parser.add_argument('--parent', type=int)

>>> foo_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> foo_parser.add_argument('foo')
>>> foo_parser.parse_args(['--parent', '2', 'XXX'])
Namespace(foo='XXX', parent=2)

>>> bar_parser = argparse.ArgumentParser(parents=[parent_parser])
>>> bar_parser.add_argument('--bar')
>>> bar_parser.parse_args(['--bar', 'YYY'])
Namespace(bar='YYY', parent=None)
```

Note that most parent parsers will specify `add_help=False`. Otherwise, the
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") will see two `-h/--help` options (one in the parent
and one in the child) and raise an error.

Note

You must fully initialize the parsers before passing them via `parents=`.
If you change the parent parsers after the child parser, those changes will
not be reflected in the child.