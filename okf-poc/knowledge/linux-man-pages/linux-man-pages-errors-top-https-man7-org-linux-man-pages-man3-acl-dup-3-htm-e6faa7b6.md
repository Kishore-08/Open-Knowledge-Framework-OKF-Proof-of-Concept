---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-dup-3-htm-e6faa7b6
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_dup.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_dup() function
       returns a value of (acl_t)NULL and sets errno to the corresponding
       value:

       [EINVAL]           The argument acl is not a valid pointer to an
                          ACL.

       [ENOMEM]           The acl_t to be returned requires more memory
                          than is allowed by the hardware or system-
                          imposed memory management constraints.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)

```
       acl_free(3), acl_get_entry(3), acl(5)
```