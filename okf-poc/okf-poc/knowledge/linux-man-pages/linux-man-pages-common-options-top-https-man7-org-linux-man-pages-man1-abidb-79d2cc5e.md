---
id: linux-man-pages-common-options-top-https-man7-org-linux-man-pages-man1-abidb-79d2cc5e
type: concept
title: COMMON OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidb.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## COMMON OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)

```
          • --abicompat PATH

            Specify the path to the abicompat program to use.  By
            default, in the absence of this option, the abicompat program
            found in directories listed in the $PATH environment is used.

          • --abidw PATH

            Specify the path to the abidw program to use.  By default, in
            the absence of this option, the abidw program found in
            directories listed in the $PATH environment is used.

          • --distrobranch BRANCH

            Specify the git branch for the abixml files in the git repo.
            The default is a string like DISTRO/VERSION/ARCHITECTURE,
            computed from the running environment.

          • --git REPO

            Specify the preexisting git working tree for abidb to submit
            to or check against.  The default is the current working
            directory.  It may be used concurrently by multiple "check"
            operations, but only one "submit" operation.

          • --help | -h

            Display a short help about the command and exit.

          • --loglevel LOGLEVEL

            Specify the diagnostic level for messages to stderr.  One of
            debug, info, warning, error, or critical; case-insensitive.
            The default is info.

          • --timeout SECONDS

            Specify a maximum limit to the execution time (in seconds)
            allowed for the abidw and abicompat programs that are
            executed.  By default, no limit is set for the execution time
            of these programs.
```