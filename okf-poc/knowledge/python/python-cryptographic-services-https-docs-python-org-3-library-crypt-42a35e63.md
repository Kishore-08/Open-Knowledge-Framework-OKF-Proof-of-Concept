---
id: python-cryptographic-services-https-docs-python-org-3-library-crypt-42a35e63
type: concept
title: Cryptographic Services[¶](https://docs.python.org/3/library/crypto.html#cryptogr
description: The modules described in this chapter implement various algorithms of
  a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/crypto.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# Cryptographic Services[¶](https://docs.python.org/3/library/crypto.html#cryptographic-services "Link to this heading")

The modules described in this chapter implement various algorithms of a
cryptographic nature. They are available at the discretion of the installation.
Here’s an overview:

- [`hashlib` — Secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)
  - [Hash algorithms](https://docs.python.org/3/library/hashlib.html#hash-algorithms)
  - [Usage](https://docs.python.org/3/library/hashlib.html#usage)
  - [Constructors](https://docs.python.org/3/library/hashlib.html#constructors)
  - [Attributes](https://docs.python.org/3/library/hashlib.html#attributes)
  - [Hash Objects](https://docs.python.org/3/library/hashlib.html#hash-objects)
  - [SHAKE variable length digests](https://docs.python.org/3/library/hashlib.html#shake-variable-length-digests)
  - [File hashing](https://docs.python.org/3/library/hashlib.html#file-hashing)
  - [Key derivation](https://docs.python.org/3/library/hashlib.html#key-derivation)
  - [BLAKE2](https://docs.python.org/3/library/hashlib.html#blake2)
    - [Creating hash objects](https://docs.python.org/3/library/hashlib.html#creating-hash-objects)
    - [Constants](https://docs.python.org/3/library/hashlib.html#constants)
    - [Examples](https://docs.python.org/3/library/hashlib.html#examples)
      - [Simple hashing](https://docs.python.org/3/library/hashlib.html#simple-hashing)
      - [Using different digest sizes](https://docs.python.org/3/library/hashlib.html#using-different-digest-sizes)
      - [Keyed hashing](https://docs.python.org/3/library/hashlib.html#keyed-hashing)
      - [Randomized hashing](https://docs.python.org/3/library/hashlib.html#randomized-hashing)
      - [Personalization](https://docs.python.org/3/library/hashlib.html#personalization)
      - [Tree mode](https://docs.python.org/3/library/hashlib.html#tree-mode)
    - [Credits](https://docs.python.org/3/library/hashlib.html#credits)
- [`hmac` — Keyed-Hashing for Message Authentication](https://docs.python.org/3/library/hmac.html)
- [`secrets` — Generate secure random numbers for managing secrets](https://docs.python.org/3/library/secrets.html)
  - [Random numbers](https://docs.python.org/3/library/secrets.html#random-numbers)
  - [Generating tokens](https://docs.python.org/3/library/secrets.html#generating-tokens)
    - [How many bytes should tokens use?](https://docs.python.org/3/library/secrets.html#how-many-bytes-should-tokens-use)
  - [Other functions](https://docs.python.org/3/library/secrets.html#other-functions)
  - [Recipes and best practices](https://docs.python.org/3/library/secrets.html#recipes-and-best-practices)