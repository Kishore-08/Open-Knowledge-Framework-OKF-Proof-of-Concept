---
id: linux-man-pages-access-check-algorithm-top-https-man7-org-linux-man-pages-ma-31f41c54
type: concept
title: ACCESS CHECK ALGORITHM         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ACCESS CHECK ALGORITHM         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       A process may request read, write, or execute/search access to a
       file object protected by an ACL. The access check algorithm
       determines whether access to the object will be granted.

       1.   If the effective user ID of the process matches the user ID
            of the file object owner, then

                  if   the  ACL_USER_OBJ  entry  contains  the  requested
                  permissions, access is granted,

                  else access is denied.

       2.   else if the effective user ID of the process matches the
            qualifier of any entry of type ACL_USER, then

                  if the matching ACL_USER entry and the  ACL_MASK  entry
                  contain the requested permissions, access is granted,

                  else access is denied.

       3.   else if the effective group ID or any of the supplementary
            group IDs of the process match the file group or the
            qualifier of any entry of type ACL_GROUP, then

                  if the ACL contains an ACL_MASK entry, then

                        if  the  ACL_MASK  entry  and any of the matching
                        ACL_GROUP_OBJ or ACL_GROUP  entries  contain  the
                        requested permissions, access is granted,

                        else access is denied.

                  else  (note  that  there  can  be  no ACL_GROUP entries
                  without an ACL_MASK entry)

                        if the ACL_GROUP_OBJ entry contains the requested
                        permissions, access is granted,

                        else access is denied.

       4.   else if the ACL_OTHER entry contains the requested
            permissions, access is granted.

       5.   else access is denied.
```