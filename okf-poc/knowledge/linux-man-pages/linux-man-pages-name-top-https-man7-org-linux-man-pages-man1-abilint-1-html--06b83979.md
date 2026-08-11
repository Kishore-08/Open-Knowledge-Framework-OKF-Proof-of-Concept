---
id: linux-man-pages-name-top-https-man7-org-linux-man-pages-man1-abilint-1-html--06b83979
type: concept
title: NAME         [top](https://man7.org/linux/man-pages/man1/abilint.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abilint.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NAME         [top](https://man7.org/linux/man-pages/man1/abilint.1.html#top_of_page)

```
       abilint - validate an abigail ABI representation

       abilint parses the native XML representation of an ABI as emitted
       by abidw.  Once it has parsed the XML representation of the ABI,
       abilint builds and in-memory model from it.  It then tries to save
       it back to an XML form, to standard output.  If that read-write
       operation succeeds chances are the input XML ABI representation is
       meaningful.

       Note that the main intent of this tool to help debugging issues in
       the underlying Libabigail library.

       Note also that abilint can also read an ELF input file, build the
       in-memory model for its ABI, and serialize that model back into
       XML to standard output.  In that case, the ELF input file must be
       accompanied with its debug information in the DWARF format.
```

## INVOCATION         [top](https://man7.org/linux/man-pages/man1/abilint.1.html#top_of_page)

```
          abilint [options] [<abi-file1>]
```