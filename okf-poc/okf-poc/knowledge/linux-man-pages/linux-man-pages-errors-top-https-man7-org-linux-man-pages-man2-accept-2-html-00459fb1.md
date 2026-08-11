---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man2-accept-2-html-00459fb1
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man2/accept.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/accept.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man2/accept.2.html#top_of_page)

```
       EAGAIN or EWOULDBLOCK
              The socket is marked nonblocking and no connections are
              present to be accepted.  POSIX.1-2001 and POSIX.1-2008
              allow either error to be returned for this case, and do not
              require these constants to have the same value, so a
              portable application should check for both possibilities.

       EBADF  sockfd is not an open file descriptor.

       ECONNABORTED
              A connection has been aborted.

       EFAULT The addr argument is not in a writable part of the user
              address space.

       EINTR  The system call was interrupted by a signal that was caught
              before a valid connection arrived; see signal(7).

       EINVAL Socket is not listening for connections, or addrlen is
              invalid (e.g., is negative).

       EINVAL (accept4()) invalid value in flags.

       EMFILE The per-process limit on the number of open file
              descriptors has been reached.

       ENFILE The system-wide limit on the total number of open files has
              been reached.

       ENOBUFS
       ENOMEM Not enough free memory.  This often means that the memory
              allocation is limited by the socket buffer limits, not by
              the system memory.

       ENOTSOCK
              The file descriptor sockfd does not refer to a socket.

       EOPNOTSUPP
              The referenced socket is not of type SOCK_STREAM.

       EPERM  Firewall rules forbid connection.

       EPROTO Protocol error.

       In addition, network errors for the new socket and as defined for
       the protocol may be returned.  Various Linux kernels can return
       other errors such as ENOSR, ESOCKTNOSUPPORT, EPROTONOSUPPORT,
       ETIMEDOUT.  The value ERESTARTSYS may be seen during a trace.
```