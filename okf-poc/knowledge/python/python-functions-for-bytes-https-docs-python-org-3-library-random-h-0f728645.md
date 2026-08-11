---
id: python-functions-for-bytes-https-docs-python-org-3-library-random-h-0f728645
type: concept
title: Functions for bytes[¶](https://docs.python.org/3/library/random.html#functions-for-bytes
  "Link to this heading")
description: random.randbytes(*n*)[¶](https://docs.python.org/3/library/random.html#random.randbytes
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Functions for bytes[¶](https://docs.python.org/3/library/random.html#functions-for-bytes "Link to this heading")

random.randbytes(*n*)[¶](https://docs.python.org/3/library/random.html#random.randbytes "Link to this definition")
:   Generate *n* random bytes.

    This method should not be used for generating security tokens.
    Use [`secrets.token_bytes()`](https://docs.python.org/3/library/secrets.html#secrets.token_bytes "secrets.token_bytes") instead.

    Added in version 3.9.