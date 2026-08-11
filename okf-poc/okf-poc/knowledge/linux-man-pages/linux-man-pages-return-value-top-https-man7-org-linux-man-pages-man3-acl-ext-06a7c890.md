---
id: linux-man-pages-return-value-top-https-man7-org-linux-man-pages-man3-acl-ext-06a7c890
type: concept
title: RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html#top_of_page)

```
       If successful, the acl_extended_fd() function returns 1 if the
       file object identified by fd has an extended access ACL, and 0 if
       the file object identified by fd does not have an extended access
       ACL. Otherwise, the value -1 is returned and the global variable
       errno is set to indicate the error.
```