---
id: linux-man-pages-concept-e6faa7b6
type: concept
title: '|  |  |'
description: '|  |  |'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/acl_dup.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

|  |  |
| --- | --- |
| [man7.org](https://man7.org/index.html) > Linux > [man-pages](https://man7.org/linux/man-pages/index.html) | [Linux/UNIX system programming training](http://man7.org/training/) |

---



# acl\_dup(3) — Linux manual page

|  |
| --- |
| [NAME](https://man7.org/linux/man-pages/man3/acl_dup.3.html#NAME) | [LIBRARY](https://man7.org/linux/man-pages/man3/acl_dup.3.html#LIBRARY) | [SYNOPSIS](https://man7.org/linux/man-pages/man3/acl_dup.3.html#SYNOPSIS) | [DESCRIPTION](https://man7.org/linux/man-pages/man3/acl_dup.3.html#DESCRIPTION) | [RETURN VALUE](https://man7.org/linux/man-pages/man3/acl_dup.3.html#RETURN_VALUE) | [ERRORS](https://man7.org/linux/man-pages/man3/acl_dup.3.html#ERRORS) | [STANDARDS](https://man7.org/linux/man-pages/man3/acl_dup.3.html#STANDARDS) | [SEE ALSO](https://man7.org/linux/man-pages/man3/acl_dup.3.html#SEE_ALSO) | [AUTHOR](https://man7.org/linux/man-pages/man3/acl_dup.3.html#AUTHOR) | [COLOPHON](https://man7.org/linux/man-pages/man3/acl_dup.3.html#COLOPHON) |
|  |

```
ACL_DUP(3)               Library Functions Manual              ACL_DUP(3)
```

## NAME         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)

```
       acl_dup — duplicate an ACL
```

## LIBRARY         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)

```
       Linux Access Control Lists library (libacl, -lacl).
```

## SYNOPSIS         [top](https://man7.org/linux/man-pages/man3/acl_dup.3.html#top_of_page)

```
       <sys/types.h> <sys/acl.h> acl_t acl_dup(acl_t acl)
```