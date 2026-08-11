---
id: linux-man-pages-git-repository-schema-top-https-man7-org-linux-man-pages-man-79d2cc5e
type: concept
title: GIT REPOSITORY SCHEMA         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidb.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## GIT REPOSITORY SCHEMA         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)

```
       abidb stores abixml documents in a git repo with the following
       naming schema within the distrobranch:

       1. The directory path leading to the shared library file

       2. The SONAME of the shared library file, as a subdirectory name

       3. A file named BUILDID.xml, where BUILDID is the hexadecimal ELF
          build-id note of the shared library.

       For example:
┌───────────────────────────┬───────────────────────────────────────────────────────────────────┐
│ shared library file name  │ abixml path in git                                                │
├───────────────────────────┼───────────────────────────────────────────────────────────────────┤
│ /usr/lib64/libc.so.6.2.32 │ /usr/lib64/libc.so.6/788cdd41a15985bf8e0a48d213a46e07d58822df.xml │
│ /usr/lib64/libc.so.6.2.33 │ /usr/lib64/libc.so.6/e2ca832f1c2112aea9d7b9bc639e97e873a6b516.xml │
│ /lib/ld-linux.so.2        │ /lib/ld-linux.so.2/b65f3c15b129f33f44f504da1719926aec03c07d.xml   │
└───────────────────────────┴───────────────────────────────────────────────────────────────────┘

       The intent of including the buildid in the name is so that as a
       distro is updated with multiple versions of a given shared
       library, they can be represented nearby but non-conflicting.  The
       SONAME is used in the second-last name component, inspired the
       behavior of ld.so and ldconfig, which rely on symbolic links to
       map references from the SONAME to an actual file.
```