---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-crea-f9904cb5
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_create_entry.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_create_entry.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_create_entry.3.html#top_of_page)

```
       The acl_create_entry() function creates a new ACL entry in the ACL
       pointed to by the contents of the pointer argument acl_p.  On
       success, the function returns a descriptor for the new ACL entry
       via entry_p.

       This function may cause memory to be allocated.  The caller should
       free any releasable memory, when the new ACL is no longer
       required, by calling acl_free(3) with (void*)*acl_p as an
       argument.  If the ACL working storage cannot be increased in the
       current location, then the working storage for the ACL pointed to
       by acl_p may be relocated and the previous working storage is
       released. A pointer to the new working storage is returned via
       acl_p.

       The components of the new ACL entry are initialized in the
       following ways: the ACL tag type component contains
       ACL_UNDEFINED_TAG, the qualifier component contains
       ACL_UNDEFINED_ID, and the set of permissions has no permissions
       enabled. Any existing ACL entry descriptors that refer to entries
       in the ACL continue to refer to those entries.
```