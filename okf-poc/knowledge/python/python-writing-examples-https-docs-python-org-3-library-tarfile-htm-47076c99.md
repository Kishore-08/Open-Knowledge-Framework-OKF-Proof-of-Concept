---
id: python-writing-examples-https-docs-python-org-3-library-tarfile-htm-47076c99
type: concept
title: Writing examples[¶](https://docs.python.org/3/library/tarfile.html#writing-examples
  "Link to this heading")
description: 'How to create an uncompressed tar archive from a list of filenames:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/tarfile.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Writing examples[¶](https://docs.python.org/3/library/tarfile.html#writing-examples "Link to this heading")

How to create an uncompressed tar archive from a list of filenames:

```
import tarfile
tar = tarfile.open("sample.tar", "w")
for name in ["foo", "bar", "quux"]:
    tar.add(name)
tar.close()
```

The same example using the [`with`](https://docs.python.org/3/reference/compound_stmts.html#with) statement:

```
import tarfile
with tarfile.open("sample.tar", "w") as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)
```

How to create and write an archive to stdout using
[`sys.stdout.buffer`](https://docs.python.org/3/library/sys.html#sys.stdout "sys.stdout") in the *fileobj* parameter
in [`TarFile.add()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "tarfile.TarFile.add"):

```
import sys
import tarfile
with tarfile.open("sample.tar.gz", "w|gz", fileobj=sys.stdout.buffer) as tar:
    for name in ["foo", "bar", "quux"]:
        tar.add(name)
```

How to create an archive and reset the user information using the *filter*
parameter in [`TarFile.add()`](https://docs.python.org/3/library/tarfile.html#tarfile.TarFile.add "tarfile.TarFile.add"):

```
import tarfile
def reset(tarinfo):
    tarinfo.uid = tarinfo.gid = 0
    tarinfo.uname = tarinfo.gname = "root"
    return tarinfo
tar = tarfile.open("sample.tar.gz", "w:gz")
tar.add("foo", filter=reset)
tar.close()
```