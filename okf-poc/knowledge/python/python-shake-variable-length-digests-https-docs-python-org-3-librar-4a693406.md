---
id: python-shake-variable-length-digests-https-docs-python-org-3-librar-4a693406
type: concept
title: SHAKE variable length digests[¶](https://docs.python.org/3/library/hashlib.html#shake-variable-length-digests
  "Link to this heading")
description: hashlib.shake\_128([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.shake_128
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## SHAKE variable length digests[¶](https://docs.python.org/3/library/hashlib.html#shake-variable-length-digests "Link to this heading")

hashlib.shake\_128([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.shake_128 "Link to this definition")

hashlib.shake\_256([*data*, ]*\**, *usedforsecurity=True*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.shake_256 "Link to this definition")

The [`shake_128()`](https://docs.python.org/3/library/hashlib.html#hashlib.shake_128 "hashlib.shake_128") and [`shake_256()`](https://docs.python.org/3/library/hashlib.html#hashlib.shake_256 "hashlib.shake_256") algorithms provide variable
length digests with length\_in\_bits//2 up to 128 or 256 bits of security.
As such, their digest methods require a length. Maximum length is not limited
by the SHAKE algorithm.

shake.digest(*length*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.shake.digest "Link to this definition")
:   Return the digest of the data passed to the [`update()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.update "hashlib.hash.update") method so far.
    This is a bytes object of size *length* which may contain bytes in
    the whole range from 0 to 255.

shake.hexdigest(*length*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.shake.hexdigest "Link to this definition")
:   Like [`digest()`](https://docs.python.org/3/library/hashlib.html#hashlib.shake.digest "hashlib.shake.digest") except the digest is returned as a string object of
    double length, containing only hexadecimal digits. This may be used to
    exchange the value in email or other non-binary environments.

Example use:

```
>>> h = hashlib.shake_256(b'Nobody inspects the spammish repetition')
>>> h.hexdigest(20)
'44709d6fcb83d92a76dcb0b668c98e1b1d3dafe7'
```