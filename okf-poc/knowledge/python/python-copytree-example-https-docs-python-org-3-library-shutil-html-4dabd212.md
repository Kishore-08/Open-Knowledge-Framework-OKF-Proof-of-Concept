---
id: python-copytree-example-https-docs-python-org-3-library-shutil-html-4dabd212
type: concept
title: copytree example[¶](https://docs.python.org/3/library/shutil.html#copytree-example
  "Link to this heading")
description: 'An example that uses the [`ignore_patterns()`](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns
  "shutil.ignore_patterns") helper:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shutil.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### copytree example[¶](https://docs.python.org/3/library/shutil.html#copytree-example "Link to this heading")

An example that uses the [`ignore_patterns()`](https://docs.python.org/3/library/shutil.html#shutil.ignore_patterns "shutil.ignore_patterns") helper:

```
from shutil import copytree, ignore_patterns

copytree(source, destination, ignore=ignore_patterns('*.pyc', 'tmp*'))
```

This will copy everything except `.pyc` files and files or directories whose
name starts with `tmp`.

Another example that uses the *ignore* argument to add a logging call:

```
from shutil import copytree
import logging

def _logpath(path, names):
    logging.info('Working in %s', path)
    return []   # nothing will be ignored

copytree(source, destination, ignore=_logpath)
```