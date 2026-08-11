---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-a64l-3-h-b5c01827
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/a64l.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/a64l.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/a64l.3.html#top_of_page)

```
       These functions provide a conversion between 32-bit long integers
       and little-endian base-64 ASCII strings (of length zero to six).
       If the string used as argument for a64l() has length greater than
       six, only the first six bytes are used.  If the type long has more
       than 32 bits, then l64a() uses only the low order 32 bits of
       value, and a64l() sign-extends its 32-bit result.

       The 64 digits in the base-64 system are:

              '.'  represents a 0
              '/'  represents a 1
              0-9  represent  2-11
              A-Z  represent 12-37
              a-z  represent 38-63

       So 123 = 59*64^0 + 1*64^1 = "v/".
```