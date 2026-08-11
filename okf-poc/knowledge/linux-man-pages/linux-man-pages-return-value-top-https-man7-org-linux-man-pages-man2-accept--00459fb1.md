---
id: linux-man-pages-return-value-top-https-man7-org-linux-man-pages-man2-accept--00459fb1
type: concept
title: RETURN VALUE         [top](https://man7.org/linux/man-pages/man2/accept.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/accept.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RETURN VALUE         [top](https://man7.org/linux/man-pages/man2/accept.2.html#top_of_page)

```
       On success, these system calls return a file descriptor for the
       accepted socket (a nonnegative integer).  On error, -1 is
       returned, errno is set to indicate the error, and addrlen is left
       unchanged.

   Error handling
       Linux accept() (and accept4()) passes already-pending network
       errors on the new socket as an error code from accept().  This
       behavior differs from other BSD socket implementations.  For
       reliable operation the application should detect the network
       errors defined for the protocol after accept() and treat them like
       EAGAIN by retrying.  In the case of TCP/IP, these are ENETDOWN,
       EPROTO, ENOPROTOOPT, EHOSTDOWN, ENONET, EHOSTUNREACH, EOPNOTSUPP,
       and ENETUNREACH.
```