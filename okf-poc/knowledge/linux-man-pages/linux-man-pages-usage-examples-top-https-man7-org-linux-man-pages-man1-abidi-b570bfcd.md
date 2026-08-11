---
id: linux-man-pages-usage-examples-top-https-man7-org-linux-man-pages-man1-abidi-b570bfcd
type: concept
title: USAGE EXAMPLES         [top](https://man7.org/linux/man-pages/man1/abidiff.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abidiff.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## USAGE EXAMPLES         [top](https://man7.org/linux/man-pages/man1/abidiff.1.html#top_of_page)

```
          1. Detecting an ABI change in a sub-type of a function:

                 $ cat -n test-v0.cc
                          1      // Compile this with:
                          2      //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                          3
                          4      struct S0
                          5      {
                          6        int m0;
                          7      };
                          8
                          9      void
                         10      foo(S0* /*parameter_name*/)
                         11      {
                         12        // do something with parameter_name.
                         13      }
                 $
                 $ cat -n test-v1.cc
                          1      // Compile this with:
                          2      //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                          3
                          4      struct type_base
                          5      {
                          6        int inserted;
                          7      };
                          8
                          9      struct S0 : public type_base
                         10      {
                         11        int m0;
                         12      };
                         13
                         14      void
                         15      foo(S0* /*parameter_name*/)
                         16      {
                         17        // do something with parameter_name.
                         18      }
                 $
                 $ g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                 $ g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                 $
                 $ abidiff libtest-v0.so libtest-v1.so; echo "exit code: $?"
                 Functions changes summary: 0 Removed, 1 Changed, 0 Added function
                 Variables changes summary: 0 Removed, 0 Changed, 0 Added variable

                 1 function with some indirect sub-type change:

                   [C]'function void foo(S0*)' has some indirect sub-type changes:
                         parameter 0 of type 'S0*' has sub-type changes:
                           in pointed to type 'struct S0':
                             size changed from 32 to 64 bits
                             1 base class insertion:
                               struct type_base
                             1 data member change:
                              'int S0::m0' offset changed from 0 to 32
                 exit code: 4
                 $

       Note how the exit code is 4, meaning the third bit
       ABIDIFF_ABI_CHANGE of value 4 is set to 1.  This means the tool
       categorizes the ABI change as harmful and thus requires a user
       review.

          2. Detecting an incompatible ABI change in the type of a
             function:

                 $ cat -n test-v0.cc
                      1  // Compile this with:
                      2  //   g++ -g -Wall -shared -o libtest-v0.so test-v0.cc
                      3
                      4  struct S0
                      5  {
                      6    int m0;
                      7  };
                      8
                      9  S0
                     10  foo()
                     11  {
                     12    S0 s = {};
                     13    return s;
                     14  }
                 $
                 $ cat -n test-v1.cc
                      1  // Compile this with:
                      2  //   g++ -g -Wall -shared -o libtest-v1.so test-v1.cc
                      3
                      4  struct type_base
                      5  {
                      6    int inserted;
                      7  };
                      8
                      9  struct S0 : public type_base
                     10  {