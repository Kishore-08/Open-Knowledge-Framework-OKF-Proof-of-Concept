---
id: linux-man-pages-return-value-top-https-man7-org-linux-man-pages-man3-acl-get-105cf513
type: concept
title: RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/acl_get_perm.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_perm.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/acl_get_perm.3.html#top_of_page)

```
       If successful, the acl_get_perm() function returns 1 if the
       permission specified by perm is contained in the ACL permission
       set permset_d, and 0 if the permission is not contained in the
       permission set. Otherwise, the value -1 is returned and the global
       variable errno is set to indicate the error.
```