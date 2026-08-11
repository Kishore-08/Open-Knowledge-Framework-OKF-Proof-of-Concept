---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man2-access-2-html-eb9e05c1
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/access.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)

```
       EACCES The requested access would be denied to the file, or search
              permission is denied for one of the directories in the path
              prefix of path.  (See also path_resolution(7).)

       EBADF  (faccessat()) path is relative but dirfd is neither
              AT_FDCWD (faccessat()) nor a valid file descriptor.

       EFAULT path points outside your accessible address space.

       EINVAL mode was incorrectly specified.

       EINVAL (faccessat()) Invalid flag specified in flags.

       EIO    An I/O error occurred.

       ELOOP  Too many symbolic links were encountered in resolving path.

       ENAMETOOLONG
              path is too long.

       ENOENT A component of path does not exist or is a dangling
              symbolic link.

       ENOMEM Insufficient kernel memory was available.

       ENOTDIR
              A component used as a directory in path is not, in fact, a
              directory.

       ENOTDIR
              (faccessat()) path is relative and dirfd is a file
              descriptor referring to a file other than a directory.

       EPERM  Write permission was requested to a file that has the
              immutable flag set.  See also FS_IOC_SETFLAGS(2const).

       EROFS  Write permission was requested for a file on a read-only
              filesystem.

       ETXTBSY
              Write access was requested to an executable which is being
              executed.
```