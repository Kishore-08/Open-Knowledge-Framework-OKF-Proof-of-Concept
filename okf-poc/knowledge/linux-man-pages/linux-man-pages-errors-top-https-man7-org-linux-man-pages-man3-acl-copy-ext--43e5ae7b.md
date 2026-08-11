---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-copy-ext--43e5ae7b
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_copy_ext.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_copy_ext.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_copy_ext.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_copy_ext()
       function returns a value of (ssize_t)-1 and sets errno to the
       corresponding value:

       [EINVAL]           The size parameter is zero or negative.

                          The argument acl is not a valid pointer to an
                          ACL.

                          The ACL referenced by acl contains one or more
                          improperly formed ACL entries, or for some
                          other reason cannot be translated into the
                          external form of an ACL.

       [ERANGE]           The size parameter is greater than zero but
                          smaller than the length of the contiguous,
                          persistent form of the ACL.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_copy_ext.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_copy_ext.3.html#top_of_page)

```
       acl_copy_int(3), acl_size(3), acl(5)
```