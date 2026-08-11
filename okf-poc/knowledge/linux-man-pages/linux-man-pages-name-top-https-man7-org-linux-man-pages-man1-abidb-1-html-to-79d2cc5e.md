---
id: linux-man-pages-name-top-https-man7-org-linux-man-pages-man1-abidb-1-html-to-79d2cc5e
type: concept
title: NAME         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidb.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## NAME         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)

```
       abidb - check binary against abixml corpus and/or submit new data

       abidb manages a git repository of abixml files describing shared
       libraries, and checks binaries against them.  elfutils and
       libabigail programs are used to query and process the binaries.
       abidb works well with debuginfod to fetch needed DWARF content
       automatically.
```

## INVOCATION         [top](https://man7.org/linux/man-pages/man1/abidb.1.html#top_of_page)

```
          abidb [OPTIONS] [--submit PATH1 PATH2 ...] [--check PATH1 PATH2 ...]
```