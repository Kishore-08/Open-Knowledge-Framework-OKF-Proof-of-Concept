---
id: python-provider-api-https-docs-python-org-3-library-pickle-html-pro-f2bc33b8
type: concept
title: Provider API[¶](https://docs.python.org/3/library/pickle.html#provider-api
  "Link to this heading")
description: The large data objects to be pickled must implement a [`__reduce_ex__()`](https://docs.python.org/3/library/pickle.html#object.__reduce_ex__
  "object.__reduce_ex__")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/pickle.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Provider API[¶](https://docs.python.org/3/library/pickle.html#provider-api "Link to this heading")

The large data objects to be pickled must implement a [`__reduce_ex__()`](https://docs.python.org/3/library/pickle.html#object.__reduce_ex__ "object.__reduce_ex__")
method specialized for protocol 5 and higher, which returns a
[`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") instance (instead of e.g. a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object)
for any large data.

A [`PickleBuffer`](https://docs.python.org/3/library/pickle.html#pickle.PickleBuffer "pickle.PickleBuffer") object *signals* that the underlying buffer is
eligible for out-of-band data transfer. Those objects remain compatible
with normal usage of the `pickle` module. However, consumers can also
opt-in to tell `pickle` that they will handle those buffers by
themselves.