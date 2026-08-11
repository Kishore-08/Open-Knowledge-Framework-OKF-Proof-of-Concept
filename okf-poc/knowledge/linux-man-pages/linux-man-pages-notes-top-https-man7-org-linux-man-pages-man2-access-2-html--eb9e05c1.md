---
id: linux-man-pages-notes-top-https-man7-org-linux-man-pages-man2-access-2-html--eb9e05c1
type: concept
title: NOTES         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/access.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NOTES         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)

```
       Warning: Using these calls to check if a user is authorized to,
       for example, open a file before actually doing so using open(2)
       creates a security hole, because the user might exploit the short
       time interval between checking and opening the file to manipulate
       it.  For this reason, the use of this system call should be
       avoided.  (In the example just described, a safer alternative
       would be to temporarily switch the process's effective user ID to
       the real ID and then call open(2).)

       access() always dereferences symbolic links.  If you need to check
       the permissions on a symbolic link, use faccessat() with the flag
       AT_SYMLINK_NOFOLLOW.

       These calls return an error if any of the access types in mode is
       denied, even if some of the other access types in mode are
       permitted.

       A file is accessible only if the permissions on each of the
       directories in the path prefix of path grant search (i.e.,
       execute) access.  If any directory is inaccessible, then the
       access() call fails, regardless of the permissions on the file
       itself.

       Only access bits are checked, not the file type or contents.
       Therefore, if a directory is found to be writable, it probably
       means that files can be created in the directory, and not that the
       directory can be written as a file.  Similarly, a DOS file may be
       reported as executable, but the execve(2) call will still fail.

       These calls may not work correctly on NFSv2 filesystems with UID
       mapping enabled, because UID mapping is done on the server and
       hidden from the client, which checks permissions.  (NFS versions 3
       and higher perform the check on the server.)  Similar problems can
       occur to FUSE mounts.
```