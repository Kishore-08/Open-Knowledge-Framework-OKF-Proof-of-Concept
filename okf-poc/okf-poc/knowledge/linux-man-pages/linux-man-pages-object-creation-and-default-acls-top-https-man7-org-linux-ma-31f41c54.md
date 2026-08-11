---
id: linux-man-pages-object-creation-and-default-acls-top-https-man7-org-linux-ma-31f41c54
type: concept
title: OBJECT CREATION AND DEFAULT ACLs         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## OBJECT CREATION AND DEFAULT ACLs         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       The access ACL of a file object is initialized when the object is
       created with any of the creat(), mkdir(), mknod(), mkfifo(), or
       open() functions. If a default ACL is associated with a directory,
       the mode parameter to the functions creating file objects and the
       default ACL of the directory are used to determine the ACL of the
       new object:

       1.   The new object inherits the default ACL of the containing
            directory as its access ACL.

       2.   The access ACL entries corresponding to the file permission
            bits are modified so that they contain no permissions that
            are not contained in the permissions specified by the mode
            parameter.

       If no default ACL is associated with a directory, the mode
       parameter to the functions creating file objects and the file
       creation mask (see umask(2)) are used to determine the ACL of the
       new object:

       1.   The new object is assigned an access ACL containing entries
            of tag types ACL_USER_OBJ, ACL_GROUP_OBJ, and ACL_OTHER. The
            permissions of these entries are set to the permissions
            specified by the file creation mask.

       2.   The access ACL entries corresponding to the file permission
            bits are modified so that they contain no permissions that
            are not contained in the permissions specified by the mode
            parameter.
```