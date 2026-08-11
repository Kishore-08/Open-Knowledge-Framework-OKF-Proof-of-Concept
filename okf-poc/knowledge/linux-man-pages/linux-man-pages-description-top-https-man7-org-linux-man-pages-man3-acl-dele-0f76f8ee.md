---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-dele-0f76f8ee
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_delete_def_file.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_delete_def_file.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_delete_def_file.3.html#top_of_page)

```
       The acl_delete_def_file() function deletes a default ACL from the
       directory whose pathname is pointed to by the argument path_p.

       The effective user ID of the process must match the owner of the
       file or directory or the process must have the CAP_FOWNER
       capability for the request to succeed.

       If the argument path_p is not a directory, then the function
       fails. It is no error if the directory whose pathname is pointed
       to by the argument path_p does not have a default ACL.
```