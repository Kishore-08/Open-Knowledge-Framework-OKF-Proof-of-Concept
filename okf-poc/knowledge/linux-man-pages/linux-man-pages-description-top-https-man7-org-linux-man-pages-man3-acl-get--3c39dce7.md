---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-get--3c39dce7
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_permset.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_permset.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_permset.3.html#top_of_page)

```
       The acl_get_permset() function returns in permset_p a descriptor
       to the permission set in the ACL entry indicated by entry_d.
       Subsequent operations using the returned permission set descriptor
       operate on the permission set within the ACL entry.

       Any ACL entry descriptors that refer to the entry referred to by
       entry_d shall continue to refer to those entries.
```