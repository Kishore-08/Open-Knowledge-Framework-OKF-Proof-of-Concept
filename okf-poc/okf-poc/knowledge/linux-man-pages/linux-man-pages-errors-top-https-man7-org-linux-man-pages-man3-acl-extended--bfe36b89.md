---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-extended--bfe36b89
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_extended_file_nofollow.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_extended_file_nofollow.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_extended_file_nofollow.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_extended_file()
       function returns -1 and sets errno to the corresponding value:

       [EACCES]           Search permission is denied for a component of
                          the path prefix.

       [ENAMETOOLONG]     The length of the argument path_p is too long.

       [ENOENT]           The named object does not exist or the argument
                          path_p points to an empty string.

       [ENOTDIR]          A component of the path prefix is not a
                          directory.

       [ENOTSUP]          The file system on which the file identified by
                          path_p is located does not support ACLs, or
                          ACLs are disabled.
```