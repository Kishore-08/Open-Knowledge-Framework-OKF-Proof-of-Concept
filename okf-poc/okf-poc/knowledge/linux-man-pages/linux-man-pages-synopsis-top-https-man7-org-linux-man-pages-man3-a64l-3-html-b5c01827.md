---
id: linux-man-pages-synopsis-top-https-man7-org-linux-man-pages-man3-a64l-3-html-b5c01827
type: concept
title: SYNOPSIS         [top](https://man7.org/linux/man-pages/man3/a64l.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/a64l.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## SYNOPSIS         [top](https://man7.org/linux/man-pages/man3/a64l.3.html#top_of_page)

```
       #include <stdlib.h>

       long a64l(const char *str64);
       char *l64a(long value);

   Feature Test Macro Requirements for glibc (see
   feature_test_macros(7)):

       a64l(), l64a():
           _XOPEN_SOURCE >= 500
               || /* glibc >= 2.19: */ _DEFAULT_SOURCE
               || /* glibc <= 2.19: */ _SVID_SOURCE
```