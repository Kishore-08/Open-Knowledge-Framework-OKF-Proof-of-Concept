---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-exte-06a7c890
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_extended_fd.3.html#top_of_page)

```
       The acl_extended_fd() function returns 1 if the file identified by
       the argument fd is associated with an extended access ACL. The
       function returns 0 if the file does not have an extended access
       ACL.

       An extended ACL is an ACL that contains entries other than the
       three required entries of tag types ACL_USER_OBJ, ACL_GROUP_OBJ
       and ACL_OTHER.  If the result of the acl_extended_fd() function
       for a file object is 0, then the ACL defines no discretionary
       access rights other than those already defined by the traditional
       file permission bits.

       Access to the file object may be further restricted by other
       mechanisms, such as Mandatory Access Control schemes. The
       access(2) system call can be used to check whether a given type of
       access to a file object would be granted.
```