---
id: python-allow-abbrev-https-docs-python-org-3-library-argparse-html-a-49b35a18
type: concept
title: allow\_abbrev[¶](https://docs.python.org/3/library/argparse.html#allow-abbrev
  "Link to this heading")
description: Normally, when you pass an argument list to the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### allow\_abbrev[¶](https://docs.python.org/3/library/argparse.html#allow-abbrev "Link to this heading")

Normally, when you pass an argument list to the
[`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method of an [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"),
it [recognizes abbreviations](https://docs.python.org/3/library/argparse.html#prefix-matching) of long options.

This feature can be disabled by setting `allow_abbrev` to `False`:

```
>>> parser = argparse.ArgumentParser(prog='PROG', allow_abbrev=False)
>>> parser.add_argument('--foobar', action='store_true')
>>> parser.add_argument('--foonley', action='store_false')
>>> parser.parse_args(['--foon'])
usage: PROG [-h] [--foobar] [--foonley]
PROG: error: unrecognized arguments: --foon
```

Added in version 3.5.