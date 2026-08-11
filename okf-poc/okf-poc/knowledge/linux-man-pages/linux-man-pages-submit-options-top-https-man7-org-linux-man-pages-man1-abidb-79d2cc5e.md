---
id: linux-man-pages-submit-options-top-https-man7-org-linux-man-pages-man1-abidb-79d2cc5e
type: concept
title: SUBMIT OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidb.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## SUBMIT OPTIONS         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)

```
          • --allow-no-debug-info

            By default, the program fails to submit a binary if its
            associated debug info could not be found.  With this option
            however if no debug info was found, then the ABI information
            submitted for the binary only comes from ELF symbols; the
            type information is omitted.

          • --archive | -Z .EXT[=CMD]

            Designate PATH names with a .EXT suffix to be treated as
            archives.  If CMD is present, pipe the PATH through the given
            shell command, otherwise pass as if through cat.  The
            resulting stream is then opened by libarchive, to enumerate
            the contents of a wide variety of possible archive file
            format.  Process each file in the archive individually into
            abixml.

            For example, -Z .zip will process each file in a zip file,
            and -Z .deb='dpkg-deb --fsys-tarfile' will process each
            payload file in a Debian archive.

          • --filter REGEX

            Limit files selected for abixml extraction to those that
            match the given regular expression.  The default is
            /lib.*\.so, as a heuristic to identify shared libraries.

          • --submit PATH1 PATH2 ...

            Using abidw, extract abixml for each of the listed files,
            generally shared libraries, subject to the filename filter
            and the archive decoding options.  Save the output of each
            abidw run into the selected distrobranch of the selected git
            repo.  If --submit and --check are both given, do submit
            operations first.

          • --sysroot PREFIX Specify the a prefix path that is to be
            removed from submitted file names.
```