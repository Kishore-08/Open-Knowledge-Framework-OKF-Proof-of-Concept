---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-equi-083028d0
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_equiv_mode.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_equiv_mode.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_equiv_mode.3.html#top_of_page)

```
       The acl_equiv_mode() function checks if the ACL pointed to by the
       argument acl contains only the required ACL entries of tag types
       ACL_USER_OBJ, ACL_GROUP_OBJ, and ACL_OTHER, and contains no
       permissions other that ACL_READ, ACL_WRITE or ACL_EXECUTE.  If the
       ACL has this form, it can can be fully represented with the
       traditional file permission bits, and is considered equivalent
       with the traditional file permission bits.

       If acl is an equivalent ACL and the pointer mode_p is not NULL,
       the value pointed to by mode_p is set to the value that defines
       the same owner, group and other permissions as contained in the
       ACL.
```