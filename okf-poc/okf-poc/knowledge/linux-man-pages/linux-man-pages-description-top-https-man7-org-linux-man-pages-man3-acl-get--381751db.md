---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-get--381751db
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_file.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_file.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_file.3.html#top_of_page)

```
       The acl_get_file() function retrieves the access ACL associated
       with a file or directory, or the default ACL associated with a
       directory. The pathname for the file or directory is pointed to by
       the argument path_p.  The ACL is placed into working storage and
       acl_get_file() returns a pointer to that storage.

       In order to read an ACL from an object, a process must have read
       access to the object's attributes.

       The value of the argument type is used to indicate whether the
       access ACL or the default ACL associated with path_p is returned.
       If type is ACL_TYPE_ACCESS, the access ACL of path_p is returned.
       If type is ACL_TYPE_DEFAULT, the default ACL of path_p is
       returned. If type is ACL_TYPE_DEFAULT and no default ACL is
       associated with the directory path_p, then an ACL containing zero
       ACL entries is returned. If type specifies a type of ACL that
       cannot be associated with path_p, then the function fails.

       This function may cause memory to be allocated.  The caller should
       free any releasable memory, when the new ACL is no longer
       required, by calling acl_free(3) with the (void*)acl_t returned by
       acl_get_file() as an argument.
```