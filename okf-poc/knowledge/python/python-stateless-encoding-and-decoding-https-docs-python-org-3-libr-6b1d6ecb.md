---
id: python-stateless-encoding-and-decoding-https-docs-python-org-3-libr-6b1d6ecb
type: concept
title: Stateless Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#stateless-encoding-and-decoding
  "Link to this heading")
description: The base [`Codec`](https://docs.python.org/3/library/codecs.html#codecs.Codec
  "codecs.Codec") class defines these methods which also define the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Stateless Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#stateless-encoding-and-decoding "Link to this heading")

The base [`Codec`](https://docs.python.org/3/library/codecs.html#codecs.Codec "codecs.Codec") class defines these methods which also define the
function interfaces of the stateless encoder and decoder:

*class* codecs.Codec[¶](https://docs.python.org/3/library/codecs.html#codecs.Codec "Link to this definition")
:   encode(*input*, *errors='strict'*)[¶](https://docs.python.org/3/library/codecs.html#codecs.Codec.encode "Link to this definition")
    :   Encodes the object *input* and returns a tuple (output object, length consumed).
        For instance, [text encoding](https://docs.python.org/3/glossary.html#term-text-encoding) converts
        a string object to a bytes object using a particular
        character set encoding (e.g., `cp1252` or `iso-8859-1`).

        The *errors* argument defines the error handling to apply.
        It defaults to `'strict'` handling.

        The method may not store state in the `Codec` instance. Use
        [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") for codecs which have to keep state in order to make
        encoding efficient.

        The encoder must be able to handle zero length input and return an empty object
        of the output object type in this situation.

    decode(*input*, *errors='strict'*)[¶](https://docs.python.org/3/library/codecs.html#codecs.Codec.decode "Link to this definition")
    :   Decodes the object *input* and returns a tuple (output object, length
        consumed). For instance, for a [text encoding](https://docs.python.org/3/glossary.html#term-text-encoding), decoding converts
        a bytes object encoded using a particular
        character set encoding to a string object.

        For text encodings and bytes-to-bytes codecs,
        *input* must be a bytes object or one which provides the read-only
        buffer interface – for example, buffer objects and memory mapped files.

        The *errors* argument defines the error handling to apply.
        It defaults to `'strict'` handling.

        The method may not store state in the `Codec` instance. Use
        [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") for codecs which have to keep state in order to make
        decoding efficient.

        The decoder must be able to handle zero length input and return an empty object
        of the output object type in this situation.