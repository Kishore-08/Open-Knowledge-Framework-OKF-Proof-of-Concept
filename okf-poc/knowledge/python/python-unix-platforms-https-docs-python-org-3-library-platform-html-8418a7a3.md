---
id: python-unix-platforms-https-docs-python-org-3-library-platform-html-8418a7a3
type: concept
title: Unix platforms[¶](https://docs.python.org/3/library/platform.html#unix-platforms
  "Link to this heading")
description: platform.libc\_ver(*executable=sys.executable*, *lib=''*, *version=''*,
  *chunksize=16384*)[¶](https://docs.python.org/3/library/platform.html#platform.libc_ver
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/platform.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Unix platforms[¶](https://docs.python.org/3/library/platform.html#unix-platforms "Link to this heading")

platform.libc\_ver(*executable=sys.executable*, *lib=''*, *version=''*, *chunksize=16384*)[¶](https://docs.python.org/3/library/platform.html#platform.libc_ver "Link to this definition")
:   Tries to determine the libc version against which the file executable (defaults
    to the Python interpreter) is linked. Returns a tuple of strings `(lib,
    version)` which default to the given parameters in case the lookup fails.

    Note that this function has intimate knowledge of how different libc versions
    add symbols to the executable is probably only usable for executables compiled
    using **gcc**.

    The file is read and scanned in chunks of *chunksize* bytes.