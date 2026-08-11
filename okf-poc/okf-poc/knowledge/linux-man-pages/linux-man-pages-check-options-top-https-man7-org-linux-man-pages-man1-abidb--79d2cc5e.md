---
id: linux-man-pages-check-options-top-https-man7-org-linux-man-pages-man1-abidb--79d2cc5e
type: concept
title: CHECK OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidb.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## CHECK OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)

```
          • --check PATH1 PATH2 ...

            Using abidiff, compare each of the listed file, generally
            executables, against abixml documents for selected versions
            for all shared libraries needed by the executable.  These are
            listed by enumerating the dynamic segment tags DT_NEEDED of
            the executable.

          • --ld-library-path DIR1:DIR2:DIR3...

            Select the search paths for abixml documents used to locate
            any particular SONAME .  The first given directory wins.
            However, all versions of the same SONAME in that directory
            are selected for comparison.  The default is unspecified,
            which means to search for all matching SONAME entries in the
            distrobranch, regardless of specific directory.
```