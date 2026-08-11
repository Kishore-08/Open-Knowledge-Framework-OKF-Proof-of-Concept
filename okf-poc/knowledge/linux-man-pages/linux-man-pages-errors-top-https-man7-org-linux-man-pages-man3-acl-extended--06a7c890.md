---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-extended--06a7c890
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_extended_fd()
       function returns -1 and sets errno to the corresponding value:

       [EBADF]            The fd argument is not a valid file descriptor.

       [ENOTSUP]          The file system on which the file identified by
                          fd is located does not support ACLs, or ACLs
                          are disabled.
```