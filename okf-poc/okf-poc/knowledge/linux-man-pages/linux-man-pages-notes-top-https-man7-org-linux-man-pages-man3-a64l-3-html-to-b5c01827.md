---
id: linux-man-pages-notes-top-https-man7-org-linux-man-pages-man3-a64l-3-html-to-b5c01827
type: concept
title: NOTES         [top](https://man7.org/linux/man-pages/man3/a64l.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/a64l.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NOTES         [top](https://man7.org/linux/man-pages/man3/a64l.3.html#top_of_page)

```
       The value returned by l64a() may be a pointer to a static buffer,
       possibly overwritten by later calls.

       The behavior of l64a() is undefined when value is negative.  If
       value is zero, it returns an empty string.

       These functions are broken before glibc 2.2.5 (puts most
       significant digit first).

       This is not the encoding used by uuencode(1).
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/a64l.3.html#top_of_page)

```
       uuencode(1), strtoul(3)
```