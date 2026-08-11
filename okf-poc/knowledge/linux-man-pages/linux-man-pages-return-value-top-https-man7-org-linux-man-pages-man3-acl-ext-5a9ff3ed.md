---
id: linux-man-pages-return-value-top-https-man7-org-linux-man-pages-man3-acl-ext-5a9ff3ed
type: concept
title: RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/acl_extended_file.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_extended_file.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/acl_extended_file.3.html#top_of_page)

```
       If successful, the acl_extended_file() function returns 1 if the
       file object referred to by path_p has an extended access ACL or a
       default ACL, and 0 if the file object referred to by path_p has
       neither an extended access ACL nor a default ACL. Otherwise, the
       value -1 is returned and the global variable errno is set to
       indicate the error.
```