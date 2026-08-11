---
id: linux-man-pages-notes-top-https-man7-org-linux-man-pages-man2-accept4-2-html-17d3ae43
type: concept
title: NOTES         [top](https://man7.org/linux/man-pages/man2/accept4.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/accept4.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NOTES         [top](https://man7.org/linux/man-pages/man2/accept4.2.html#top_of_page)

```
       There may not always be a connection waiting after a SIGIO is
       delivered or select(2), poll(2), or epoll(7) return a readability
       event because the connection might have been removed by an
       asynchronous network error or another thread before accept() is
       called.  If this happens, then the call will block waiting for the
       next connection to arrive.  To ensure that accept() never blocks,
       the passed socket sockfd needs to have the O_NONBLOCK flag set
       (see socket(7)).

       For certain protocols which require an explicit confirmation, such
       as DECnet, accept() can be thought of as merely dequeuing the next
       connection request and not implying confirmation.  Confirmation
       can be implied by a normal read or write on the new file
       descriptor, and rejection can be implied by closing the new
       socket.  Currently, only DECnet has these semantics on Linux.

   The socklen_t type
       In the original BSD sockets implementation (and on other older
       systems) the third argument of accept() was declared as an int *.
       A POSIX.1g draft standard wanted to change it into a size_t *;
       later POSIX standards and glibc 2.x have socklen_t * .
```

## EXAMPLES         [top](https://man7.org/linux/man-pages/man2/accept4.2.html#top_of_page)

```
       See bind(2).
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man2/accept4.2.html#top_of_page)

```
       bind(2), connect(2), listen(2), select(2), socket(2), socket(7)
```