---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-dele-2baa3814
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_delete_entry.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_delete_entry.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_delete_entry.3.html#top_of_page)

```
       The acl_delete_entry() function removes the ACL entry indicated by
       the entry_d descriptor from the ACL pointed to by acl.  Any
       existing ACL entry descriptors that refer to entries in acl other
       than that referred to by entry_d continue to refer to the same
       entries. The argument entry_d and any other ACL entry descriptors
       that refer to the same ACL entry are undefined after this function
       completes. Any existing ACL pointers that refer to the ACL
       referred to by acl continue to refer to the ACL.
```