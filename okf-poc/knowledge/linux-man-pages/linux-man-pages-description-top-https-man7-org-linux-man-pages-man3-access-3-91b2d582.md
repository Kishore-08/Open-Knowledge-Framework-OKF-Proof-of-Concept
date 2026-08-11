---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-access-3-91b2d582
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/access.3p.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)

```
       The access() function shall check the file named by the pathname
       pointed to by the path argument for accessibility according to the
       bit pattern contained in amode.  The checks for accessibility
       (including directory permissions checked during pathname
       resolution) shall be performed using the real user ID in place of
       the effective user ID and the real group ID in place of the
       effective group ID.

       The value of amode is either the bitwise-inclusive OR of the
       access permissions to be checked (R_OK, W_OK, X_OK) or the
       existence test (F_OK).

       If any access permissions are checked, each shall be checked
       individually, as described in the Base Definitions volume of
       POSIX.1‐2017, Section 4.5, File Access Permissions, except that
       where that description refers to execute permission for a process
       with appropriate privileges, an implementation may indicate
       success for X_OK even if execute permission is not granted to any
       user.

       The faccessat() function, when called with a flag value of zero,
       shall be equivalent to the access() function, except in the case
       where path specifies a relative path. In this case the file whose
       accessibility is to be determined shall be located relative to the
       directory associated with the file descriptor fd instead of the
       current working directory.  If the access mode of the open file
       description associated with the file descriptor is not O_SEARCH,
       the function shall check whether directory searches are permitted
       using the current permissions of the directory underlying the file
       descriptor.  If the access mode is O_SEARCH, the function shall
       not perform the check.

       If faccessat() is passed the special value AT_FDCWD in the fd
       parameter, the current working directory shall be used and, if
       flag is zero, the behavior shall be identical to a call to
       access().

       Values for flag are constructed by a bitwise-inclusive OR of flags
       from the following list, defined in <fcntl.h>:

       AT_EACCESS  The checks for accessibility (including directory
                   permissions checked during pathname resolution) shall
                   be performed using the effective user ID and group ID
                   instead of the real user ID and group ID as required
                   in a call to access().
```