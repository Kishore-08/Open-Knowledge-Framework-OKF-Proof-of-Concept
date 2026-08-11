---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-get-entry-c2b06266
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_get_entry.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_entry.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_get_entry.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_get_entry()
       function returns -1 and sets errno to the corresponding value:

       [EINVAL]           The argument acl_p is not a valid pointer to an
                          ACL.

                          The argument entry_id is neither ACL_NEXT_ENTRY
                          nor ACL_FIRST_ENTRY.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_get_entry.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```