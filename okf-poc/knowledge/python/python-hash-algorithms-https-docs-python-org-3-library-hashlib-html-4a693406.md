---
id: python-hash-algorithms-https-docs-python-org-3-library-hashlib-html-4a693406
type: concept
title: Hash algorithms[¶](https://docs.python.org/3/library/hashlib.html#hash-algorithms
  "Link to this heading")
description: There is one constructor method named for each type of *hash*. All return
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Hash algorithms[¶](https://docs.python.org/3/library/hashlib.html#hash-algorithms "Link to this heading")

There is one constructor method named for each type of *hash*. All return
a hash object with the same simple interface. For example: use [`sha256()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "hashlib.sha256")
to create a SHA-256 hash object. You can now feed this object with
[bytes-like objects](https://docs.python.org/3/glossary.html#term-bytes-like-object) (normally [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")) using
the [`update`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.update "hashlib.hash.update") method. At any point you can ask it for the
*digest* of the concatenation of the data fed to it so far using the
[`digest()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.digest "hashlib.hash.digest") or [`hexdigest()`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest "hashlib.hash.hexdigest") methods.

To allow multithreading, the Python [GIL](https://docs.python.org/3/glossary.html#term-GIL) is released while computing a
hash supplied more than 2047 bytes of data at once in its constructor or
[`.update`](https://docs.python.org/3/library/hashlib.html#hashlib.hash.update "hashlib.hash.update") method.

Constructors for hash algorithms that are always present in this module are
[`sha1()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha1 "hashlib.sha1"), [`sha224()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha224 "hashlib.sha224"), [`sha256()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha256 "hashlib.sha256"), [`sha384()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha384 "hashlib.sha384"), [`sha512()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha512 "hashlib.sha512"),
[`sha3_224()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha3_224 "hashlib.sha3_224"), [`sha3_256()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha3_256 "hashlib.sha3_256"), [`sha3_384()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha3_384 "hashlib.sha3_384"), [`sha3_512()`](https://docs.python.org/3/library/hashlib.html#hashlib.sha3_512 "hashlib.sha3_512"),
[`shake_128()`](https://docs.python.org/3/library/hashlib.html#hashlib.shake_128 "hashlib.shake_128"), [`shake_256()`](https://docs.python.org/3/library/hashlib.html#hashlib.shake_256 "hashlib.shake_256"), [`blake2b()`](https://docs.python.org/3/library/hashlib.html#hashlib.blake2b "hashlib.blake2b"), and [`blake2s()`](https://docs.python.org/3/library/hashlib.html#hashlib.blake2s "hashlib.blake2s").
[`md5()`](https://docs.python.org/3/library/hashlib.html#hashlib.md5 "hashlib.md5") is normally available as well, though it may be missing or blocked
if you are using a rare “FIPS compliant” build of Python.
These correspond to [`algorithms_guaranteed`](https://docs.python.org/3/library/hashlib.html#hashlib.algorithms_guaranteed "hashlib.algorithms_guaranteed").

Additional algorithms may also be available if your Python distribution’s
`hashlib` was linked against a build of OpenSSL that provides others.
Others *are not guaranteed available* on all installations and will only be
accessible by name via [`new()`](https://docs.python.org/3/library/hashlib.html#hashlib.new "hashlib.new"). See [`algorithms_available`](https://docs.python.org/3/library/hashlib.html#hashlib.algorithms_available "hashlib.algorithms_available").

Warning

Some algorithms have known hash collision weaknesses (including MD5 and
SHA1). Refer to [Attacks on cryptographic hash algorithms](https://en.wikipedia.org/wiki/Cryptographic_hash_function#Attacks_on_cryptographic_hash_algorithms) and the
[hashlib-seealso](https://docs.python.org/3/library/hashlib.html#hashlib-seealso) section at the end of this document.

Added in version 3.6: SHA3 (Keccak) and SHAKE constructors [`sha3_224()`](https://docs.python.org/3/library/hashlib.html