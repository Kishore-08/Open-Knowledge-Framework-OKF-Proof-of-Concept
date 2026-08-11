---
id: linux-man-pages-environment-top-https-man7-org-linux-man-pages-man1-abipkgdi-1463afa5
type: concept
title: ENVIRONMENT         [top](https://man7.org/linux/man-pages/man1/abipkgdiff.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abipkgdiff.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## ENVIRONMENT         [top](https://man7.org/linux/man-pages/man1/abipkgdiff.1.html#top_of_page)

```
       abipkgdiff loads two default suppression specifications files,
       merges their content and use it to filter out ABI change reports
       that might be considered as false positives to users.

       • Default system-wide suppression specification file

         It's located by the optional environment variable
         LIBABIGAIL_DEFAULT_SYSTEM_SUPPRESSION_FILE.  If that environment
         variable is not set, then abipkgdiff tries to load the
         suppression file $libdir/libabigail/libabigail-default.abignore.
         If that file is not present, then no default system-wide
         suppression specification file is loaded.

       • Default user suppression specification file.

         It's located by the optional environment
         LIBABIGAIL_DEFAULT_USER_SUPPRESSION_FILE.  If that environment
         variable is not set, then abipkgdiff tries to load the
         suppression file $HOME/.abignore.  If that file is not present,
         then no default user suppression specification is loaded.

       In addition to those default suppression specification files,
       abipkgdiff will also look inside the packages being compared and
       if it sees a file that ends with the extension .abignore, then it
       will consider it as a suppression specification and it will
       combine it to the default suppression specification that might be
       already loaded.

       The user might as well use the --suppressions option (that is
       documented further below) to provide a suppression specification.
```