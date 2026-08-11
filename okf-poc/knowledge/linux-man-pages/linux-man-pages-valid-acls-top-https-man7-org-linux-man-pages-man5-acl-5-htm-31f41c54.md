---
id: linux-man-pages-valid-acls-top-https-man7-org-linux-man-pages-man5-acl-5-htm-31f41c54
type: concept
title: VALID ACLs         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## VALID ACLs         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       A valid ACL contains exactly one entry with each of the
       ACL_USER_OBJ, ACL_GROUP_OBJ, and ACL_OTHER tag types. Entries with
       ACL_USER and ACL_GROUP tag types may appear zero or more times in
       an ACL. An ACL that contains entries of ACL_USER or ACL_GROUP tag
       types must contain exactly one entry of the ACL_MASK tag type. If
       an ACL contains no entries of ACL_USER or ACL_GROUP tag types, the
       ACL_MASK entry is optional.

       All user ID qualifiers must be unique among all entries of
       ACL_USER tag type, and all group IDs must be unique among all
       entries of ACL_GROUP tag type.

         The acl_get_file() function returns an ACL with zero ACL entries
       as the default ACL of a directory, if the directory is not
       associated with a default ACL. The acl_set_file() function also
       accepts an ACL with zero ACL entries as a valid default ACL for
       directories, denoting that the directory shall not be associated
       with a default ACL. This is equivalent to using the
       acl_delete_def_file() function.
```