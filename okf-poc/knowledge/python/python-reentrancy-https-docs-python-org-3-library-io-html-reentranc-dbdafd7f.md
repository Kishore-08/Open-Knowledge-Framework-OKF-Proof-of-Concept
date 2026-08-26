---
id: python-reentrancy-https-docs-python-org-3-library-io-html-reentranc-dbdafd7f
type: concept
title: Reentrancy[¶](https://docs.python.org/3/library/io.html#reentrancy "Link to
  this heading")
description: Binary buffered objects (instances of [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader
  "io.BufferedReader"),
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/io.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Reentrancy[¶](https://docs.python.org/3/library/io.html#reentrancy "Link to this heading")

Binary buffered objects (instances of [`BufferedReader`](https://docs.python.org/3/library/io.html#io.BufferedReader "io.BufferedReader"),
[`BufferedWriter`](https://docs.python.org/3/library/io.html#io.BufferedWriter "io.BufferedWriter"), [`BufferedRandom`](https://docs.python.org/3/library/io.html#io.BufferedRandom "io.BufferedRandom") and [`BufferedRWPair`](https://docs.python.org/3/library/io.html#io.BufferedRWPair "io.BufferedRWPair"))
are not reentrant. While reentrant calls will not happen in normal situations,
they can arise from doing I/O in a [`signal`](https://docs.python.org/3/library/signal.html#module-signal "signal: Set handlers for asynchronous events.") handler. If a thread tries to
re-enter a buffered object which it is already accessing, a [`RuntimeError`](https://docs.python.org/3/library/exceptions.html#RuntimeError "RuntimeError")
is raised. Note this doesn’t prohibit a different thread from entering the
buffered object.

The above implicitly extends to text files, since the [`open()`](https://docs.python.org/3/library/functions.html#open "open") function
will wrap a buffered object inside a [`TextIOWrapper`](https://docs.python.org/3/library/io.html#io.TextIOWrapper "io.TextIOWrapper"). This includes
standard streams and therefore affects the built-in [`print()`](https://docs.python.org/3/library/functions.html#print "print") function as
well.