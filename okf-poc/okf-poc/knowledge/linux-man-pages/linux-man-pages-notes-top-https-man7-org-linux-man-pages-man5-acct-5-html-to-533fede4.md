---
id: linux-man-pages-notes-top-https-man7-org-linux-man-pages-man5-acct-5-html-to-533fede4
type: concept
title: NOTES         [top](https://man7.org/linux/man-pages/man5/acct.5.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man5/acct.5.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NOTES         [top](https://man7.org/linux/man-pages/man5/acct.5.html#top_of_page)

```
       Records in the accounting file are ordered by termination time of
       the process.

       Up to and including Linux 2.6.9, a separate accounting record is
       written for each thread created using the NPTL threading library;
       since Linux 2.6.10, a single accounting record is written for the
       entire process on termination of the last thread in the process.

       The /proc/sys/kernel/acct file, described in proc(5), defines
       settings that control the behavior of process accounting when disk
       space runs low.
```

## SEE ALSO         [top](https://man7.org/linux/man-pages/man5/acct.5.html#top_of_page)

```
       lastcomm(1), acct(2), accton(8), sa(8)
```