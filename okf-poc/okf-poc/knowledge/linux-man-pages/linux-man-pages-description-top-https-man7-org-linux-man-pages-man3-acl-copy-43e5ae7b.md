---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-copy-43e5ae7b
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_copy_ext.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_copy_ext.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_copy_ext.3.html#top_of_page)

```
       The acl_copy_ext() function copies the ACL pointed to by acl from
       system-managed space to the user managed space pointed to by
       buf_p.  The size parameter represents the size in bytes of the
       buffer pointed to by buf_p.  The format of the ACL placed in the
       buffer pointed to by buf_p is a contiguous, persistent data item,
       the format of which is unspecified.  It is the responsibility of
       the invoker to allocate an area large enough to hold the copied
       ACL. The size of the exportable, contiguous, persistent form of
       the ACL may be obtained by invoking the acl_size() function.

       Any ACL entry descriptors that refer to an entry in the ACL
       referenced by acl continue to refer to those entries. Any existing
       ACL pointers that refer to the ACL referenced by acl continue to
       refer to the ACL.
```