---
id: linux-man-pages-name-top-https-man7-org-linux-man-pages-man1-abipkgdiff-1-ht-1463afa5
type: concept
title: NAME         [top](https://man7.org/linux/man-pages/man1/abipkgdiff.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abipkgdiff.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NAME         [top](https://man7.org/linux/man-pages/man1/abipkgdiff.1.html#top_of_page)

```
       abipkgdiff - compare ABIs of ELF files in software packages

       abipkgdiff compares the Application Binary Interfaces (ABI) of the
       ELF binaries contained in two sets of software packages.  The
       software package formats currently supported are Deb, RPM, tar
       archives (either compressed or not) and plain directories that
       contain binaries.

       The ABI of the binaries contained in the second set of packages is
       compared against the ABI of the binaries contained in the first
       set of packages.

       For a comprehensive ABI change report that includes changes about
       function and variable sub-types, the two input package sets must
       be accompanied with their debug information packages that contain
       debug information either in DWARF, CTF or in BTF formats.  Please
       note however that some packages contain binaries that embed the
       debug information directly in a section of said binaries.  In
       those cases, obviously, no separate debug information package is
       needed as the tool will find the debug information inside the
       binaries.

       By default, abipkgdiff uses debug information in DWARF format, if
       present, otherwise it compares binaries interfaces using debug
       information in CTF or in BTF formats, if present. Finally, if no
       debug info in these formats is found, it only considers ELF
       symbols and report about their addition or removal.

       This tool uses the libabigail library to analyze the binary as
       well as its associated debug information.  Here is its general
       mode of operation.

       When instructed to do so, a binary and its associated debug
       information is read and analyzed.  To that effect, libabigail
       analyzes by default the descriptions of the types reachable by the
       interfaces (functions and variables) that are visible outside of
       their translation unit.  Once that analysis is done, an
       Application Binary Interface Corpus is constructed by only
       considering the subset of types reachable from interfaces
       associated to ELF symbols that are defined and exported by the
       binary.  It's that final ABI corpus which libabigail considers as
       representing the ABI of the analyzed binary.

       Libabigail then has capabilities to generate textual
       representations of ABI Corpora, compare them, analyze their
       changes and report about them.
```