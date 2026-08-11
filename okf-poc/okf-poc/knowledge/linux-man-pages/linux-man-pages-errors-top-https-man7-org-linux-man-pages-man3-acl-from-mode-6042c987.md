---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-from-mode-6042c987
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_from_mode.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_from_mode.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_from_mode.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_from_mode()
       function returns a value of (acl_t)NULL and sets errno to the
       corresponding value:

       [ENOMEM]           The ACL working storage requires more memory
                          than is allowed by the hardware or system-
                          imposed memory management constraints.
```