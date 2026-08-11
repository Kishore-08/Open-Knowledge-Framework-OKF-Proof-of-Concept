---
id: linux-man-pages-name-top-https-man7-org-linux-man-pages-man1-abidw-1-html-to-e6884ed0
type: concept
title: NAME         [top](https://man7.org/linux/man-pages/man1/abidw.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidw.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NAME         [top](https://man7.org/linux/man-pages/man1/abidw.1.html#top_of_page)

```
       abidw - serialize the ABI of an ELF file

       abidw reads a shared library in ELF format and emits an XML
       representation of its ABI to standard output.  The emitted
       representation format, named ABIXML, includes all the globally
       defined functions and variables, along with a complete
       representation of their types.  It also includes a representation
       of the globally defined ELF symbols of the file.

       When given the --linux-tree option, this program can also handle a
       Linux kernel tree.  That is, a directory tree that contains both
       the vmlinux binary and Linux Kernel modules.  It analyses those ‐
       Linux Kernel binaries and emits an XML representation of the
       interface between the kernel and its module, to standard output.
       In this case, we don't call it an ABI, but a KMI (Kernel Module
       Interface).  The emitted KMI includes all the globally defined
       functions and variables, along with a complete representation of
       their types.

       To generate either ABI or KMI representation, by default abidw
       uses debug information in the DWARF format, if present, otherwise
       it looks for debug information in CTF or BTF formats, if present.
       Finally, if no debug info in these formats is found, it only
       considers ELF symbols and report about their addition or removal.

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

## INVOCATION         [top](https://man7.org/linux/man-pages/man1/abidw.1.html#top_of_page)

```
          abidw [options] [<path-to-elf-file>]
```