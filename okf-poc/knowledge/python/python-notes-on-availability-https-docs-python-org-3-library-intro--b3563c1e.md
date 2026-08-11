---
id: python-notes-on-availability-https-docs-python-org-3-library-intro--b3563c1e
type: concept
title: Notes on availability[¶](https://docs.python.org/3/library/intro.html#notes-on-availability
  "Link to this heading")
description: '- An “Availability: Unix” note means that this function is commonly
  found on'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/intro.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Notes on availability[¶](https://docs.python.org/3/library/intro.html#notes-on-availability "Link to this heading")

- An “Availability: Unix” note means that this function is commonly found on
  Unix systems. It does not make any claims about its existence on a specific
  operating system.
- If not separately noted, all functions that claim “Availability: Unix” are
  supported on macOS, iOS and Android, all of which build on a Unix core.
- If an availability note contains both a minimum Kernel version and a minimum
  libc version, then both conditions must hold. For example a feature with note
  *Availability: Linux >= 3.17 with glibc >= 2.27* requires both Linux 3.17 or
  newer and glibc 2.27 or newer.