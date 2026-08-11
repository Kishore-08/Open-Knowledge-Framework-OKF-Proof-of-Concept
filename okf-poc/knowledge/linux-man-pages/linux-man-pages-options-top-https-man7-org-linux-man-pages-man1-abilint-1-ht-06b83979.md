---
id: linux-man-pages-options-top-https-man7-org-linux-man-pages-man1-abilint-1-ht-06b83979
type: concept
title: OPTIONS         [top](https://man7.org/linux/man-pages/man1/abilint.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abilint.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## OPTIONS         [top](https://man7.org/linux/man-pages/man1/abilint.1.html#top_of_page)

```
          • --annotate

            Annotate the ABIXML output with comments above most elements.
            The comments are made of the pretty-printed form of types,
            declaration or even ELF symbols.  The purpose is to make the
            ABIXML output more human-readable for debugging or
            documenting purposes.

          • --ctf

            Extract ABI information from CTF debug information, if
            present in the given object.

          • --debug-info-dir <path>

            When reading an ELF input file which debug information is
            split out into a separate file, this options tells abilint
            where to find that separate debug information file.

            Note that path must point to the root directory under which
            the debug information is arranged in a tree-like manner.
            Under Red Hat based systems, that directory is usually
            <root>/usr/lib/debug.

            Note also that this option is not mandatory for split debug
            information installed by your system's package manager
            because then abidiff knows where to find it.

          • --diff

            For XML inputs, perform a text diff between the input and the
            memory model saved back to disk.  This can help to spot
            issues in the handling of the XML format by the underlying
            Libabigail library.

          • --header-file | --hf <header-file-path>

            Specifies where to find one of the public headers of the abi
            file that the tool has to consider.  The tool will thus
            filter out types that are not defined in public headers.

          • --headers-dir | --hd <headers-directory-path-1>

            Specifies where to find the public headers of the first
            shared library that the tool has to consider.  The tool will
            thus filter out types that are not defined in public headers.

          • --help

            Display a short help message and exits.

          • --noout

            Do not display anything on standard output.  The return code
            of the command is the only way to know if the command
            succeeded.

          • --suppressions | suppr
            <path-to-suppression-specifications-file>

            Use a suppression specification file located at
            path-to-suppression-specifications-file.  Note that this
            option can appear multiple times on the command line.  In
            that case, all of the provided suppression specification
            files are taken into account.  ABI artifacts matched by the
            suppression specifications are suppressed from the output of
            this tool.

          • --stdin | --

            Read the input content from standard input.

          • --tu

            Expect the input XML to represent a single translation unit.

          • --verbose

            Shows verbose messages about internal stuff.  This is used to
            debug the tool and its underlying library.

          • --version | -v

            Display the version of the program and exit.
```

## AUTHOR         [top](https://man7.org/linux/man-pages/man1/abilint.1.html#top_of_page)

```
       Dodji Seketeli
```

## COPYRIGHT         [top](https://man7.org/linux/man-pages/man1/abilint.1.html#top_of_page)

```
       2014-2025, Red Hat, Inc.
```