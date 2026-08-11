---
id: linux-man-pages-invocation-top-https-man7-org-linux-man-pages-man1-abipkgdif-1463afa5
type: concept
title: INVOCATION         [top](https://man7.org/linux/man-pages/man1/abipkgdiff.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abipkgdiff.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## INVOCATION         [top](https://man7.org/linux/man-pages/man1/abipkgdiff.1.html#top_of_page)

```
          abipkgdiff [options] <package1> <package2>

       package1 and package2 are the packages that contain the binaries
       to be compared.

       An alternate invocation style would be:

          abipkgdiff [options] --set1 <pkg1-v1> <pkg2-v1> <pkg3-v1> \
                               --set2 <pkg1-v2> <pkg2-v2> <pkg3-v2>

       where the ABI of binaries contained in the second set of packages
       are compared against binaries contained in the first set of
       packages.
```