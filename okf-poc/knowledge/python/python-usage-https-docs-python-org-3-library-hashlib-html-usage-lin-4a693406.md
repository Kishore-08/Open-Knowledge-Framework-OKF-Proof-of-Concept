---
id: python-usage-https-docs-python-org-3-library-hashlib-html-usage-lin-4a693406
type: concept
title: Usage[¶](https://docs.python.org/3/library/hashlib.html#usage "Link to this
  heading")
description: To obtain the digest of the byte string `b"Nobody inspects the spammish
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Usage[¶](https://docs.python.org/3/library/hashlib.html#usage "Link to this heading")

To obtain the digest of the byte string `b"Nobody inspects the spammish
repetition"`:

```
>>> import hashlib
>>> m = hashlib.sha256()
>>> m.update(b"Nobody inspects")
>>> m.update(b" the spammish repetition")
>>> m.digest()
b'\x03\x1e\xdd}Ae\x15\x93\xc5\xfe\\\x00o\xa5u+7\xfd\xdf\xf7\xbcN\x84:\xa6\xaf\x0c\x95\x0fK\x94\x06'
>>> m.hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
```

More condensed:

```
>>> hashlib.sha256(b"Nobody inspects the spammish repetition").hexdigest()
'031edd7d41651593c5fe5c006fa5752b37fddff7bc4e843aa6af0c950f4b9406'
```