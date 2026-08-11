---
id: linux-man-pages-rationale-top-https-man7-org-linux-man-pages-man3-access-3p--91b2d582
type: concept
title: RATIONALE         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man3/access.3p.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## RATIONALE         [top](https://man7.org/linux/man-pages/man3/access.3p.html#top_of_page)

```
       In early proposals, some inadequacies in the access() function led
       to the creation of an eaccess() function because:

        1. Historical implementations of access() do not test file access
           correctly when the process' real user ID is superuser. In
           particular, they always return zero when testing execute
           permissions without regard to whether the file is executable.

        2. The superuser has complete access to all files on a system. As
           a consequence, programs started by the superuser and switched
           to the effective user ID with lesser privileges cannot use
           access() to test their file access permissions.

       However, the historical model of eaccess() does not resolve
       problem (1), so this volume of POSIX.1‐2017 now allows access() to
       behave in the desired way because several implementations have
       corrected the problem. It was also argued that problem (2) is more
       easily solved by using open(), chdir(), or one of the exec
       functions as appropriate and responding to the error, rather than
       creating a new function that would not be as reliable. Therefore,
       eaccess() is not included in this volume of POSIX.1‐2017.

       The sentence concerning appropriate privileges and execute
       permission bits reflects the two possibilities implemented by
       historical implementations when checking superuser access for
       X_OK.

       New implementations are discouraged from returning X_OK unless at
       least one execution permission bit is set.

       The purpose of the faccessat() function is to enable the checking
       of the accessibility of files in directories other than the
       current working directory without exposure to race conditions. Any
       part of the path of a file could be changed in parallel to a call
       to access(), resulting in unspecified behavior. By opening a file
       descriptor for the target directory and using the faccessat()
       function it can be guaranteed that the file tested for
       accessibility is located relative to the desired directory.
```