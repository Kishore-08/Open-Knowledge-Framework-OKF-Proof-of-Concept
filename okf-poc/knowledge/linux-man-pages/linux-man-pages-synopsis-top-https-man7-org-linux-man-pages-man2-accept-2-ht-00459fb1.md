---
id: linux-man-pages-synopsis-top-https-man7-org-linux-man-pages-man2-accept-2-ht-00459fb1
type: concept
title: SYNOPSIS         [top](https://man7.org/linux/man-pages/man2/accept.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/accept.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## SYNOPSIS         [top](https://man7.org/linux/man-pages/man2/accept.2.html#top_of_page)

```
       #include <sys/socket.h>

       int accept(int sockfd, struct sockaddr *_Nullable restrict addr,
                  socklen_t *_Nullable restrict addrlen);

       #define _GNU_SOURCE             /* See feature_test_macros(7) */
       #include <sys/socket.h>

       int accept4(int sockfd, struct sockaddr *_Nullable restrict addr,
                  socklen_t *_Nullable restrict addrlen, int flags);
```