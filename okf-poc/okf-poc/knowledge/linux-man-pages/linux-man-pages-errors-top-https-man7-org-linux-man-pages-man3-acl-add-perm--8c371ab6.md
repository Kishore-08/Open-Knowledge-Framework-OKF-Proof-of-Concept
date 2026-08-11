---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-add-perm--8c371ab6
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_add_perm.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_add_perm.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_add_perm.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_add_perm()
       function returns -1 and sets errno to the corresponding value:

       [EINVAL]           The argument permset_d is not a valid
                          descriptor for a permission set within an ACL
                          entry.

                          The argument perm does not contain a valid
                          acl_perm_t value.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_add_perm.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```