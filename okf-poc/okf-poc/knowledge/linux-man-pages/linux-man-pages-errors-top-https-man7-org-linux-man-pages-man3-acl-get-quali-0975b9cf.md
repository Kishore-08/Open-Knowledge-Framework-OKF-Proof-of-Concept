---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-get-quali-0975b9cf
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_get_qualifier.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_qualifier.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_get_qualifier.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_get_qualifier()
       function returns (void *)NULL and sets errno to the corresponding
       value:

       [EINVAL]           The argument entry_d is not a valid descriptor
                          for an ACL entry.

                          The value of the tag type in the ACL entry
                          referenced by the argument entry_d is neither
                          ACL_USER nor ACL_GROUP.

       [ENOMEM]           The value to be returned requires more memory
                          than is allowed by the hardware or system-
                          imposed memory management constraints.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_get_qualifier.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```