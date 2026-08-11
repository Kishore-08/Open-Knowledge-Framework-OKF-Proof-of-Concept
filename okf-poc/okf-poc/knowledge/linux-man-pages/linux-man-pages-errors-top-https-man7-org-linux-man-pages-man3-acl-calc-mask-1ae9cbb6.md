---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-calc-mask-1ae9cbb6
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_calc_mask.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_calc_mask.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_calc_mask.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_calc_mask()
       function returns -1 and sets errno to the corresponding value:

       [EINVAL]           The argument acl is not a valid pointer to an
                          ACL.

       [ENOMEM]           The acl_calc_mask() function is unable to
                          allocate the memory required for an ACL_MASK
                          ACL entry.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_calc_mask.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_calc_mask.3.html#top_of_page)

```
       acl_check(3), acl_get_entry(3), acl_valid(3), acl(5)
```