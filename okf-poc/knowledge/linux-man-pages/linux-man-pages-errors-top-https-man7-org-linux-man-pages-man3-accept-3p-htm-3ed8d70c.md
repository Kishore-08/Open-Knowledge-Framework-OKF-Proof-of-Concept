---
id: linux-man-pages-errors-top-https-man7-org-linux-man-pages-man3-accept-3p-htm-3ed8d70c
type: concept
title: ERRORS         [top](https://man7.org/linux/man-pages/man3/accept.3p.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/accept.3p.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ERRORS         [top](https://man7.org/linux/man-pages/man3/accept.3p.html#top_of_page)

```
       The accept() function shall fail if:

       EAGAIN or EWOULDBLOCK
              O_NONBLOCK is set for the socket file descriptor and no
              connections are present to be accepted.

       EBADF  The socket argument is not a valid file descriptor.

       ECONNABORTED
              A connection has been aborted.

       EINTR  The accept() function was interrupted by a signal that was
              caught before a valid connection arrived.

       EINVAL The socket is not accepting connections.

       EMFILE All file descriptors available to the process are currently
              open.

       ENFILE The maximum number of file descriptors in the system are
              already open.

       ENOBUFS
              No buffer space is available.

       ENOMEM There was insufficient memory available to complete the
              operation.

       ENOTSOCK
              The socket argument does not refer to a socket.

       EOPNOTSUPP
              The socket type of the specified socket does not support
              accepting connections.

       The accept() function may fail if:

       EPROTO A protocol error has occurred; for example, the STREAMS
              protocol stack has not been initialized.

       The following sections are informative.
```

## EXAMPLES         [top](https://man7.org/linux/man-pages/man3/accept.3p.html#top_of_page)

```
       None.
```