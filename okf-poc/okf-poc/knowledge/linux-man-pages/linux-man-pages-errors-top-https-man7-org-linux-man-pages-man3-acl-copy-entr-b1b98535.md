---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-copy-entr-b1b98535
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_copy_entry.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_copy_entry.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_copy_entry.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_copy_entry()
       function returns -1 and sets errno to the corresponding value:

       [EINVAL]           The argument src_d or dest_d is not a valid
                          descriptor for an ACL entry.

                          The arguments src_d and dest_d reference the
                          same ACL entry.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_copy_entry.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_copy_entry.3.html#top_of_page)

```
       acl_get_entry(3), acl(5)
```