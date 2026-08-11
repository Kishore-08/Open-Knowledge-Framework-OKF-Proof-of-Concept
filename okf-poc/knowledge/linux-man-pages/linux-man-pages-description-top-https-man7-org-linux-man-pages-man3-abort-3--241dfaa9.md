---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-abort-3--241dfaa9
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/abort.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)

```
       The abort() function first unblocks the SIGABRT signal, and then
       raises that signal for the calling process (as though raise(3) was
       called).  This results in the abnormal termination of the process
       unless the SIGABRT signal is caught and the signal handler does
       not return (see longjmp(3)).

       If the SIGABRT signal is ignored, or caught by a handler that
       returns, the abort() function will still terminate the process.
       It does this by restoring the default disposition for SIGABRT and
       then raising the signal for a second time.

       As with other cases of abnormal termination the functions
       registered with atexit(3) and on_exit(3) are not called.
```

## RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)

```
       The abort() function never returns.
```