---
id: linux-man-pages-synopsis-top-https-man7-org-linux-man-pages-man2-acct-2-html-e5f6339c
type: concept
title: SYNOPSIS         [top](https://man7.org/linux/man-pages/man2/acct.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/acct.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## SYNOPSIS         [top](https://man7.org/linux/man-pages/man2/acct.2.html#top_of_page)

```
       #include <unistd.h>

       int acct(const char *_Nullable path);

   Feature Test Macro Requirements for glibc (see
   feature_test_macros(7)):

       acct():
           Since glibc 2.21:
               _DEFAULT_SOURCE
           In glibc 2.19 and 2.20:
               _DEFAULT_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE < 500)
           Up to and including glibc 2.19:
               _BSD_SOURCE || (_XOPEN_SOURCE && _XOPEN_SOURCE < 500)
```