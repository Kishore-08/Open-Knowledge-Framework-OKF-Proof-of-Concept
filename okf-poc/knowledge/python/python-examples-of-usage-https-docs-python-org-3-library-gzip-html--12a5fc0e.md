---
id: python-examples-of-usage-https-docs-python-org-3-library-gzip-html--12a5fc0e
type: concept
title: Examples of usage[¶](https://docs.python.org/3/library/gzip.html#examples-of-usage
  "Link to this heading")
description: 'Example of how to read a compressed file:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/gzip.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Examples of usage[¶](https://docs.python.org/3/library/gzip.html#examples-of-usage "Link to this heading")

Example of how to read a compressed file:

```
import gzip
with gzip.open('/home/joe/file.txt.gz', 'rb') as f:
    file_content = f.read()
```

Example of how to create a compressed GZIP file:

```
import gzip
content = b"Lots of content here"
with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
    f.write(content)
```

Example of how to GZIP compress an existing file:

```
import gzip
import shutil
with open('/home/joe/file.txt', 'rb') as f_in:
    with gzip.open('/home/joe/file.txt.gz', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)
```

Example of how to GZIP compress a binary string:

```
import gzip
s_in = b"Lots of content here"
s_out = gzip.compress(s_in)
```

See also

Module [`zlib`](https://docs.python.org/3/library/zlib.html#module-zlib "zlib: Low-level interface to compression and decompression routines compatible with gzip.")
:   The basic data compression module needed to support the **gzip** file
    format.

In case gzip (de)compression is a bottleneck, the [python-isal](https://github.com/pycompression/python-isal)
package speeds up (de)compression with a mostly compatible API.