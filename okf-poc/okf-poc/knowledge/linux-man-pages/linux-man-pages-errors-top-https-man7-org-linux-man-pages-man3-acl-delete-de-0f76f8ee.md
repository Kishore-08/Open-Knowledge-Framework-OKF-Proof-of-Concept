---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-delete-de-0f76f8ee
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_delete_def_file.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_delete_def_file.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_delete_def_file.3.html#top_of_page)

```
       If any of the following conditions occur, the
       acl_delete_def_file() function returns the value -1 and and sets
       errno to the corresponding value:

       [EINVAL]           The file referred to by path_p is not a
                          directory.

       [ENOTSUP]          The file system on which the file identified by
                          path_p is located does not support ACLs, or
                          ACLs are disabled.

       [EPERM]            The process does not have appropriate privilege
                          to perform the operation to delete the default
                          ACL.

       [EROFS]            This function requires modification of a file
                          system which is currently read-only.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_delete_def_file.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_delete_def_file.3.html#top_of_page)

```
       acl_get_file(3), acl_set_file(3), acl(5)
```