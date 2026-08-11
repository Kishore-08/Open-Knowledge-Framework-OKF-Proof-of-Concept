---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-copy-044e1b69
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_copy_int.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_copy_int.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_copy_int.3.html#top_of_page)

```
       The acl_copy_int() function copies an exportable, contiguous,
       persistent form of an ACL, pointed to by buf_p, to the internal
       representation.

       This function may cause memory to be allocated.  The caller should
       free any releasable memory, when the new ACL is no longer
       required, by calling acl_free(3) with the (void*)acl_t returned by
       acl_copy_int() as an argument.
```