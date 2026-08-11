---
id: linux-man-pages-bugs-top-https-man7-org-linux-man-pages-man2-access-2-html-t-eb9e05c1
type: concept
title: BUGS         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/access.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## BUGS         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)

```
       Because the Linux kernel's faccessat() system call does not
       support a flags argument, the glibc faccessat() wrapper function
       provided in glibc 2.32 and earlier emulates the required
       functionality using a combination of the faccessat() system call
       and fstatat(2).  However, this emulation does not take ACLs into
       account.  Starting with glibc 2.33, the wrapper function avoids
       this bug by making use of the faccessat2() system call where it is
       provided by the underlying kernel.

       In Linux 2.4 (and earlier) there is some strangeness in the
       handling of X_OK tests for superuser.  If all categories of
       execute permission are disabled for a nondirectory file, then the
       only access() test that returns -1 is when mode is specified as
       just X_OK; if R_OK or W_OK is also specified in mode, then
       access() returns 0 for such files.  Early Linux 2.6 (up to and
       including Linux 2.6.3) also behaved in the same way as Linux 2.4.

       Before Linux 2.6.20, these calls ignored the effect of the
       MS_NOEXEC flag if it was used to mount(2) the underlying
       filesystem.  Since Linux 2.6.20, the MS_NOEXEC flag is honored.
```