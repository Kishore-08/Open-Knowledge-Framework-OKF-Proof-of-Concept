---
id: python-rmtree-example-https-docs-python-org-3-library-shutil-html-r-4dabd212
type: concept
title: rmtree example[¶](https://docs.python.org/3/library/shutil.html#rmtree-example
  "Link to this heading")
description: This example shows how to remove a directory tree on Windows where some
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shutil.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### rmtree example[¶](https://docs.python.org/3/library/shutil.html#rmtree-example "Link to this heading")

This example shows how to remove a directory tree on Windows where some
of the files have their read-only bit set. It uses the onexc callback
to clear the readonly bit and reattempt the remove. Any subsequent failure
will propagate.

```
import os, stat
import shutil

def remove_readonly(func, path, _):
    "Clear the readonly bit and reattempt the removal"
    os.chmod(path, stat.S_IWRITE)
    func(path)

shutil.rmtree(directory, onexc=remove_readonly)
```