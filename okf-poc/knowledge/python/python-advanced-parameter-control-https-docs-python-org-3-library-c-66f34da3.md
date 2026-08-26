---
id: python-advanced-parameter-control-https-docs-python-org-3-library-c-66f34da3
type: concept
title: Advanced parameter control[¶](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control
  "Link to this heading")
description: '*class* compression.zstd.CompressionParameter[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/compression.zstd.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Advanced parameter control[¶](https://docs.python.org/3/library/compression.zstd.html#advanced-parameter-control "Link to this heading")

*class* compression.zstd.CompressionParameter[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter "Link to this definition")
:   An [`IntEnum`](https://docs.python.org/3/library/enum.html#enum.IntEnum "enum.IntEnum") containing the advanced compression parameter
    keys that can be used when compressing data.

    The [`bounds()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "compression.zstd.CompressionParameter.bounds") method can be used on any attribute to get the valid
    values for that parameter.

    Parameters are optional; any omitted parameter will have its value selected
    automatically.

    Example getting the lower and upper bound of [`compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level"):

    ```
    lower, upper = CompressionParameter.compression_level.bounds()
    ```

    Example setting the [`window_log`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.window_log "compression.zstd.CompressionParameter.window_log") to the maximum size:

    ```
    _lower, upper = CompressionParameter.window_log.bounds()
    options = {CompressionParameter.window_log: upper}
    compress(b'venezuelan beaver cheese', options=options)
    ```

    bounds()[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.bounds "Link to this definition")
    :   Return the tuple of int bounds, `(lower, upper)`, of a compression
        parameter. This method should be called on the attribute you wish to
        retrieve the bounds of. For example, to get the valid values for
        [`compression_level`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "compression.zstd.CompressionParameter.compression_level"), one may check the result of
        `CompressionParameter.compression_level.bounds()`.

        Both the lower and upper bounds are inclusive.

    compression\_level[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.compression_level "Link to this definition")
    :   A high-level means of setting other compression parameters that affect
        the speed and ratio of compressing data.

        Regular compression levels are greater than `0`. Values greater than
        `20` are considered “ultra” compression and require more memory than
        other levels. Negative values can be used to trade off faster compression
        for worse compression ratios.

        Setting the level to zero uses [`COMPRESSION_LEVEL_DEFAULT`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.COMPRESSION_LEVEL_DEFAULT "compression.zstd.COMPRESSION_LEVEL_DEFAULT").

    window\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.window_log "Link to this definition")
    :   Maximum allowed back-reference distance the compressor can use when
        compressing data, expressed as power of two, `1 << window_log` bytes.
        This parameter greatly influences the memory usage of compression. Higher
        values require more memory but gain better compression values.

        A value of zero causes the value to be selected automatically.

    hash\_log[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.CompressionParameter.hash_log "Link to this definition")
    :   Size of the initial probe table, as a power of two. The resulting memory
        usage is `1 << (hash_log+2)` bytes. Larger tables improve compression
        ratio of strategies <= [`dfast`](https://docs.python.org/3/libr