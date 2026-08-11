---
id: linux-man-pages-description-top-https-man7-org-linux-man-pages-man3-abort-3p-6d6a8ef0
type: concept
title: DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/abort.3p.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/abort.3p.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## DESCRIPTION         [top](https://man7.org/linux/man-pages/man3/abort.3p.html#top_of_page)

```
       The functionality described on this reference page is aligned with
       the ISO C standard. Any conflict between the requirements
       described here and the ISO C standard is unintentional. This
       volume of POSIX.1‐2017 defers to the ISO C standard.

       The abort() function shall cause abnormal process termination to
       occur, unless the signal SIGABRT is being caught and the signal
       handler does not return.

       The abnormal termination processing shall include the default
       actions defined for SIGABRT and may include an attempt to effect
       fclose() on all open streams.

       The SIGABRT signal shall be sent to the calling process as if by
       means of raise() with the argument SIGABRT.

       The status made available to wait(), waitid(), or waitpid() by
       abort() shall be that of a process terminated by the SIGABRT
       signal.  The abort() function shall override blocking or ignoring
       the SIGABRT signal.
```

## RETURN VALUE         [top](https://man7.org/linux/man-pages/man3/abort.3p.html#top_of_page)

```
       The abort() function shall not return.
```

## ERRORS         [top](https://man7.org/linux/man-pages/man3/abort.3p.html#top_of_page)

```
       No errors are defined.

       The following sections are informative.
```

## EXAMPLES         [top](https://man7.org/linux/man-pages/man3/abort.3p.html#top_of_page)

```
       None.
```