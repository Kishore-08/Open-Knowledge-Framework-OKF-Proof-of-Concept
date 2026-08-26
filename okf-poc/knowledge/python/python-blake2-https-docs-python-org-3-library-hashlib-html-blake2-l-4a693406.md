---
id: python-blake2-https-docs-python-org-3-library-hashlib-html-blake2-l-4a693406
type: concept
title: BLAKE2[¶](https://docs.python.org/3/library/hashlib.html#blake2 "Link to this
  heading")
description: '[BLAKE2](https://www.blake2.net) is a cryptographic hash function defined
  in [**RFC 7693**](https://datatracker.ietf.org/doc/html/rfc7693.html) that comes
  in two'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/hashlib.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## BLAKE2[¶](https://docs.python.org/3/library/hashlib.html#blake2 "Link to this heading")

[BLAKE2](https://www.blake2.net) is a cryptographic hash function defined in [**RFC 7693**](https://datatracker.ietf.org/doc/html/rfc7693.html) that comes in two
flavors:

- **BLAKE2b**, optimized for 64-bit platforms and produces digests of any size
  between 1 and 64 bytes,
- **BLAKE2s**, optimized for 8- to 32-bit platforms and produces digests of any
  size between 1 and 32 bytes.

BLAKE2 supports **keyed mode** (a faster and simpler replacement for [HMAC](https://en.wikipedia.org/wiki/Hash-based_message_authentication_code)),
**salted hashing**, **personalization**, and **tree hashing**.

Hash objects from this module follow the API of standard library’s
`hashlib` objects.