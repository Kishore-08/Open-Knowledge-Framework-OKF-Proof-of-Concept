---
id: linux-man-pages-notes-top-https-man7-org-linux-man-pages-man5-access-conf-5--7d01bebe
type: concept
title: NOTES         [top](https://man7.org/linux/man-pages/man5/access.conf.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/access.conf.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NOTES         [top](https://man7.org/linux/man-pages/man5/access.conf.5.html#top_of_page)

```
       The default separators of list items in a field are space, ',',
       and tabulator characters. Thus conveniently if spaces are put at
       the beginning and the end of the fields they are ignored. However
       if the list separator is changed with the listsep option, the
       spaces will become part of the actual item and the line will be
       most probably ignored. For this reason, it is not recommended to
       put spaces around the ':' characters.

       An IPv6 link local host address must contain the interface
       identifier. IPv6 link local network/netmask is not supported.

       Hostnames should be written as Fully-Qualified Host Name (FQHN) to
       avoid confusion with device names or PAM service names.
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man5/access.conf.5.html#top_of_page)

```
       pam_access(8), pam.d(5), pam(8)
```