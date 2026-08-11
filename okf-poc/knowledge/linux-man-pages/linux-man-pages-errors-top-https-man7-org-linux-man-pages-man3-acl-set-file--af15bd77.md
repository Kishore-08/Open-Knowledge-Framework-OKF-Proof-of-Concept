---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-set-file--af15bd77
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_set_file.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_set_file.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_set_file.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_set_file()
       function returns -1 and sets errno to the corresponding value:

       [EACCES]           Search permission is denied for a component of
                          the path prefix or the object exists and the
                          process does not have appropriate access
                          rights.

                          Argument type specifies a type of ACL that
                          cannot be associated with path_p.

       [EINVAL]           The argument acl does not point to a valid ACL.

                          The ACL has more entries than the file referred
                          to by path_p can obtain.

                          The type parameter is not ACL_TYPE_ACCESS or
                          ACL_TYPE_DEFAULT.

                          The type parameter is ACL_TYPE_DEFAULT, but the
                          file referred to by path_p is not a directory.

       [ENAMETOOLONG]     The length of the argument path_p is too long.

       [ENOENT]           The named object does not exist or the argument
                          path_p points to an empty string.

       [ENOSPC]           The directory or file system that would contain
                          the new ACL cannot be extended or the file
                          system is out of file allocation resources.

       [ENOTDIR]          A component of the path prefix is not a
                          directory.

       [ENOTSUP]          The file identified by path_p cannot be
                          associated with the ACL because the file system
                          on which the file is located does not support
                          this.

       [EPERM]            The process does not have appropriate privilege
                          to perform the operation to set the ACL.

       [EROFS]            This function requires modification of a file
                          system which is currently read-only.
```