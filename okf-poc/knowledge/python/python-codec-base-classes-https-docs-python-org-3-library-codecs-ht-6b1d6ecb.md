---
id: python-codec-base-classes-https-docs-python-org-3-library-codecs-ht-6b1d6ecb
type: concept
title: Codec Base Classes[¶](https://docs.python.org/3/library/codecs.html#codec-base-classes
  "Link to this heading")
description: The `codecs` module defines a set of base classes which define the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Codec Base Classes[¶](https://docs.python.org/3/library/codecs.html#codec-base-classes "Link to this heading")

The `codecs` module defines a set of base classes which define the
interfaces for working with codec objects, and can also be used as the basis
for custom codec implementations.

Each codec has to define four interfaces to make it usable as codec in Python:
stateless encoder, stateless decoder, stream reader and stream writer. The
stream reader and writers typically reuse the stateless encoder/decoder to
implement the file protocols. Codec authors also need to define how the
codec will handle encoding and decoding errors.