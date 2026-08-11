---
id: linux-man-pages-synopsis-top-https-man7-org-linux-man-pages-man2-access-2-ht-eb9e05c1
type: concept
title: SYNOPSIS         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/access.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## SYNOPSIS         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)

```
       #include <unistd.h>

       int access(const char *path, int mode);

       #include <fcntl.h>            /* Definition of AT_* constants */
       #include <unistd.h>

       int faccessat(int dirfd, const char *path, int mode, int flags);
                       /* But see C library/kernel differences, below */

       #include <fcntl.h>            /* Definition of AT_* constants */
       #include <sys/syscall.h>      /* Definition of SYS_* constants */
       #include <unistd.h>

       int syscall(SYS_faccessat2,
                   int dirfd, const char *path, int mode, int flags);

   Feature Test Macro Requirements for glibc (see
   feature_test_macros(7)):

       faccessat():
           Since glibc 2.10:
               _POSIX_C_SOURCE >= 200809L
           Before glibc 2.10:
               _ATFILE_SOURCE
```