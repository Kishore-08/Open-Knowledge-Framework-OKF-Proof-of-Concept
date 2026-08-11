---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-dele-e3eb24fb
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_delete_perm.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_delete_perm.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_delete_perm.3.html#top_of_page)

```
       The acl_delete_perm() function deletes the permission contained in
       the argument perm (one of ACL_READ, ACL_WRITE, ACL_EXECUTE) from
       the permission set referred to by the argument permset_d.  An
       attempt to delete a permission that is not contained in the
       permission set is not considered an error.

       Any existing descriptors that refer to permset_d continue to refer
       to that permission set.
```