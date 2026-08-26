---
id: python-miscellaneous-https-docs-python-org-3-library-compression-zs-66f34da3
type: concept
title: Miscellaneous[¶](https://docs.python.org/3/library/compression.zstd.html#miscellaneous
  "Link to this heading")
description: compression.zstd.get\_frame\_info(*frame\_buffer*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.get_frame_info
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/compression.zstd.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Miscellaneous[¶](https://docs.python.org/3/library/compression.zstd.html#miscellaneous "Link to this heading")

compression.zstd.get\_frame\_info(*frame\_buffer*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.get_frame_info "Link to this definition")
:   Retrieve a [`FrameInfo`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo "compression.zstd.FrameInfo") object containing metadata about a Zstandard
    frame. Frames contain metadata related to the compressed data they hold.

*class* compression.zstd.FrameInfo[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo "Link to this definition")
:   Metadata related to a Zstandard frame.

    decompressed\_size[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo.decompressed_size "Link to this definition")
    :   The size of the decompressed contents of the frame.

    dictionary\_id[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.FrameInfo.dictionary_id "Link to this definition")
    :   An integer representing the Zstandard dictionary ID needed for
        decompressing the frame. `0` means the dictionary ID was not
        recorded in the frame header. This may mean that a Zstandard dictionary
        is not needed, or that the ID of a required dictionary was not recorded.

compression.zstd.COMPRESSION\_LEVEL\_DEFAULT[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.COMPRESSION_LEVEL_DEFAULT "Link to this definition")
:   The default compression level for Zstandard: `3`.

compression.zstd.zstd\_version\_info[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.zstd_version_info "Link to this definition")
:   Version number of the runtime zstd library as a tuple of integers
    (major, minor, release).