---
id: linux-man-pages-synopsis-top-https-man7-org-linux-man-pages-man3-access-3p-h-91b2d582
type: concept
title: SYNOPSIS         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/access.3p.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## SYNOPSIS         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)

```
       #include <unistd.h>

       int access(const char *path, int amode);

       #include <fcntl.h>

       int faccessat(int fd, const char *path, int amode, int flag);
```