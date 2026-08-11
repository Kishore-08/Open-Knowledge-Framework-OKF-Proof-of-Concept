---
id: python-text-transforms-https-docs-python-org-3-library-codecs-html--6b1d6ecb
type: concept
title: Text Transforms[¶](https://docs.python.org/3/library/codecs.html#text-transforms
  "Link to this heading")
description: 'The following codec provides a text transform: a [`str`](https://docs.python.org/3/library/stdtypes.html#str
  "str") to `str`'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Text Transforms[¶](https://docs.python.org/3/library/codecs.html#text-transforms "Link to this heading")

The following codec provides a text transform: a [`str`](https://docs.python.org/3/library/stdtypes.html#str "str") to `str`
mapping. It is not supported by [`str.encode()`](https://docs.python.org/3/library/stdtypes.html#str.encode "str.encode") (which only produces
[`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") output).

| Codec | Aliases | Meaning |
| --- | --- | --- |
| rot\_13 | rot13 | Return the Caesar-cypher encryption of the operand. |

Added in version 3.2: Restoration of the `rot_13` text transform.

Changed in version 3.4: Restoration of the `rot13` alias.