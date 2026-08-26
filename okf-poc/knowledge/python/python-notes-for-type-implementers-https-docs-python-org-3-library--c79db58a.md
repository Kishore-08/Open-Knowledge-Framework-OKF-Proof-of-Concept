---
id: python-notes-for-type-implementers-https-docs-python-org-3-library--c79db58a
type: concept
title: Notes for type implementers[¶](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers
  "Link to this heading")
description: Implementers should be careful to make equal numbers equal and hash
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/numbers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Notes for type implementers[¶](https://docs.python.org/3/library/numbers.html#notes-for-type-implementers "Link to this heading")

Implementers should be careful to make equal numbers equal and hash
them to the same values. This may be subtle if there are two different
extensions of the real numbers. See also [Hashing of numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-hash).