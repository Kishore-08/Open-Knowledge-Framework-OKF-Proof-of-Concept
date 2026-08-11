---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-set-fd-3--1a789181
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_set_fd.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_set_fd.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_set_fd.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_set_fd()
       function returns the value -1 and and sets errno to the
       corresponding value:

       [EBADF]            The fd argument is not a valid file descriptor.

       [EINVAL]           The argument acl does not point to a valid ACL.

                          The ACL has more entries than the file referred
                          to by fd can obtain.

       [ENOSPC]           The directory or file system that would contain
                          the new ACL cannot be extended or the file
                          system is out of file allocation resources.

       [ENOTSUP]          The file identified by fd cannot be associated
                          with the ACL because the file system on which
                          the file is located does not support this.

       [EPERM]            The process does not have appropriate privilege
                          to perform the operation to set the ACL.

       [EROFS]            This function requires modification of a file
                          system which is currently read-only.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_set_fd.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_set_fd.3.html#top_of_page)

```
       acl_delete_def_file(3), acl_get_file(3), acl_set_file(3),
       acl_valid(3), acl(5)
```