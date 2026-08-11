---
id: linux-man-pages-usage-examples-top-https-man7-org-linux-man-pages-man1-abidw-e6884ed0
type: concept
title: USAGE EXAMPLES         [top](https://man7.org/linux/man-pages/man1/abidw.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidw.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## USAGE EXAMPLES         [top](https://man7.org/linux/man-pages/man1/abidw.1.html#top_of_page)

```
          1. Emitting an ABIXML representation of a binary:

                 $ abidw binary > binary.abi

          2. Emitting an ABIXML representation of a set of binaries
             specified on the command line:

                 $ abidw --added-binaries=bin1,bin2,bin3  \
                         --added-binaries-dir /some/where \
                         binary > binaries.abi

             Note that the binaries bin1, bin2 and bin3 are to be found
             in the directory /some/where.  A representation of the ABI
             of the set of binaries binary, bin1, bin2 and bin3 called an
             ABI corpus group is serialized in the file binaries.abi.

          3. Emitting an ABIXML representation of a binary and its
             dependencies:

                 $ abidw --follow-dependencies              \
                         --added-binaries-dir /some/where   \
                         binary > binary.abi

             Note that only the dependencies that are found in the
             directory /some/where are analysed.  Their ABIs, along with
             the ABI the binary named binary are represented as an ABI
             corpus group and serialized in the file binary.abi, in the
             ABIXML format.
```