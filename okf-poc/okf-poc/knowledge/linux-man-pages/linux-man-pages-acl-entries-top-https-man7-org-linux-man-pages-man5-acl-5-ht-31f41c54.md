---
id: linux-man-pages-acl-entries-top-https-man7-org-linux-man-pages-man5-acl-5-ht-31f41c54
type: concept
title: ACL ENTRIES         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ACL ENTRIES         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       An ACL consists of a set of ACL entries. An ACL entry specifies
       the access permissions on the associated object for an individual
       user or a group of users as a combination of read, write and
       search/execute permissions.

       An ACL entry contains an entry tag type, an optional entry tag
       qualifier, and a set of permissions.  We use the term qualifier to
       denote the entry tag qualifier of an ACL entry.

       The qualifier denotes the identifier of a user or a group, for
       entries with tag types of ACL_USER or ACL_GROUP, respectively.
       Entries with tag types other than ACL_USER or ACL_GROUP have no
       defined qualifiers.

       The following entry tag types are defined:

             ACL_USER_OBJ    The ACL_USER_OBJ entry denotes access rights
                             for the file owner.

             ACL_USER        ACL_USER entries denote access rights for
                             users identified by the entry's qualifier.

             ACL_GROUP_OBJ   The ACL_GROUP_OBJ entry denotes access
                             rights for the file group.

             ACL_GROUP       ACL_GROUP entries denote access rights for
                             groups identified by the entry's qualifier.

             ACL_MASK        The ACL_MASK entry denotes the maximum
                             access rights that can be granted by entries
                             of type ACL_USER, ACL_GROUP_OBJ, or
                             ACL_GROUP.

             ACL_OTHER       The ACL_OTHER entry denotes access rights
                             for processes that do not match any other
                             entry in the ACL.

       When an access check is performed, the ACL_USER_OBJ and ACL_USER
       entries are tested against the effective user ID. The effective
       group ID, as well as all supplementary group IDs are tested
       against the ACL_GROUP_OBJ and ACL_GROUP entries.
```