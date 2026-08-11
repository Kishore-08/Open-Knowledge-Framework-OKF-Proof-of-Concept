---
id: linux-man-pages-options-top-https-man7-org-linux-man-pages-man1-abidw-1-html-e6884ed0
type: concept
title: OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidw.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidw.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidw.1.html#top_of_page)

```
          • --abidiff
              Load the ABI of the ELF binary given in argument, save it
              in libabigail's XML format in a temporary file; read the
              ABI from the temporary XML file and compare the ABI that
              has been read back against the ABI of the ELF binary given
              in argument.  The ABIs should compare equal.  If they
              don't, the program emits a diagnostic and exits with a
              non-zero code.

              This is a debugging and sanity check option.

          • --abixml-version

            Display the version of the ABIXML format emitted by this
            program and exit.

          • --add-binaries <bin1,bin2,...>

            For each of the comma-separated binaries given in argument to
            this option, if the binary is found in the directory
            specified by the --added-binaries-dir option, then load the
            ABI corpus of the binary and add it to a set of ABI corpora
            (called a ABI Corpus Group) made of the binary denoted by the
            Argument of abidw.  That corpus group is then serialized out.

          • --added-binaries-dir | --abd <dir-path>

            This option is to be used in conjunction with the
            --add-binaries, the --follow-dependencies or the
            --list-dependencies option.  Binaries listed as arguments of
            the --add-binaries option or being dependencies of the input
            binary in the case of the --follow-dependencies option and
            found in the directory <dir-path> are going to be loaded as
            ABI corpus and added to the set of ABI corpora (called an ABI
            corpus group) built and serialized.

          • --allow-non-exported-interfaces

            When looking at the debug information accompanying a binary,
            this tool analyzes the descriptions of the types reachable by
            the interfaces (functions and variables) that are visible
            outside of their translation unit.  Once that analysis is
            done, an ABI corpus is constructed by only considering the
            subset of types reachable from interfaces associated to ELF
            symbols that are defined and exported by the binary.  It's
            that final ABI corpus which textual representation is saved
            as ABIXML.

            The problem with that approach however is that analyzing all
            the interfaces that are visible from outside their
            translation unit can amount to a lot of data, especially when
            those binaries are applications, as opposed to shared
            libraries.  One example of such applications is the Linux
            Kernel.  Analyzing massive ABI corpora like these can be
            extremely slow.

            In the presence of an "average sized" binary however one can
            afford having libabigail analyze all interfaces that are
            visible outside of their translation unit, using this option.

            Note that this option is turned on by default, unless we are
            in the presence of the Linux Kernel.

          • --annotate
              Annotate the ABIXML output with comments above most
              elements.  The comments are made of the pretty-printed form
              types, declaration or even ELF symbols.  The purpose is to
              make the ABIXML output more human-readable for debugging or
              documenting purposes.

          • --btf

            Extract ABI information from BTF debug information, if
            present in the given object.

          • --check-alternate-debug-info <elf-path>

            If the debug info for the file elf-path contains a reference
            to an alternate debug info file, abidw checks that it can
            find that alternate debug info file.  In that case, it emits