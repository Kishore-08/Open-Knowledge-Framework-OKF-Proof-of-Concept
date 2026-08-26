---
id: python-prefix-chars-https-docs-python-org-3-library-argparse-html-p-49b35a18
type: concept
title: prefix\_chars[¶](https://docs.python.org/3/library/argparse.html#prefix-chars
  "Link to this heading")
description: Most command-line options will use `-` as the prefix, e.g. `-f/--foo`.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### prefix\_chars[¶](https://docs.python.org/3/library/argparse.html#prefix-chars "Link to this heading")

Most command-line options will use `-` as the prefix, e.g. `-f/--foo`.
Parsers that need to support different or additional prefix
characters, e.g. for options
like `+f` or `/foo`, may specify them using the `prefix_chars=` argument
to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor:

```
>>> parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+')
>>> parser.add_argument('+f')
>>> parser.add_argument('++bar')
>>> parser.parse_args('+f X ++bar Y'.split())
Namespace(bar='Y', f='X')
```

The `prefix_chars=` argument defaults to `'-'`. Supplying a set of
characters that does not include `-` will cause `-f/--foo` options to be
disallowed.