---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-clear-per-567c5a84
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_clear_perms.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_clear_perms.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_clear_perms.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_clear_perms()
       function returns -1 and sets errno to the corresponding value:

       [EINVAL]           The argument permset_d is not a valid
                          descriptor for a permission set within an ACL
                          entry.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_clear_perms.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```