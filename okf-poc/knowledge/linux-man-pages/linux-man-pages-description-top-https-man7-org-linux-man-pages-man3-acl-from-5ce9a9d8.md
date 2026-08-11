---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-from-5ce9a9d8
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_from_text.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_from_text.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_from_text.3.html#top_of_page)

```
       The acl_from_text() function converts the text form of the ACL
       referred to by buf_p into the internal form of an ACL and returns
       a pointer to the working storage that contains the ACL. The
       acl_from_text() function accepts as input the long text form and
       short text form of an ACL as described in acl(5).

       This function may cause memory to be allocated.  The caller should
       free any releasable memory, when the new ACL is no longer
       required, by calling acl_free(3) with the (void*)acl_t returned by
       acl_from_text() as an argument.
```