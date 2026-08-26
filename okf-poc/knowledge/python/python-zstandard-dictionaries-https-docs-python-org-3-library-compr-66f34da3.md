---
id: python-zstandard-dictionaries-https-docs-python-org-3-library-compr-66f34da3
type: concept
title: Zstandard dictionaries[¶](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries
  "Link to this heading")
description: compression.zstd.train\_dict(*samples*, *dict\_size*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/compression.zstd.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Zstandard dictionaries[¶](https://docs.python.org/3/library/compression.zstd.html#zstandard-dictionaries "Link to this heading")

compression.zstd.train\_dict(*samples*, *dict\_size*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "Link to this definition")
:   Train a Zstandard dictionary, returning a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict") instance.
    Zstandard dictionaries enable more efficient compression of smaller sizes
    of data, which is traditionally difficult to compress due to less
    repetition. If you are compressing multiple similar groups of data (such as
    similar files), Zstandard dictionaries can improve compression ratios and
    speed significantly.

    The *samples* argument (an iterable of [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects), is the
    population of samples used to train the Zstandard dictionary.

    The *dict\_size* argument, an integer, is the maximum size (in bytes) the
    Zstandard dictionary should be. The Zstandard documentation suggests an
    absolute maximum of no more than 100 KB, but the maximum can often be smaller
    depending on the data. Larger dictionaries generally slow down compression,
    but improve compression ratios. Smaller dictionaries lead to faster
    compression, but reduce the compression ratio.

compression.zstd.finalize\_dict(*zstd\_dict*, */*, *samples*, *dict\_size*, *level*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.finalize_dict "Link to this definition")
:   An advanced function for converting a “raw content” Zstandard dictionary into
    a regular Zstandard dictionary. “Raw content” dictionaries are a sequence of
    bytes that do not need to follow the structure of a normal Zstandard
    dictionary.

    The *zstd\_dict* argument is a [`ZstdDict`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "compression.zstd.ZstdDict") instance with
    the [`dict_content`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict.dict_content "compression.zstd.ZstdDict.dict_content") containing the raw dictionary contents.

    The *samples* argument (an iterable of [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes") objects), contains
    sample data for generating the Zstandard dictionary.

    The *dict\_size* argument, an integer, is the maximum size (in bytes) the
    Zstandard dictionary should be. See [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict") for
    suggestions on the maximum dictionary size.

    The *level* argument (an integer) is the compression level expected to be
    passed to the compressors using this dictionary. The dictionary information
    varies for each compression level, so tuning for the proper compression
    level can make compression more efficient.

*class* compression.zstd.ZstdDict(*dict\_content*, */*, *\**, *is\_raw=False*)[¶](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.ZstdDict "Link to this definition")
:   A wrapper around Zstandard dictionaries. Dictionaries can be used to improve
    the compression of many small chunks of data. Use [`train_dict()`](https://docs.python.org/3/library/compression.zstd.html#compression.zstd.train_dict "compression.zstd.train_dict") if you
    need to train a new dictionary from sample data.

    The *dict\_content* argument (a [bytes-like object](https://docs.python.org/3/glossary.html#term-bytes-like-object)), is the already
    trained dictionary information.

    The *is\_raw* argument, a boolean, is an advanced parameter controlling the
    meaning of *dict\_content*. `True` means *dict\_content* is a “raw content”
    dictionary, without any format restrictions. `False` means *dict\_content*
    is