---
id: python-required-https-docs-python-org-3-library-argparse-html-requi-49b35a18
type: concept
title: required[¶](https://docs.python.org/3/library/argparse.html#required "Link
  to this heading")
description: In general, the `argparse` module assumes that flags like `-f` and `--bar`
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### required[¶](https://docs.python.org/3/library/argparse.html#required "Link to this heading")

In general, the `argparse` module assumes that flags like `-f` and `--bar`
indicate *optional* arguments, which can always be omitted at the command line.
To make an option *required*, `True` can be specified for the `required=`
keyword argument to [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument"):

```
>>> parser = argparse.ArgumentParser()
>>> parser.add_argument('--foo', required=True)
>>> parser.parse_args(['--foo', 'BAR'])
Namespace(foo='BAR')
>>> parser.parse_args([])
usage: [-h] --foo FOO
: error: the following arguments are required: --foo
```

As the example shows, if an option is marked as `required`,
[`parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") will report an error if that option is not
present at the command line.

Note

Required options are generally considered bad form because users expect
*options* to be *optional*, and thus they should be avoided when possible.