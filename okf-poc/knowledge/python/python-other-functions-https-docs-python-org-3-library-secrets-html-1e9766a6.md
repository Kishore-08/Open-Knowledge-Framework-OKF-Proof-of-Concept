---
id: python-other-functions-https-docs-python-org-3-library-secrets-html-1e9766a6
type: concept
title: Other functions[¶](https://docs.python.org/3/library/secrets.html#other-functions
  "Link to this heading")
description: secrets.compare\_digest(*a*, *b*)[¶](https://docs.python.org/3/library/secrets.html#secrets.compare_digest
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/secrets.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Other functions[¶](https://docs.python.org/3/library/secrets.html#other-functions "Link to this heading")

secrets.compare\_digest(*a*, *b*)[¶](https://docs.python.org/3/library/secrets.html#secrets.compare_digest "Link to this definition")
:   Return `True` if strings or
    [bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object)
    *a* and *b* are equal, otherwise `False`,
    using a “constant-time compare” to reduce the risk of
    [timing attacks](https://web.archive.org/web/20250815071532/https://codahale.com/a-lesson-in-timing-attacks/).
    See [`hmac.compare_digest()`](https://docs.python.org/3/library/hmac.html#hmac.compare_digest "hmac.compare_digest") for additional details.