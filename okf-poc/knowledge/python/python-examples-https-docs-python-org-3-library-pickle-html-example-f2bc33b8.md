---
id: python-examples-https-docs-python-org-3-library-pickle-html-example-f2bc33b8
type: concept
title: Examples[¶](https://docs.python.org/3/library/pickle.html#examples "Link to
  this heading")
description: For the simplest code, use the [`dump()`](https://docs.python.org/3/library/pickle.html#pickle.dump
  "pickle.dump") and [`load()`](https://docs.python.org/3/library/pickle.html#pickle.load
  "pickle.load
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Examples[¶](https://docs.python.org/3/library/pickle.html#examples "Link to this heading")

For the simplest code, use the [`dump()`](https://docs.python.org/3/library/pickle.html#pickle.dump "pickle.dump") and [`load()`](https://docs.python.org/3/library/pickle.html#pickle.load "pickle.load") functions.

```
import pickle

# An arbitrary collection of objects supported by pickle.
data = {
    'a': [1, 2.0, 3+4j],
    'b': ("character string", b"byte string"),
    'c': {None, True, False}
}

with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)
```

The following example reads the resulting pickled data.

```
import pickle

with open('data.pickle', 'rb') as f:
    # The protocol version used is detected automatically, so we do not
    # have to specify it.
    data = pickle.load(f)
```