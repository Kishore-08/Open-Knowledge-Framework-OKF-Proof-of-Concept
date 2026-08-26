---
id: python-compressing-and-decompressing-data-in-memory-https-docs-pyth-66f34da3
type: concept
title: Compressing and decompressing data in memory[¶](https://docs.python.org/3/library/compression.zstd.html#compressing-and-decompressing-data-in-memory
  "Link to this heading")
description: compression.zstd.compress(*data*, *level=None*, *options=None*, *zstd\_dict=None*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/compression.zstd.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Compressing and decompressing data in memory[¶](https://docs.python.org/3/library/compression.zstd.html#compressing-and-decompressing-data-in-memory "Link to this heading")

compression.zstd.compress(*data*, *level=None*, *options=None*, *zstd\_dict=None*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress "Link to this definition")
:   Compress *data* (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)), returning the compressed
    data as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.

    The *level* argument is an integer controlling the level of
    compression. *level* is an alternative to setting
    [`CompressionParameter.compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level") in *options*. Use
    [`bounds()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "compression.zstd.CompressionParameter.bounds") on
    `compression_level` to get the values that can
    be passed for *level*. If advanced compression options are needed, the
    *level* argument must be omitted and in the *options* dictionary the
    `CompressionParameter.compression_level` parameter should be set.

    The *options* argument is a Python dictionary containing advanced
    compression parameters. The valid keys and values for compression parameters
    are documented as part of the [`CompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "compression.zstd.CompressionParameter") documentation.

    The *zstd\_dict* argument is an instance of [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
    containing trained data to improve compression efficiency. The
    function [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict") can be used to generate a Zstandard dictionary.

compression.zstd.decompress(*data*, *zstd\_dict=None*, *options=None*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.decompress "Link to this definition")
:   Decompress *data* (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)), returning the uncompressed
    data as a [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") object.

    The *options* argument is a Python dictionary containing advanced
    decompression parameters. The valid keys and values for compression
    parameters are documented as part of the [`DecompressionParameter`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.DecompressionParameter "compression.zstd.DecompressionParameter")
    documentation.

    The *zstd\_dict* argument is an instance of [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict")
    containing trained data used during compression. This must be
    the same Zstandard dictionary used during compression.

    If *data* is the concatenation of multiple distinct compressed frames,
    decompress all of these frames, and return the concatenation of the results.

*class* compression.zstd.ZstdCompressor(*level=None*, *options=None*, *zstd\_dict=None*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdCompressor "Link to this definition")
:   Create a compressor object, which can be used to compress data
    incrementally.

    For a more convenient way of compressing a single chunk of data, see the
    module-level function [`compress()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.compress "compression.zstd.compress").

    The *level* argument is an integer