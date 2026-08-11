---
id: linux-man-pages-return-values-top-https-man7-org-linux-man-pages-man1-abicom-90d69f6f
type: concept
title: RETURN VALUES         [top](https://man7.org/linux/man-pages/man1/abicompat.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abicompat.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RETURN VALUES         [top](https://man7.org/linux/man-pages/man1/abicompat.1.html#top_of_page)

```
       The exit code of the abicompat command is either 0 if the ABI of
       the binaries being compared are equal, or non-zero if they differ
       or if the tool encountered an error.

       In the later case, the exit code is a 8-bits-wide bit field in
       which each bit has a specific meaning.

       The first bit, of value 1, named ABIDIFF_ERROR means there was an
       error.

       The second bit, of value 2, named ABIDIFF_USAGE_ERROR means there
       was an error in the way the user invoked the tool.  It might be
       set, for instance, if the user invoked the tool with an unknown
       command line switch, with a wrong number or argument, etc.  If
       this bit is set, then the ABIDIFF_ERROR bit must be set as well.

       The third bit, of value 4, named ABIDIFF_ABI_CHANGE means the ABI
       of the binaries being compared are different.

       The fourth bit, of value 8, named ABIDIFF_ABI_INCOMPATIBLE_CHANGE
       means the ABI of the binaries compared are different in an
       incompatible way.  If this bit is set, then the ABIDIFF_ABI_CHANGE
       bit must be set as well.  If the ABIDIFF_ABI_CHANGE is set and the
       ABIDIFF_INCOMPATIBLE_CHANGE is NOT set, then it means that the
       ABIs being compared might or might not be compatible.  In that
       case, a human being needs to review the ABI changes to decide if
       they are compatible or not.

       The remaining bits are not used for the moment.
```