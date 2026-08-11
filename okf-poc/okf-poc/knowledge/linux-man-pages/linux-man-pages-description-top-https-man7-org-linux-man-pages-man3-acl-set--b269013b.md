---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-acl-set--b269013b
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_set_permset.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_set_permset.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/acl_set_permset.3.html#top_of_page)

```
       The acl_set_permset() function sets the permission set of the ACL
       entry indicated by the argument entry_d to the permissions
       contained in the argument permset_d.

       Any ACL entry descriptors that refer to the entry containing the
       permission set referred to by permset_d shall continue to refer to
       those entries. Any ACL entry descriptors that refer to the entry
       referred to by entry_d shall continue to refer to that entry.
```