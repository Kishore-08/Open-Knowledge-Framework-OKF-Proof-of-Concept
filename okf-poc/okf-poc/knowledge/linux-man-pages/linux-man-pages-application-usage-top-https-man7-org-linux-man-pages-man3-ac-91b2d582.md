---
id: linux-man-pages-application-usage-top-https-man7-org-linux-man-pages-man3-ac-91b2d582
type: concept
title: APPLICATION USAGE         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/access.3p.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## APPLICATION USAGE         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)

```
       Use of these functions is discouraged since by the time the
       returned information is acted upon, it is out-of-date. (That is,
       acting upon the information always leads to a time-of-check-to-
       time-of-use race condition.) An application should instead attempt
       the action itself and handle the [EACCES] error that occurs if the
       file is not accessible (with a change of effective user and group
       IDs beforehand, and perhaps a change back afterwards, in the case
       where access() or faccessat() without AT_EACCES would have been
       used.)

       Historically, one of the uses of access() was in set-user-ID root
       programs to check whether the user running the program had access
       to a file. This relied on ``super-user'' privileges which were
       granted based on the effective user ID being zero, so that when
       access() used the real user ID to check accessibility those
       privileges were not taken into account. On newer systems where
       privileges can be assigned which have no association with user or
       group IDs, if a program with such privileges calls access(), the
       change of IDs has no effect on the privileges and therefore they
       are taken into account in the accessibility checks. Thus, access()
       (and faccessat() with flag zero) cannot be used for this
       historical purpose in such programs. Likewise, if a system
       provides any additional or alternate file access control
       mechanisms that are not user ID-based, they will still be taken
       into account.

       If a relative pathname is used, no account is taken of whether the
       current directory (or the directory associated with the file
       descriptor fd) is accessible via any absolute pathname.
       Applications using access(), or faccessat() without AT_EACCES, may
       consequently act as if the file would be accessible to a user with
       the real user ID and group ID of the process when such a user
       would not in practice be able to access the file because access
       would be denied at some point above the current directory (or the
       directory associated with the file descriptor fd) in the file
       hierarchy.

       If access() or faccessat() is used with W_OK to check for write
       access to a directory which has the S_ISVTX bit set, a return
       value indicating the directory is writable can be misleading since
       some operations on files in the directory would not be permitted
       based on the ownership of those files (see the Base Definitions
       volume of POSIX.1‐2017, Section 4.3, Directory Protection).

       Additional values of amode other than the set defined in the
       description may be valid; for example, if a system has extended
       access controls.

       The use of the AT_EACCESS value for flag enables functionality not
       available in access().
```