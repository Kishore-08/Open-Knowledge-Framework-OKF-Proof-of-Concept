---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-get-fd-3--3dc37acf
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_get_fd.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_fd.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_get_fd.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_get_fd()
       function returns a value of (acl_t)NULL and sets errno to the
       corresponding value:

       [EBADF]            The fd argument is not a valid file descriptor.

       [ENOMEM]           The ACL working storage requires more memory
                          than is allowed by the hardware or system-
                          imposed memory management constraints.

       [ENOTSUP]          The file system on which the file identified by
                          fd is located does not support ACLs, or ACLs
                          are disabled.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_get_fd.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_get_fd.3.html#top_of_page)

```
       acl_free(3), acl_get_entry(3), acl_get_file(3), acl_set_fd(3),
       acl(5)
```