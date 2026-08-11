---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-chec-dc9f1f5e
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_check.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_check.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_check.3.html#top_of_page)

```
       The acl_check() function checks the ACL referred to by the
       argument acl for validity.

       The three required entries ACL_USER_OBJ, ACL_GROUP_OBJ, and
       ACL_OTHER must exist exactly once in the ACL. If the ACL contains
       any ACL_USER or ACL_GROUP entries, then an ACL_MASK entry is also
       required. The ACL may contain at most one ACL_MASK entry.

       The user identifiers must be unique among all entries of type
       ACL_USER.  The group identifiers must be unique among all entries
       of type ACL_GROUP.

       If the ACL referred to by acl is invalid, acl_check() returns a
       positive error code that indicates which type of error was
       detected.  The following symbolic error codes are defined:

       ACL_MULTI_ERROR       The ACL contains multiple entries that have
                             a tag type that may occur at most once.

       ACL_DUPLICATE_ERROR   The ACL contains multiple ACL_USER entries
                             with the same user ID, or multiple ACL_GROUP
                             entries with the same group ID.

       ACL_MISS_ERROR        A required entry is missing.

       ACL_ENTRY_ERROR       The ACL contains an invalid entry tag type.

       The acl_error() function can be used to translate error codes to
       text messages.

       In addition, if the pointer last is not NULL, acl_check() assigns
       the number of the ACL entry at which the error was detected to the
       value pointed to by last.  Entries are numbered starting with
       zero, in the order in which they would be returned by the
       acl_get_entry() function.
```