---
id: python-stateful-extraction-filter-example-https-docs-python-org-3-l-47076c99
type: concept
title: Stateful extraction filter example[¶](https://docs.python.org/3/library/tarfile.html#stateful-extraction-filter-example
  "Link to this heading")
description: While *tarfile*’s extraction methods take a simple *filter* callable,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Stateful extraction filter example[¶](https://docs.python.org/3/library/tarfile.html#stateful-extraction-filter-example "Link to this heading")

While *tarfile*’s extraction methods take a simple *filter* callable,
custom filters may be more complex objects with an internal state.
It may be useful to write these as context managers, to be used like this:

```
with StatefulFilter() as filter_func:
    tar.extractall(path, filter=filter_func)
```

Such a filter can be written as, for example:

```
class StatefulFilter:
    def __init__(self):
        self.file_count = 0

    def __enter__(self):
        return self

    def __call__(self, member, path):
        self.file_count += 1
        return member

    def __exit__(self, *exc_info):
        print(f'{self.file_count} files extracted')
```