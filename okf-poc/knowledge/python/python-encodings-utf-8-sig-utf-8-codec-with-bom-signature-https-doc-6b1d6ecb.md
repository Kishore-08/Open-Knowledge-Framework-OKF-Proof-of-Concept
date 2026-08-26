---
id: python-encodings-utf-8-sig-utf-8-codec-with-bom-signature-https-doc-6b1d6ecb
type: concept
title: '`encodings.utf_8_sig` — UTF-8 codec with BOM signature[¶](https://docs.python.org/3/library/codecs.html#module-encodings.utf_8_sig
  "Link to this heading")'
description: This module implements a variant of the UTF-8 codec. On encoding, a UTF-8
  encoded
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## `encodings.utf_8_sig` — UTF-8 codec with BOM signature[¶](https://docs.python.org/3/library/codecs.html#module-encodings.utf_8_sig "Link to this heading")

This module implements a variant of the UTF-8 codec. On encoding, a UTF-8 encoded
BOM will be prepended to the UTF-8 encoded bytes. For the stateful encoder this
is only done once (on the first write to the byte stream). On decoding, an
optional UTF-8 encoded BOM at the start of the data will be skipped.