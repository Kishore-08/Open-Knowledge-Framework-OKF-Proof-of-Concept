---
id: python-archiving-example-with-base-dir-https-docs-python-org-3-libr-4dabd212
type: concept
title: Archiving example with *base\_dir*[¶](https://docs.python.org/3/library/shutil.html#archiving-example-with-base-dir
  "Link to this heading")
description: In this example, similar to the [one above](https://docs.python.org/3/library/shutil.html#shutil-archiving-example),
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/shutil.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Archiving example with *base\_dir*[¶](https://docs.python.org/3/library/shutil.html#archiving-example-with-base-dir "Link to this heading")

In this example, similar to the [one above](https://docs.python.org/3/library/shutil.html#shutil-archiving-example),
we show how to use [`make_archive()`](https://docs.python.org/3/library/shutil.html#shutil.make_archive "shutil.make_archive"), but this time with the usage of
*base\_dir*. We now have the following directory structure:

```
$ tree tmp
tmp
└── root
    └── structure
        ├── content
            └── please_add.txt
        └── do_not_add.txt
```

In the final archive, `please_add.txt` should be included, but
`do_not_add.txt` should not. Therefore we use the following:

```
>>> from shutil import make_archive
>>> import os
>>> archive_name = os.path.expanduser(os.path.join('~', 'myarchive'))
>>> make_archive(
...     archive_name,
...     'tar',
...     root_dir='tmp/root',
...     base_dir='structure/content',
... )
'/Users/tarek/myarchive.tar'
```

Listing the files in the resulting archive gives us:

```
$ python -m tarfile -l /Users/tarek/myarchive.tar
structure/content/
structure/content/please_add.txt
```