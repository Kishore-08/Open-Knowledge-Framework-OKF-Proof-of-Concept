---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-get--3dc37acf
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_fd.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_fd.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_fd.3.html#top_of_page)

```
       The acl_get_fd() function retrieves the access ACL associated with
       the file referred to by fd.  The ACL is placed into working
       storage and acl_get_fd() returns a pointer to that storage.

       In order to read an ACL from an object, a process must have read
       access to the object's attributes.

       This function may cause memory to be allocated.  The caller should
       free any releasable memory, when the new ACL is no longer
       required, by calling acl_free(3) with the (void*)acl_t returned by
       acl_get_fd() as an argument.
```