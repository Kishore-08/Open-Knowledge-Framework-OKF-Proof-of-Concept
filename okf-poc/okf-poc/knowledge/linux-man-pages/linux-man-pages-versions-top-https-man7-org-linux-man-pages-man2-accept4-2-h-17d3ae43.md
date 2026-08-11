---
id: linux-man-pages-versions-top-https-man7-org-linux-man-pages-man2-accept4-2-h-17d3ae43
type: concept
title: VERSIONS         [top](https://man7.org/linux/man-pages/man2/accept4.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/accept4.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## VERSIONS         [top](https://man7.org/linux/man-pages/man2/accept4.2.html#top_of_page)

```
       On Linux, the new socket returned by accept() does not inherit
       file status flags such as O_NONBLOCK and O_ASYNC from the
       listening socket.  This behavior differs from the canonical BSD
       sockets implementation.  Portable programs should not rely on
       inheritance or noninheritance of file status flags and always
       explicitly set all required flags on the socket returned from
       accept().
```

## STANDARDS         [top](https://man7.org/linux/man-pages/man2/accept4.2.html#top_of_page)

```
       POSIX.1-2024.
```