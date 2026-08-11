---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-dup--e6faa7b6
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_dup.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)

```
       The acl_dup() function returns a pointer to a copy of the ACL
       pointed to by acl.

       This function may cause memory to be allocated.  The caller should
       free any releasable memory, when the new ACL is no longer
       required, by calling acl_free(3) with the (void*)acl_t returned by
       acl_dup() as an argument.
```