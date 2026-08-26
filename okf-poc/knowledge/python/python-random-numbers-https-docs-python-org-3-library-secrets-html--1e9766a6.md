---
id: python-random-numbers-https-docs-python-org-3-library-secrets-html--1e9766a6
type: concept
title: Random numbers[¶](https://docs.python.org/3/library/secrets.html#random-numbers
  "Link to this heading")
description: The `secrets` module provides access to the most secure source of
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/secrets.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Random numbers[¶](https://docs.python.org/3/library/secrets.html#random-numbers "Link to this heading")

The `secrets` module provides access to the most secure source of
randomness that your operating system provides.

*class* secrets.SystemRandom[¶](https://docs.python.org/3/library/secrets.html#secrets.SystemRandom "Link to this definition")
:   A class for generating random numbers using the highest-quality
    sources provided by the operating system. See
    [`random.SystemRandom`](https://docs.python.org/3/library/random.html#random.SystemRandom "random.SystemRandom") for additional details.

secrets.choice(*seq*)[¶](https://docs.python.org/3/library/secrets.html#secrets.choice "Link to this definition")
:   Return a randomly chosen element from a non-empty sequence.

secrets.randbelow(*exclusive\_upper\_bound*)[¶](https://docs.python.org/3/library/secrets.html#secrets.randbelow "Link to this definition")
:   Return a random int in the range [0, *exclusive\_upper\_bound*).

secrets.randbits(*k*)[¶](https://docs.python.org/3/library/secrets.html#secrets.randbits "Link to this definition")
:   Return a non-negative int with *k* random bits.