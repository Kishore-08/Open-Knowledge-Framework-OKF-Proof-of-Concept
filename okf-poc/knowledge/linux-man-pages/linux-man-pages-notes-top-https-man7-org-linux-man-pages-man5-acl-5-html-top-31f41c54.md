---
id: linux-man-pages-notes-top-https-man7-org-linux-man-pages-man5-acl-5-html-top-31f41c54
type: concept
title: NOTES         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acl.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NOTES         [top](https://man7.org/linux/man-pages/man5/acl.5.html#top_of_page)

```
   DENIED PERMISSIONS AND LINUX USER NAMESPACES
       While ACLs can be used to deny processes permissions based on the
       groups they are in, this is considered bad practice.  Privileged
       helpers such as newuidmap(1) can give unprivileged processes
       access to the setgroups(2) system call, which allows them to drop
       supplementary group membership and render restrictions based on
       that membership ineffective.  For further details, see
       user_namespaces(7).
```