---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-get--c2b06266
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_entry.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_entry.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_get_entry.3.html#top_of_page)

```
       The acl_get_entry() function obtains a descriptor for an ACL entry
       as specified by entry_id within the ACL indicated by the argument
       acl.  If the value of entry_id is ACL_FIRST_ENTRY, then the
       function returns in entry_p a descriptor for the first ACL entry
       within acl.  If the value of entry_id is ACL_NEXT_ENTRY, then the
       function returns in entry_p a descriptor for the next ACL entry
       within acl.

       If a call is made to acl_get_entry() with entry_id set to
       ACL_NEXT_ENTRY when there has not been either an initial
       successful call to acl_get_entry(), or a previous successful call
       to acl_get_entry() following a call to acl_calc_mask(),
       acl_copy_int(), acl_create_entry(), acl_delete_entry(), acl_dup(),
       acl_from_text(), acl_get_fd(), acl_get_file(), acl_set_fd(),
       acl_set_file(), or acl_valid(), then the effect is unspecified.

       Calls to acl_get_entry() do not modify any ACL entries. Subsequent
       operations using the returned ACL entry descriptor operate on the
       ACL entry within the ACL in working storage. The order of all
       existing entries in the ACL remains unchanged.  Any existing ACL
       entry descriptors that refer to entries within the ACL continue to
       refer to those entries. Any existing ACL pointers that refer to
       the ACL referred to by acl continue to refer to the ACL.
```