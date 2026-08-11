---
id: linux-man-pages-changes-to-the-file-utilities-top-https-man7-org-linux-man-p-31f41c54
type: concept
title: CHANGES TO THE FILE UTILITIES         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## CHANGES TO THE FILE UTILITIES         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
       On a system that supports ACLs, the file utilities ls(1), cp(1),
       and mv(1) change their behavior in the following way:

       •   For files that have a default ACL or an access ACL that
           contains more than the three required ACL entries, the ls(1)
           utility in the long form produced by ls -l displays a plus
           sign (+) after the permission string.

       •   If the -p flag is specified, the cp(1) utility also preserves
           ACLs.  If this is not possible, a warning is produced.

       •     The mv(1) utility always preserves ACLs. If this is not
           possible, a warning is produced.

       The effect of the chmod(1) utility, and of the chmod(2) system
       call, on the access ACL is described in “CORRESPONDENCE BETWEEN
       ACL ENTRIES AND FILE PERMISSION BITS”.
```