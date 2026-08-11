---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man2-access-2-eb9e05c1
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/access.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)

```
       access() checks whether the calling process can access the file
       path.  If path is a symbolic link, it is dereferenced.

       The mode specifies the accessibility check(s) to be performed, and
       is either the value F_OK, or a mask consisting of the bitwise OR
       of one or more of R_OK, W_OK, and X_OK.  F_OK tests for the
       existence of the file.  R_OK, W_OK, and X_OK test whether the file
       exists and grants read, write, and execute permissions,
       respectively.

       The check is done using the calling process's real UID and GID,
       rather than the effective IDs as is done when actually attempting
       an operation (e.g., open(2)) on the file.  Similarly, for the root
       user, the check uses the set of permitted capabilities rather than
       the set of effective capabilities; and for non-root users, the
       check uses an empty set of capabilities.

       This allows set-user-ID programs and capability-endowed programs
       to easily determine the invoking user's authority.  In other
       words, access() does not answer the "can I read/write/execute this
       file?" question.  It answers a slightly different question:
       "(assuming I'm a setuid binary) can the user who invoked me
       read/write/execute this file?", which gives set-user-ID programs
       the possibility to prevent malicious users from causing them to
       read files which users shouldn't be able to read.

       If the calling process is privileged (i.e., its real UID is zero),
       then an X_OK check is successful for a regular file if execute
       permission is enabled for any of the file owner, group, or other.

   faccessat()
       faccessat() operates in exactly the same way as access(), except
       for the differences described here.

       If path is relative, then it is interpreted relative to the
       directory referred to by the file descriptor dirfd (rather than
       relative to the current working directory of the calling process,
       as is done by access() for a relative pathname).

       If path is relative and dirfd is the special value AT_FDCWD, then
       path is interpreted relative to the current working directory of
       the calling process (like access()).

       If path is absolute, then dirfd is ignored.

       flags is constructed by ORing together zero or more of the
       following values:

       AT_EACCESS
              Perform access checks using the effective user and group
              IDs.  By default, faccessat() uses the real IDs (like
              access()).

       AT_EMPTY_PATH (since Linux 5.8)
              If path is an empty string, operate on the file referred to
              by dirfd (which may have been obtained using the open(2)
              O_PATH flag).  In this case, dirfd can refer to any type of
              file, not just a directory.  If dirfd is AT_FDCWD, the call
              operates on the current working directory.  This flag is
              Linux-specific; define _GNU_SOURCE to obtain its
              definition.

       AT_SYMLINK_NOFOLLOW
              If path is a symbolic link, do not dereference it: instead
              return information about the link itself.

       See openat(2) for an explanation of the need for faccessat().

   faccessat2()
       The description of faccessat() given above corresponds to POSIX.1
       and to the implementation provided by glibc.  However, the glibc
       implementation was an imperfect emulation (see BUGS) that papered
       over the fact that the raw Linux faccessat() system call does not
       have a flags argument.  To allow for a proper implementation,
       Linux 5.8 added the faccessat2() system call, which supports the
       flags argument and allows a correct implementation of the
       faccessat() wrapper function.
```