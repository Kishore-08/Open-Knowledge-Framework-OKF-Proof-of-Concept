---
id: python-examples-https-docs-python-org-3-library-tomllib-html-exampl-00f2bfaf
type: concept
title: Examples[¶](https://docs.python.org/3/library/tomllib.html#examples "Link to
  this heading")
description: 'Parsing a TOML file:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tomllib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Examples[¶](https://docs.python.org/3/library/tomllib.html#examples "Link to this heading")

Parsing a TOML file:

```
import tomllib

with open("pyproject.toml", "rb") as f:
    data = tomllib.load(f)
```

Parsing a TOML string:

```
import tomllib

toml_str = """
python-version = "3.11.0"
python-implementation = "CPython"
"""

data = tomllib.loads(toml_str)
```