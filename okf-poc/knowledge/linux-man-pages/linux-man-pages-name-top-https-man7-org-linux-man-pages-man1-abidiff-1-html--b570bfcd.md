---
id: linux-man-pages-name-top-https-man7-org-linux-man-pages-man1-abidiff-1-html--b570bfcd
type: concept
title: NAME         [top](https://man7.org/linux/man-pages/man1/abidiff.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidiff.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NAME         [top](https://man7.org/linux/man-pages/man1/abidiff.1.html#top_of_page)

```
       abidiff - compare ABIs of ELF files

       abidiff compares the Application Binary Interfaces (ABI) of two
       shared libraries in ELF format.  It emits a meaningful report
       describing the differences between the two ABIs.

       This tool can also compare the textual representations of the ABI
       of two ELF binaries (as emitted by abidw) or an ELF binary against
       a textual representation of another ELF binary.

       For a comprehensive ABI change report between two input shared
       libraries that includes changes about function and variable
       sub-types, abidiff uses by default, debug information in DWARF
       format, if present, otherwise it compares interfaces using debug
       information in CTF or BTF formats, if present. Finally, if no
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

## INVOCATION         [top](https://man7.org/linux/man-pages/man1/abidiff.1.html#top_of_page)

```
          abidiff [options] <first-shared-library> <second-shared-library>
```