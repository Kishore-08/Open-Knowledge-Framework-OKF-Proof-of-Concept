---
id: linux-man-pages-return-value-top-https-man7-org-linux-man-pages-man2-access--eb9e05c1
type: concept
title: RETURN VALUE         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man2/access.2.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RETURN VALUE         [top](https://man7.org/linux/man-pages/man2/access.2.html#top_of_page)

```
       On success (all requested permissions granted, or mode is F_OK and
       the file exists), zero is returned.  On error (at least one bit in
       mode asked for a permission that is denied, or mode is F_OK and
       the file does not exist, or some other error occurred), -1 is
       returned, and errno is set to indicate the error.
```