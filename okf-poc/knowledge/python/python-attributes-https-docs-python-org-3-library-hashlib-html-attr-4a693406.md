---
id: python-attributes-https-docs-python-org-3-library-hashlib-html-attr-4a693406
type: concept
title: Attributes[¶](https://docs.python.org/3/library/hashlib.html#attributes "Link
  to this heading")
description: 'Hashlib provides the following constant module attributes:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Attributes[¶](https://docs.python.org/3/library/hashlib.html#attributes "Link to this heading")

Hashlib provides the following constant module attributes:

hashlib.algorithms\_guaranteed[¶](https://docs.python.org/3/library/hashlib.html#hashlib.algorithms_guaranteed "Link to this definition")
:   A set containing the names of the hash algorithms guaranteed to be supported
    by this module on all platforms. Note that ‘md5’ is in this list despite
    some upstream vendors offering an odd “FIPS compliant” Python build that
    excludes it.

    Added in version 3.2.

hashlib.algorithms\_available[¶](https://docs.python.org/3/library/hashlib.html#hashlib.algorithms_available "Link to this definition")
:   A set containing the names of the hash algorithms that are available in the
    running Python interpreter. These names will be recognized when passed to
    [`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new"). [`algorithms_guaranteed`](https://docs.python.org/3/library/hashlib.html#hashlib.algorithms_guaranteed "hashlib.algorithms_guaranteed") will always be a subset. The
    same algorithm may appear multiple times in this set under different names
    (thanks to OpenSSL).

    Added in version 3.2.