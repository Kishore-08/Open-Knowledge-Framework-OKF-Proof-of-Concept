---
id: python-stream-encoding-and-decoding-https-docs-python-org-3-library-6b1d6ecb
type: concept
title: Stream Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#stream-encoding-and-decoding
  "Link to this heading")
description: The [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter
  "codecs.StreamWriter") and [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader
  "co
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Stream Encoding and Decoding[¶](https://docs.python.org/3/library/codecs.html#stream-encoding-and-decoding "Link to this heading")

The [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") and [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") classes provide generic
working interfaces which can be used to implement new encoding submodules very
easily. See `encodings.utf_8` for an example of how this is done.

#### StreamWriter Objects[¶](https://docs.python.org/3/library/codecs.html#streamwriter-objects "Link to this heading")

The [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") class is a subclass of [`Codec`](https://docs.python.org/3/library/codecs.html#codecs.Codec "codecs.Codec") and defines the
following methods which every stream writer must define in order to be
compatible with the Python codec registry.

*class* codecs.StreamWriter(*stream*, *errors='strict'*)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "Link to this definition")
:   Constructor for a `StreamWriter` instance.

    All stream writers must provide this constructor interface. They are free to add
    additional keyword arguments, but only the ones defined here are used by the
    Python codec registry.

    The *stream* argument must be a file-like object open for writing
    text or binary data, as appropriate for the specific codec.

    The `StreamWriter` may implement different error handling schemes by
    providing the *errors* keyword argument. See [Error Handlers](https://docs.python.org/3/library/codecs.html#error-handlers) for
    the standard error handlers the underlying stream codec may support.

    The *errors* argument will be assigned to an attribute of the same name.
    Assigning to this attribute makes it possible to switch between different error
    handling strategies during the lifetime of the `StreamWriter` object.

    write(*object*)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.write "Link to this definition")
    :   Writes the object’s contents encoded to the stream.

    writelines(*list*)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.writelines "Link to this definition")
    :   Writes the concatenated iterable of strings to the stream (possibly by reusing
        the [`write()`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.write "codecs.StreamWriter.write") method). Infinite or
        very large iterables are not supported. The standard bytes-to-bytes codecs
        do not support this method.

    reset()[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter.reset "Link to this definition")
    :   Resets the codec buffers used for keeping internal state.

        Calling this method should ensure that the data on the output is put into
        a clean state that allows appending of new fresh data without having to
        rescan the whole stream to recover state.

In addition to the above methods, the [`StreamWriter`](https://docs.python.org/3/library/codecs.html#codecs.StreamWriter "codecs.StreamWriter") must also inherit
all other methods and attributes from the underlying stream.

#### StreamReader Objects[¶](https://docs.python.org/3/library/codecs.html#streamreader-objects "Link to this heading")

The [`StreamReader`](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "codecs.StreamReader") class is a subclass of [`Codec`](https://docs.python.org/3/library/codecs.html#codecs.Codec "codecs.Codec") and defines the
following methods which every stream reader must define in order to be
compatible with the Python codec registry.

*class* codecs.StreamReader(*stream*, *errors='strict'*)[¶](https://docs.python.org/3/library/codecs.html#codecs.StreamReader "Link to this definition")
:   Constructor for a `StreamReader` instance.