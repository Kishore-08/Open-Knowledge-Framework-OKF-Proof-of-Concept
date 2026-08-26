---
id: python-hashlib-secure-hashes-and-message-digests-https-docs-python--4a693406
type: concept
title: '`hashlib` — Secure hashes and message digests[¶](https://docs.python.org/3/libra'
description: '**Source code:** [Lib/hashlib.py](https://github.com/python/cpython/tree/3.14/Lib/hashlib.py)'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `hashlib` — Secure hashes and message digests[¶](https://docs.python.org/3/library/hashlib.html#module-hashlib "Link to this heading")

**Source code:** [Lib/hashlib.py](https://github.com/python/cpython/tree/3.14/Lib/hashlib.py)

---

This module implements a common interface to many different hash algorithms.
Included are the FIPS secure hash algorithms SHA224, SHA256, SHA384, SHA512,
(defined in [the FIPS 180-4 standard](https://csrc.nist.gov/pubs/fips/180-4/upd1/final)), the SHA-3 series (defined in [the FIPS
202 standard](https://csrc.nist.gov/pubs/fips/202/final)) as well as the legacy algorithms SHA1 ([formerly part of FIPS](https://csrc.nist.gov/news/2023/decision-to-revise-fips-180-4))
and the MD5 algorithm (defined in internet [**RFC 1321**](https://datatracker.ietf.org/doc/html/rfc1321.html)).

Note

If you want the adler32 or crc32 hash functions, they are available in
the [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.") module.