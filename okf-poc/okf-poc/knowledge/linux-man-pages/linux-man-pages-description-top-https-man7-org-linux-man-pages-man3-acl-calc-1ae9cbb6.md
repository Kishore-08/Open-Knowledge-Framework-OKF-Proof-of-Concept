---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-calc-1ae9cbb6
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_calc_mask.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_calc_mask.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_calc_mask.3.html#top_of_page)

```
       The acl_calc_mask() function calculates and sets the permissions
       associated with the ACL_MASK ACL entry of the ACL referred to by
       acl_p.  The value of the new permissions is the union of the
       permissions granted by all entries of tag type ACL_GROUP,
       ACL_GROUP_OBJ, or ACL_USER.  If the ACL referred to by acl_p
       already contains an ACL_MASK entry, its permissions are
       overwritten; if it does not contain an ACL_MASK entry, one is
       added.

       If the ACL referred to by acl_p does not contain enough space for
       the new ACL entry, then additional working storage may be
       allocated. If the working storage cannot be increased in the
       current location, then it may be relocated and the previous
       working storage is released and a pointer to the new working
       storage is returned via acl_p.

       The order of existing entries in the ACL is undefined after this
       function.

       Any existing ACL entry descriptors that refer to entries in the
       ACL continue to refer to those entries. Any existing ACL pointers
       that refer to the ACL referred to by acl_p continue to refer to
       the ACL.
```