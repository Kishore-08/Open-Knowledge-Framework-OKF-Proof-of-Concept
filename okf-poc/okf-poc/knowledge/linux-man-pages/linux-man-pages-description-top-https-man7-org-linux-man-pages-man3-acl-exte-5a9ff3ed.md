---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-exte-5a9ff3ed
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_extended_file.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_extended_file.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_extended_file.3.html#top_of_page)

```
       The acl_extended_file() function returns 1 if the file or
       directory referred to by the argument path_p is associated with an
       extended access ACL, or if the directory referred to by path_p is
       associated with a default ACL. The function returns 0 if the file
       has neither an extended access ACL nor a default ACL.

       An extended ACL is an ACL that contains entries other than the
       three required entries of tag types ACL_USER_OBJ, ACL_GROUP_OBJ
       and ACL_OTHER.  If the result of the acl_extended_file() function
       for a file object is 0, then ACLs define no discretionary access
       rights other than those already defined by the traditional file
       permission bits.

       Access to the file object may be further restricted by other
       mechanisms, such as Mandatory Access Control schemes. The
       access(2) system call can be used to check whether a given type of
       access to a file object would be granted.

       acl_extended_file_nofollow() is identical to acl_extended_file(),
       except in the case of a symbolic link, where the link itself is
       interrogated, not the file that it refers to.  Since symbolic
       links have no ACL themselves, the operation is supposed to fail on
       them.
```