---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man1-ac-1-htm-16c19016
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man1/ac.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/ac.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man1/ac.1.html#top_of_page)

```
       ac prints out a report of connect time (in hours) based on the lo‐
       gins/logouts  in  the  current wtmp file.  A total is also printed
       out.

       The accounting file wtmp is maintained by  init(8)  and  login(1).
       Neither  ac nor login creates the wtmp if it doesn't exist, no ac‐
       counting is done.  To begin accounting, create  the  file  with  a
       length of zero.

       NOTE:   The  wtmp file can get really big, really fast.  You might
       want to trim it every once and a while.

       GNU ac works nearly the same UNIX ac, though it's a little smarter
       in several ways.  You should therefore expect differences  in  the
       output of GNU ac and the output of ac's on other systems.  Use the
       command info accounting to get additional information.
```