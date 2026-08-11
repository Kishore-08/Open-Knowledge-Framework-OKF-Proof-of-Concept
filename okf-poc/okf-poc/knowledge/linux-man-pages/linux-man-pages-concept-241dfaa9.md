---
id: linux-man-pages-concept-241dfaa9
type: concept
title: '|  |  |'
description: '|  |  |'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/abort.3.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

|  |  |
| --- | --- |
| [man7.org](https://man7.org/index.html) > Linux > [man-pages](https://man7.org/linux/man-pages/index.html) | [Linux/UNIX system programming training](http://man7.org/training/) |

---



# abort(3) — Linux manual page

|  |
| --- |
| [NAME](https://man7.org/linux/man-pages/man3/abort.3.html#NAME) | [LIBRARY](https://man7.org/linux/man-pages/man3/abort.3.html#LIBRARY) | [SYNOPSIS](https://man7.org/linux/man-pages/man3/abort.3.html#SYNOPSIS) | [DESCRIPTION](https://man7.org/linux/man-pages/man3/abort.3.html#DESCRIPTION) | [RETURN VALUE](https://man7.org/linux/man-pages/man3/abort.3.html#RETURN_VALUE) | [ATTRIBUTES](https://man7.org/linux/man-pages/man3/abort.3.html#ATTRIBUTES) | [STANDARDS](https://man7.org/linux/man-pages/man3/abort.3.html#STANDARDS) | [HISTORY](https://man7.org/linux/man-pages/man3/abort.3.html#HISTORY) | [SEE ALSO](https://man7.org/linux/man-pages/man3/abort.3.html#SEE_ALSO) | [COLOPHON](https://man7.org/linux/man-pages/man3/abort.3.html#COLOPHON) |
|  |

```
abort(3)                 Library Functions Manual                abort(3)
```

## NAME         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)

```
       abort - cause abnormal process termination
```

## LIBRARY         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)

```
       Standard C library (libc, -lc)
```

## SYNOPSIS         [top](https://man7.org/linux/man-pages/man3/abort.3.html#top_of_page)

```
       #include <stdlib.h>

       [[noreturn]] void abort(void);
```