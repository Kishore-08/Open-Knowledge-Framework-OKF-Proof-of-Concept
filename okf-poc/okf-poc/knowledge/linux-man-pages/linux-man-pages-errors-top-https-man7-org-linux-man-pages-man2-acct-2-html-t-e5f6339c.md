---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man2-acct-2-html-t-e5f6339c
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man2/acct.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/acct.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man2/acct.2.html#top_of_page)

```
       EACCES Write permission is denied for the specified file, or
              search permission is denied for one of the directories in
              the path prefix of path (see also path_resolution(7)), or
              path is not a regular file.

       EFAULT path points outside your accessible address space.

       EIO    Error writing to the file path.

       EISDIR path is a directory.

       ELOOP  Too many symbolic links were encountered in resolving path.

       ENAMETOOLONG
              path was too long.

       ENFILE The system-wide limit on the total number of open files has
              been reached.

       ENOENT The specified path does not exist.

       ENOMEM Out of memory.

       ENOSYS BSD process accounting has not been enabled when the
              operating system kernel was compiled.  The kernel
              configuration parameter controlling this feature is
              CONFIG_BSD_PROCESS_ACCT.

       ENOTDIR
              A component used as a directory in path is not in fact a
              directory.

       EPERM  The calling process has insufficient privilege to enable
              process accounting.  On Linux, the CAP_SYS_PACCT capability
              is required.

       EROFS  path refers to a file on a read-only filesystem.

       EUSERS There are no more free file structures or we ran out of
              memory.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man2/acct.2.html#top_of_page)

```
       None.
```

## HISTORY         [top](https://man7.org/linux/man-pages/man2/acct.2.html#top_of_page)

```
       SVr4, 4.3BSD.
```