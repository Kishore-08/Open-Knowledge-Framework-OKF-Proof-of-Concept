---
id: linux-man-pages-versions-top-https-man7-org-linux-man-pages-man2-access-2-ht-eb9e05c1
type: concept
title: VERSIONS         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/access.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## VERSIONS         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)

```
       If the calling process has appropriate privileges (i.e., is
       superuser), POSIX.1-2001 permits an implementation to indicate
       success for an X_OK check even if none of the execute file
       permission bits are set.  Linux does not do this.

   C library/kernel differences
       The raw faccessat() system call takes only the first three
       arguments.  The AT_EACCESS and AT_SYMLINK_NOFOLLOW flags are
       actually implemented within the glibc wrapper function for
       faccessat().  If either of these flags is specified, then the
       wrapper function employs fstatat(2) to determine access
       permissions, but see BUGS.

   glibc notes
       On older kernels where faccessat() is unavailable (and when the
       AT_EACCESS and AT_SYMLINK_NOFOLLOW flags are not specified), the
       glibc wrapper function falls back to the use of access().  When
       path is relative, glibc constructs a pathname based on the
       symbolic link in /proc/self/fd that corresponds to the dirfd
       argument.
```