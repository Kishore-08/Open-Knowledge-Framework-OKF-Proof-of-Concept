---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-set--1a789181
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_set_fd.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_set_fd.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_set_fd.3.html#top_of_page)

```
       The acl_set_fd() function associates an access ACL with the file
       referred to by fd.

       The effective user ID of the process must match the owner of the
       file or the process must have the CAP_FOWNER capability for the
       request to succeed.
```