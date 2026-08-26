---
id: python-examples-https-docs-python-org-3-library-hashlib-html-exampl-4a693406
type: concept
title: Examples[¶](https://docs.python.org/3/library/hashlib.html#examples "Link to
  this heading")
description: To calculate hash of some data, you should first construct a hash object
  by
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Examples[¶](https://docs.python.org/3/library/hashlib.html#examples "Link to this heading")

#### Simple hashing[¶](https://docs.python.org/3/library/hashlib.html#simple-hashing "Link to this heading")

To calculate hash of some data, you should first construct a hash object by
calling the appropriate constructor function ([`blake2b()`](https://docs.python.org/3/library/hashlib.html#hashlib.blake2b "hashlib.blake2b") or
[`blake2s()`](https://docs.python.org/3/library/hashlib.html#hashlib.blake2s "hashlib.blake2s")), then update it with the data by calling [`update()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.update "hashlib.hash.update") on the
object, and, finally, get the digest out of the object by calling
[`digest()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.digest "hashlib.hash.digest") (or [`hexdigest()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest "hashlib.hash.hexdigest") for hex-encoded string).

```
>>> from hashlib import blake2b
>>> h = blake2b()
>>> h.update(b'Hello world')
>>> h.hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
```

As a shortcut, you can pass the first chunk of data to update directly to the
constructor as the positional argument:

```
>>> from hashlib import blake2b
>>> blake2b(b'Hello world').hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
```

You can call [`hash.update()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.update "hashlib.hash.update") as many times as you need to iteratively
update the hash:

```
>>> from hashlib import blake2b
>>> items = [b'Hello', b' ', b'world']
>>> h = blake2b()
>>> for item in items:
...     h.update(item)
...
>>> h.hexdigest()
'6ff843ba685842aa82031d3f53c48b66326df7639a63d128974c5c14f31a0f33343a8c65551134ed1ae0f2b0dd2bb495dc81039e3eeb0aa1bb0388bbeac29183'
```

#### Using different digest sizes[¶](https://docs.python.org/3/library/hashlib.html#using-different-digest-sizes "Link to this heading")

BLAKE2 has configurable size of digests up to 64 bytes for BLAKE2b and up to 32
bytes for BLAKE2s. For example, to replace SHA-1 with BLAKE2b without changing
the size of output, we can tell BLAKE2b to produce 20-byte digests:

```
>>> from hashlib import blake2b
>>> h = blake2b(digest_size=20)
>>> h.update(b'Replacing SHA1 with the more secure function')
>>> h.hexdigest()
'd24f26cf8de66472d58d4e1b1774b4c9158b1f4c'
>>> h.digest_size
20
>>> len(h.digest())
20
```

Hash objects with different digest sizes have completely different outputs
(shorter hashes are *not* prefixes of longer hashes); BLAKE2b and BLAKE2s
produce different outputs even if the output length is the same:

```
>>> from hashlib import blake2b, blake2s
>>> blake2b(digest_size=10).hexdigest()
'6fa1d8fcfd719046d762'
>>> blake2b(digest_size=11).hexdigest()
'eb6ec15daf9546254f0809'
>>> blake2s(digest_size=10).hexdigest()
'1bf21a98c78a1c376ae9'
>>> blake2s(digest_size=11).hexdigest()
'567004bf96e4a25773ebf4'
```

#### Keyed hashing[¶](https://docs.python.org/3/library/hashlib.html#keyed-hashing "Link to this heading")

Keyed hashing can be used for authentication as a faster and simpler
replacement for [Hash-based message authentication code](https://en.wikipedia.org/wiki/HMAC) (HMAC).
BLAKE2 can be securely used in prefix-MAC mode thanks to the
indifferentiability property inherited from BLAKE.

This example shows how to get a (hex-encoded) 128-bit authentication code for
message `b'message data'` with key `b'pseudorandom key'`:

```
>>> from hashlib import blake2b
>>> h = blake2b(key=b'pseudorandom key', digest_size=16)
>>> h.update(b'message data')
>>> h.hexdigest()
'3d363ff7401e02026f4a4687d4863ced'
```

As a practical example, a web application can symmetrically sign cookies sent
to users and later verify them to make sure they weren