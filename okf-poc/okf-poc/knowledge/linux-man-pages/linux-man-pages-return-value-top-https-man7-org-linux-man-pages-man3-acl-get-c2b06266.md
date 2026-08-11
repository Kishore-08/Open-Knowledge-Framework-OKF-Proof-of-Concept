---
id: linux-man-pages-return-value-top-https-man7-org-linux-man-pages-man3-acl-get-c2b06266
type: concept
title: RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/acl_get_entry.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_get_entry.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/acl_get_entry.3.html#top_of_page)

```
       If the function successfully obtains an ACL entry, the function
       returns a value of 1.  If the ACL has no ACL entries, the function
       returns the value 0.  If the value of entry_id is ACL_NEXT_ENTRY
       and the last ACL entry in the ACL has already been returned by a
       previous call to acl_get_entry(), the function returns the value 0
       until a successful call with an entry_id of ACL_FIRST_ENTRY is
       made. Otherwise, the value -1 is returned and errno is set to
       indicate the error.
```