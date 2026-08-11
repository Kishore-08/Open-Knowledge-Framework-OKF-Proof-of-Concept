---
id: linux-man-pages-options-top-https-man7-org-linux-man-pages-man1-abipkgdiff-1-1463afa5
type: concept
title: OPTIONS         [top](https://man7.org/linux/man-pages/man1/abipkgdiff.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abipkgdiff.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## OPTIONS         [top](https://man7.org/linux/man-pages/man1/abipkgdiff.1.html#top_of_page)

```
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

            Note that this option is turned on by default, unless we are
            in the presence of the Linux Kernel.

          • --btf
                This is used to compare packages with BTF debug
                information, if present.

          • --ctf
                This is used to compare packages with CTF debug
                information, if present.

          • --debug-info-pkg1 | --d1 <path>

            For cases where the debug information for package1 is split
            out into a separate file, tells abipkgdiff where to find that
            separate debug information package.

            Note that the debug info for package1 can have been split
            into several different debug info packages.  In that case,
            several instances of this options can be provided, along with
            those several different debug info packages.

          • --debug-info-pkg2 | --d2 <path>

            For cases where the debug information for package2 is split
            out into a separate file, tells abipkgdiff where to find that
            separate debug information package.

            Note that the debug info for package2 can have been split
            into several different debug info packages.  In that case,
            several instances of this options can be provided, along with
            those several different debug info packages.

          • --devel-pkg1 | --devel1 <path>

            Specifies where to find the Development Package associated
            with the first package to be compared.  That Development
            Package at path should at least contain header files in which
            public types exposed by the libraries (of the first package
            to be compared) are defined.  When this option is provided,
            the tool filters out reports about ABI changes to types that
            are NOT defined in these header files.

          • --devel-pkg2 | --devel2 <path>

            Specifies where to find the Development Package associated
            with the second package to be compared.  That Development
            Package at path should at least contains header files in
            which public types exposed by the libraries (of the second
            package to be compared) are defined.  When this option is
            provided, the tool filters out reports about ABI changes to
            types that are NOT defined in these header files.

          • --drop-private-types

            This option is to be used with the --devel-pkg1 and
            --devel-pkg2 options.  With this option, types that are NOT