---
id: linux-man-pages-synopsis-top-https-man7-org-linux-man-pages-man3-abs-3-html--c64b576e
type: concept
title: SYNOPSIS         [top](https://man7.org/linux/man-pages/man3/abs.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/abs.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## SYNOPSIS         [top](https://man7.org/linux/man-pages/man3/abs.3.html#top_of_page)

```
       #include <stdlib.h>

       int abs(int j);
       long labs(long j);
       long long llabs(long long j);

       unsigned int uabs(int j);
       unsigned long ulabs(long j);
       unsigned long long ullabs(long long j);

       #include <inttypes.h>

       intmax_t imaxabs(intmax_t j);
       uintmax_t umaxabs(intmax_t j);

   Feature Test Macro Requirements for glibc (see
   feature_test_macros(7)):

       llabs():
           _ISOC99_SOURCE || _POSIX_C_SOURCE >= 200112L

       uabs(), ulabs(), ullabs(), umaxabs():
           _ISOC2Y_SOURCE
```