---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-init-7ef1f40d
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_init.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_init.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_init.3.html#top_of_page)

```
       The acl_init() function allocates and initializes the working
       storage for an ACL of at least count ACL entries.  The ACL created
       initially contains no ACL entries.  A pointer to the working
       storage is returned.

       This function may cause memory to be allocated.  The caller should
       free any releasable memory, when the new ACL is no longer
       required, by calling acl_free(3) with the (void*)acl_t returned by
       acl_init() as an argument.
```