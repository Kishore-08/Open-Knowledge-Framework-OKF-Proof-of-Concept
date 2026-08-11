---
id: python-incremental-encoding-and-decoding-https-docs-python-org-3-li-6b1d6ecb
type: concept
title: Incremental Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#incremental-encoding-and-decoding
  "Link to this heading")
description: The [`IncrementalEncoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder
  "codecs.IncrementalEncoder") and [`IncrementalDecoder`](https://docs.python.org/3/library/codecs.html
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Incremental Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#incremental-encoding-and-decoding "Link to this heading")

The [`IncrementalEncoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder "codecs.IncrementalEncoder") and [`IncrementalDecoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder "codecs.IncrementalDecoder") classes provide
the basic interface for incremental encoding and decoding. Encoding/decoding the
input isn’t done with one call to the stateless encoder/decoder function, but
with multiple calls to the
[`encode()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.encode "codecs.IncrementalEncoder.encode")/[`decode()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.decode "codecs.IncrementalDecoder.decode") method of
the incremental encoder/decoder. The incremental encoder/decoder keeps track of
the encoding/decoding process during method calls.

The joined output of calls to the
[`encode()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.encode "codecs.IncrementalEncoder.encode")/[`decode()`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalDecoder.decode "codecs.IncrementalDecoder.decode") method is
the same as if all the single inputs were joined into one, and this input was
encoded/decoded with the stateless encoder/decoder.

#### IncrementalEncoder Objects[¶](https://docs.python.org/3/library/codecs.html#incrementalencoder-objects "Link to this heading")

The [`IncrementalEncoder`](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder "codecs.IncrementalEncoder") class is used for encoding an input in multiple
steps. It defines the following methods which every incremental encoder must
define in order to be compatible with the Python codec registry.

*class* codecs.IncrementalEncoder(*errors='strict'*)[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder "Link to this definition")
:   Constructor for an `IncrementalEncoder` instance.

    All incremental encoders must provide this constructor interface. They are free
    to add additional keyword arguments, but only the ones defined here are used by
    the Python codec registry.

    The `IncrementalEncoder` may implement different error handling schemes
    by providing the *errors* keyword argument. See [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers) for
    possible values.

    The *errors* argument will be assigned to an attribute of the same name.
    Assigning to this attribute makes it possible to switch between different error
    handling strategies during the lifetime of the `IncrementalEncoder`
    object.

    encode(*object*, *final=False*)[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.encode "Link to this definition")
    :   Encodes *object* (taking the current state of the encoder into account)
        and returns the resulting encoded object. If this is the last call to
        `encode()` *final* must be true (the default is false).

    reset()[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.reset "Link to this definition")
    :   Reset the encoder to the initial state. The output is discarded: call
        `.encode(object, final=True)`, passing an empty byte or text string
        if necessary, to reset the encoder and to get the output.

    getstate()[¶](https://docs.python.org/3/library/codecs.html#codecs.IncrementalEncoder.getstate "Link to this definition")
    :   Return the current state of the encoder which must be an integer. The
        implementation should make sure that `0` is the most common
        state. (States that are more complicated than integers can be converted
        into an integer by marshaling/pickling the state and encoding the bytes
        of the resulting string into an integer.)

    setstate(*state*)[¶](https://d