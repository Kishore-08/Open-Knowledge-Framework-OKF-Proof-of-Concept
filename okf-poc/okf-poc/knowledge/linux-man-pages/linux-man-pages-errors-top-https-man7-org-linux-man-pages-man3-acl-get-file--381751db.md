---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-acl-get-file--381751db
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_get_file.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_file.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/acl_get_file.3.html#top_of_page)

```
       If any of the following conditions occur, the acl_get_file()
       function returns a value of (acl_t)NULL and sets errno to the
       corresponding value:

       [EACCES]           Search permission is denied for a component of
                          the path prefix or the object exists and the
                          process does not have appropriate access
                          rights.

                          Argument type specifies a type of ACL that
                          cannot be associated with path_p.

       [EINVAL]           The argument type is not ACL_TYPE_ACCESS or
                          ACL_TYPE_DEFAULT.

       [ENAMETOOLONG]     The length of the argument path_p is too long.

       [ENOENT]           The named object does not exist or the argument
                          path_p points to an empty string.

       [ENOMEM]           The ACL working storage requires more memory
                          than is allowed by the hardware or system-
                          imposed memory management constraints.

       [ENOTDIR]          A component of the path prefix is not a
                          directory.

       [ENOTSUP]          The file system on which the file identified by
                          path_p is located does not support ACLs, or
                          ACLs are disabled.
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man3/acl_get_file.3.html#top_of_page)

```
       IEEE Std 1003.1e draft 17 (“POSIX.1e”, abandoned)
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/acl_get_file.3.html#top_of_page)

```
       acl_free(3), acl_get_entry(3), acl_get_fd(3), acl_set_file(3),
       acl(5)
```