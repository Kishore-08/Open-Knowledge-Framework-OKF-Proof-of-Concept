---
id: linux-man-pages-history-top-https-man7-org-linux-man-pages-man3-abort-3-html-241dfaa9
type: concept
title: HISTORY         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/abort.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## HISTORY         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)

```
       SVr4, POSIX.1-2001, 4.3BSD, C89.

       Up until glibc 2.26, if the abort() function caused process
       termination, all open streams were closed and flushed (as with
       fclose(3)).  However, in some cases this could result in deadlocks
       and data corruption.  Therefore, starting with glibc 2.27, abort()
       terminates the process without flushing streams.  POSIX.1 permits
       either possible behavior, saying that abort() "may include an
       attempt to effect fclose() on all open streams".
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)

```
       gdb(1), sigaction(2), assert(3), exit(3), longjmp(3), raise(3)
```