---
id: linux-man-pages-options-top-https-man7-org-linux-man-pages-man1-abidiff-1-ht-b570bfcd
type: concept
title: OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidiff.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidiff.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidiff.1.html#top_of_page)

```
          • --add-binaries1 <bin1,bin2,bin3,..>

            For each of the comma-separated binaries given in argument to
            this option, if the binary is found in the directory
            specified by the --added-binaries-dir1 option, then abidiff
            loads the ABI corpus of the binary and adds it to a set of
            corpora (called an ABI Corpus Group) that includes the first
            argument of abidiff.

            That ABI corpus group is then compared against the second
            corpus group given in argument to abidiff.

          • --add-binaries2 <bin1,bin2,bin3,..>

            For each of the comma-separated binaries given in argument to
            this option, if the binary is found in the directory
            specified by the --added-binaries-dir2 option, then abidiff
            loads the ABI corpus of the binary and adds it to a set of
            corpora(called an ABI Corpus Group) that includes the second
            argument of abidiff.

            That ABI corpus group is then compared against the first
            corpus group given in argument to abidiff.

          • --added-binaries-dir1 | --abd1 <added-binaries-directory-1>

            This option is to be used in conjunction with the
            --add-binaries1, --follow-dependencies and
            --list-dependencies options.  Binaries referred to by these
            options, if found in the directory
            added-binaries-directory-1, are loaded as ABI corpus and are
            added to the first ABI corpus group that is to be used in the
            comparison.

          • --added-binaries-dir2 | --abd2 <added-binaries-directory-2>

            This option is to be used in conjunction with the
            --add-binaries2, --follow-dependencies and
            --list-dependencies options.  Binaries referred to by these
            options, if found in the directory
            added-binaries-directory-2, are loaded as ABI corpus and are
            added to the second ABI corpus group to be used in the
            comparison.

          • --added-fns

            In the resulting report about the differences between
            first-shared-library and second-shared-library, only display
            the globally defined functions that were added to
            second-shared-library.

          • --added-vars

            In the resulting report about the differences between
            first-shared-library and second-shared-library, only display
            the global variables that were added (defined) to
            second-shared-library.

          • --allow-non-exported-interfaces

            When looking at the debug information accompanying a binary,
            this tool analyzes the descriptions of the types reachable by
            the interfaces (functions and variables) that are visible
            outside of their translation unit.  Once that analysis is
            done, an ABI corpus is constructed by only considering the
            subset of types reachable from interfaces associated to ELF
            symbols that are defined and exported by the binary.  It's
            those final ABI Corpora that are compared by this tool.

            The problem with that approach however is that analyzing all
            the interfaces that are visible from outside their
            translation unit can amount to a lot of data, especially when
            those binaries are applications, as opposed to shared
            libraries.  One example of such applications is the Linux
            Kernel.  Analyzing massive ABI Corpora like these can be
            extremely slow.

            In the presence of an "average sized" binary however one can
            afford having libabigail analyze all interfaces that are
            visible outside of their translation unit, using this option.

            Note that