---
id: linux-man-pages-correspondence-between-acl-entries-and-file-permission-bits--31f41c54
type: concept
title: CORRESPONDENCE BETWEEN ACL ENTRIES AND FILE PERMISSION BITS         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## CORRESPONDENCE BETWEEN ACL ENTRIES AND FILE PERMISSION BITS         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       The permissions defined by ACLs are a superset of the permissions
       specified by the file permission bits.

       There is a correspondence between the file owner, group, and other
       permissions and specific ACL entries: the owner permissions
       correspond to the permissions of the ACL_USER_OBJ entry. If the
       ACL has an ACL_MASK entry, the group permissions correspond to the
       permissions of the ACL_MASK entry.  Otherwise, if the ACL has no
       ACL_MASK entry, the group permissions correspond to the
       permissions of the ACL_GROUP_OBJ entry.  The other permissions
       correspond to the permissions of the ACL_OTHER entry.

       The file owner, group, and other permissions always match the
       permissions of the corresponding ACL entry. Modification of the
       file permission bits results in the modification of the associated
       ACL entries, and modification of these ACL entries results in the
       modification of the file permission bits.
```