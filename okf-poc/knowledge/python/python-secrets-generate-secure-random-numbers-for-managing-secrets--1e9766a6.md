---
id: python-secrets-generate-secure-random-numbers-for-managing-secrets--1e9766a6
type: concept
title: '`secrets` — Generate secure random numbers for managing secrets[¶](https://docs.'
description: Added in version 3.6.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/secrets.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `secrets` — Generate secure random numbers for managing secrets[¶](https://docs.python.org/3/library/secrets.html#module-secrets "Link to this heading")

Added in version 3.6.

**Source code:** [Lib/secrets.py](https://github.com/python/cpython/tree/3.14/Lib/secrets.py)

---

The `secrets` module is used for generating cryptographically strong
random numbers suitable for managing data such as passwords, account
authentication, security tokens, and related secrets.

In particular, `secrets` should be used in preference to the
default pseudo-random number generator in the [`random`](https://docs.python.org/3/library/random.html#module-random "random: Generate pseudo-random numbers with various common distributions.") module, which
is designed for modelling and simulation, not security or cryptography.

See also

[**PEP 506**](https://peps.python.org/pep-0506/)