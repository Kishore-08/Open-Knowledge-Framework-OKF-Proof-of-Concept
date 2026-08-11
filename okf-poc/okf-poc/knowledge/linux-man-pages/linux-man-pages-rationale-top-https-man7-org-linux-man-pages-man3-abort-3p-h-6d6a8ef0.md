---
id: linux-man-pages-rationale-top-https-man7-org-linux-man-pages-man3-abort-3p-h-6d6a8ef0
type: concept
title: RATIONALE         [top](https://man7.org/linux/man-pages/man3/abort.3p.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/abort.3p.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RATIONALE         [top](https://man7.org/linux/man-pages/man3/abort.3p.html#top_of_page)

```
       The ISO/IEC 9899:1999 standard requires the abort() function to be
       async-signal-safe. Since POSIX.1‐2008 defers to the ISO C
       standard, this required a change to the DESCRIPTION from ``shall
       include the effect of fclose()'' to ``may include an attempt to
       effect fclose().''

       The revised wording permits some backwards-compatibility and
       avoids a potential deadlock situation.

       The Open Group Base Resolution bwg2002‐003 is applied, removing
       the following XSI shaded paragraph from the DESCRIPTION:

       ``On XSI-conformant systems, in addition the abnormal termination
       processing shall include the effect of fclose() on message catalog
       descriptors.''

       There were several reasons to remove this paragraph:

        *  No special processing of open message catalogs needs to be
           performed prior to abnormal process termination.

        *  The main reason to specifically mention that abort() includes
           the effect of fclose() on open streams is to flush output
           queued on the stream. Message catalogs in this context are
           read-only and, therefore, do not need to be flushed.

        *  The effect of fclose() on a message catalog descriptor is
           unspecified. Message catalog descriptors are allowed, but not
           required to be implemented using a file descriptor, but there
           is no mention in POSIX.1‐2008 of a message catalog descriptor
           using a standard I/O stream FILE object as would be expected
           by fclose().
```

## FUTURE DIRECTIONS         [top](https://man7.org/linux/man-pages/man3/abort.3p.html#top_of_page)

```
       None.
```