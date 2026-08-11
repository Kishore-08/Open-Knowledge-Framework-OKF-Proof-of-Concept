---
id: linux-man-pages-standards-top-https-man7-org-linux-man-pages-man3-acl-set-fi-af15bd77
type: concept
title: STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_set_file.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_set_file.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_set_file.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)

       The behavior of acl_set_file() when the acl parameter refers to an
       empty ACL and the type parameter is ACL_TYPE_DEFAULT is an
       extension in the Linux implementation, in order that all values
       returned by acl_get_file() can be passed to acl_set_file().  The
       POSIX.1e function for removing a default ACL is
       acl_delete_def_file().
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_set_file.3.html#top_of_page)

```
       acl_delete_def_file(3), acl_get_file(3), acl_set_fd(3),
       acl_valid(3), acl(5)
```