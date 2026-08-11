---
id: linux-man-pages-options-top-https-man7-org-linux-man-pages-man1-abicompat-1--90d69f6f
type: concept
title: OPTIONS         [top](https://man7.org/linux/man-pages/man1/abicompat.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abicompat.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## OPTIONS         [top](https://man7.org/linux/man-pages/man1/abicompat.1.html#top_of_page)

```
          • --help

            Display a short help about the command and exit.

          • --version | -v

            Display the version of the program and exit.

          • --list-undefined-symbols | -u

            Display the list of undefined symbols of the application and
            exit.

          • --show-base-names | -b

            In the resulting report emitted by the tool, this option
            makes the application and libraries be referred to by their
            base names only; not by a full absolute name.  This can be
            useful for use in scripts that wants to compare names of the
            application and libraries independently of what their
            directory names are.

          • --app-debug-info-dir | --appd
            <path-to-app-debug-info-directory>

            Set the path to the directory under which the debug
            information of the application is supposed to be laid out.
            This is useful for application binaries for which the debug
            info is in a separate set of files.

          • --lib-debug-info-dir1 | --libd1 <path-to-lib1-debug-info>

            Set the path to the directory under which the debug
            information of the first version of the shared library is
            supposed to be laid out.  This is useful for shared library
            binaries for which the debug info is in a separate set of
            files.

          • --lib-debug-info-dir2 | --libd2 <path-to-lib1-debug-info>

            Set the path to the directory under which the debug
            information of the second version of the shared library is
            supposed to be laid out.  This is useful for shared library
            binaries for which the debug info is in a separate set of
            files.

          • --suppressions | --suppr <path-to-suppressions>

            Use a suppression specification file located at
            path-to-suppressions.  Note that this option can appear
            multiple times on the command line; all the suppression
            specification files are then taken into account.

          • --no-show-locs
              Do not show information about where in the second shared
              library the respective type was changed.

          • --btf

            When comparing binaries, extract ABI information from BTF
            debug information, if present.

          • --ctf

            When comparing binaries, extract ABI information from CTF
            debug information, if present.

          • --fail-no-debug-info

            If no debug info was found, then this option makes the
            program to fail.  Otherwise, without this option, the program
            will attempt to compare properties of the binaries that are
            not related to debug info, like pure ELF properties.

          • --ignore-soname

            Ignore differences in the SONAME when doing a comparison

          • --weak-mode

            This triggers the weak mode of abicompat.  In this mode, only
            one version of the library is required.  That is, abicompat
            is invoked like this:

                abicompat --weak-mode <the-application> <the-library>

            Note that the --weak-mode option can even be omitted if only
            one version of the library is given, along with the
            application; in that case, abicompat automatically switches
            to operate in weak mode:

                abicompat <the-application> <the-library>

            In this weak mode, the types of functions and variables
            exported by the library and consumed by the application (as
            in, the symbols of the these functions and variables are
            undefined in the application and are defined and exported by
            the library) are compared to the version of these types as