---
id: linux-man-pages-examples-top-https-man7-org-linux-man-pages-man3-access-3p-h-91b2d582
type: concept
title: EXAMPLES         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/access.3p.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## EXAMPLES         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)

```
   Testing for the Existence of a File
       The following example tests whether a file named myfile exists in
       the /tmp directory.

           #include <unistd.h>
           ...
           int result;
           const char *pathname = "/tmp/myfile";

           result = access (pathname, F_OK);
```