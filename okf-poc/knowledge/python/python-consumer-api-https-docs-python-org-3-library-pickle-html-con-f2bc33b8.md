---
id: python-consumer-api-https-docs-python-org-3-library-pickle-html-con-f2bc33b8
type: concept
title: Consumer API[¶](https://docs.python.org/3/library/pickle.html#consumer-api
  "Link to this heading")
description: A communications system can enable custom handling of the [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer
  "pickle.PickleBuffer")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Consumer API[¶](https://docs.python.org/3/library/pickle.html#consumer-api "Link to this heading")

A communications system can enable custom handling of the [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer")
objects generated when serializing an object graph.

On the sending side, it needs to pass a *buffer\_callback* argument to
[`Pickler`](https://docs.python.org/3/library/pickle.html#pickle.Pickler "pickle.Pickler") (or to the [`dump()`](https://docs.python.org/3/library/pickle.html#pickle.dump "pickle.dump") or [`dumps()`](https://docs.python.org/3/library/pickle.html#pickle.dumps "pickle.dumps") function), which
will be called with each [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") generated while pickling
the object graph. Buffers accumulated by the *buffer\_callback* will not
see their data copied into the pickle stream, only a cheap marker will be
inserted.

On the receiving side, it needs to pass a *buffers* argument to
[`Unpickler`](https://docs.python.org/3/library/pickle.html#pickle.Unpickler "pickle.Unpickler") (or to the [`load()`](https://docs.python.org/3/library/pickle.html#pickle.load "pickle.load") or [`loads()`](https://docs.python.org/3/library/pickle.html#pickle.loads "pickle.loads") function),
which is an iterable of the buffers which were passed to *buffer\_callback*.
That iterable should produce buffers in the same order as they were passed
to *buffer\_callback*. Those buffers will provide the data expected by the
reconstructors of the objects whose pickling produced the original
[`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") objects.

Between the sending side and the receiving side, the communications system
is free to implement its own transfer mechanism for out-of-band buffers.
Potential optimizations include the use of shared memory or datatype-dependent
compression.