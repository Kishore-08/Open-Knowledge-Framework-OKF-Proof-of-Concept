---
id: python-notes-on-reproducibility-https-docs-python-org-3-library-ran-0f728645
type: concept
title: Notes on Reproducibility[¶](https://docs.python.org/3/library/random.html#notes-on-reproducibility
  "Link to this heading")
description: Sometimes it is useful to be able to reproduce the sequences given by
  a
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/random.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Notes on Reproducibility[¶](https://docs.python.org/3/library/random.html#notes-on-reproducibility "Link to this heading")

Sometimes it is useful to be able to reproduce the sequences given by a
pseudo-random number generator. By reusing a seed value, the same sequence should be
reproducible from run to run as long as multiple threads are not running.

Most of the random module’s algorithms and seeding functions are subject to
change across Python versions, but two aspects are guaranteed not to change:

- If a new seeding method is added, then a backward compatible seeder will be
  offered.
- The generator’s [`random()`](https://docs.python.org/3/library/random.html#random.Random.random "random.Random.random") method will continue to produce the same
  sequence when the compatible seeder is given the same seed.