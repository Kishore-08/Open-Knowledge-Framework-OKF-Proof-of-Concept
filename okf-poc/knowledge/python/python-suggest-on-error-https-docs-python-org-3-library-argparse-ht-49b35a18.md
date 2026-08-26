---
id: python-suggest-on-error-https-docs-python-org-3-library-argparse-ht-49b35a18
type: concept
title: suggest\_on\_error[¶](https://docs.python.org/3/library/argparse.html#suggest-on-error
  "Link to this heading")
description: By default, when a user passes an invalid argument choice or subparser
  name,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### suggest\_on\_error[¶](https://docs.python.org/3/library/argparse.html#suggest-on-error "Link to this heading")

By default, when a user passes an invalid argument choice or subparser name,
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") will exit with error info and list the permissible
argument choices (if specified) or subparser names as part of the error message.

If the user would like to enable suggestions for mistyped argument choices and
subparser names, the feature can be enabled by setting `suggest_on_error` to
`True`. Note that this only applies for arguments when the choices specified
are strings:

```
>>> parser = argparse.ArgumentParser(suggest_on_error=True)
>>> parser.add_argument('--action', choices=['debug', 'dryrun'])
>>> parser.parse_args(['--action', 'debugg'])
usage: tester.py [-h] [--action {debug,dryrun}]
tester.py: error: argument --action: invalid choice: 'debugg', maybe you meant 'debug'? (choose from debug, dryrun)
```

If you’re writing code that needs to be compatible with older Python versions
and want to opportunistically use `suggest_on_error` when it’s available, you
can set it as an attribute after initializing the parser instead of using the
keyword argument:

```
>>> parser = argparse.ArgumentParser(description='Process some integers.')
>>> parser.suggest_on_error = True
```

Added in version 3.14.