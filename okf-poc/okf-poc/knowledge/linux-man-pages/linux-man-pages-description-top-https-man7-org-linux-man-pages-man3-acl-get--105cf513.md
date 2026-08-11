---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-get--105cf513
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_perm.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_perm.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_perm.3.html#top_of_page)

```
       The acl_get_perm() function tests if the permission specified by
       the argument perm (one of ACL_READ, ACL_WRITE, ACL_EXECUTE) is
       contained in the ACL permission set pointed to by the argument
       permset_d.

       Any existing descriptors that refer to permset_d continue to refer
       to that permission set.
```