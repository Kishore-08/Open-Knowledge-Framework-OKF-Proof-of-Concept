---
id: python-hash-objects-https-docs-python-org-3-library-hashlib-html-ha-4a693406
type: concept
title: Hash Objects[¶](https://docs.python.org/3/library/hashlib.html#hash-objects
  "Link to this heading")
description: The following values are provided as constant attributes of the hash
  objects
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Hash Objects[¶](https://docs.python.org/3/library/hashlib.html#hash-objects "Link to this heading")

The following values are provided as constant attributes of the hash objects
returned by the constructors:

hash.digest\_size[¶](https://docs.python.org/3/library/hashlib.html#hashlib.hash.digest_size "Link to this definition")
:   The size of the resulting hash in bytes.

hash.block\_size[¶](https://docs.python.org/3/library/hashlib.html#hashlib.hash.block_size "Link to this definition")
:   The internal block size of the hash algorithm in bytes.

A hash object has the following attributes:

hash.name[¶](https://docs.python.org/3/library/hashlib.html#hashlib.hash.name "Link to this definition")
:   The canonical name of this hash, always lowercase and always suitable as a
    parameter to [`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new") to create another hash of this type.

    Changed in version 3.4: The name attribute has been present in CPython since its inception, but
    until Python 3.4 was not formally specified, so may not exist on some
    platforms.

A hash object has the following methods:

hash.update(*data*)[¶](https://docs.python.org/3/library/hashlib.html#hashlib.hash.update "Link to this definition")
:   Update the hash object with the [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object).
    Repeated calls are equivalent to a single call with the
    concatenation of all the arguments: `m.update(a); m.update(b)` is
    equivalent to `m.update(a+b)`.

hash.digest()[¶](https://docs.python.org/3/library/hashlib.html#hashlib.hash.digest "Link to this definition")
:   Return the digest of the data passed to the [`update()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.update "hashlib.hash.update") method so far.
    This is a bytes object of size [`digest_size`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.digest_size "hashlib.hash.digest_size") which may contain bytes in
    the whole range from 0 to 255.

hash.hexdigest()[¶](https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest "Link to this definition")
:   Like [`digest()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.digest "hashlib.hash.digest") except the digest is returned as a string object of
    double length, containing only hexadecimal digits. This may be used to
    exchange the value safely in email or other non-binary environments.

hash.copy()[¶](https://docs.python.org/3/library/hashlib.html#hashlib.hash.copy "Link to this definition")
:   Return a copy (“clone”) of the hash object. This can be used to efficiently
    compute the digests of data sharing a common initial substring.