---
id: linux-man-pages-usage-examples-top-https-man7-org-linux-man-pages-man1-abico-90d69f6f
type: concept
title: USAGE EXAMPLES         [top](https://man7.org/linux/man-pages/man1/abicompat.1.html#top_of_page)
description: '```'
category: linux-man-pages
tags: []
source:
  name: linux-man-pages
  url: https://man7.org/linux/man-pages/man1/abicompat.1.html
updated_at: '2026-08-11'
created_at: '2026-08-11'
---

## USAGE EXAMPLES         [top](https://man7.org/linux/man-pages/man1/abicompat.1.html#top_of_page)

```
          • Detecting a possible ABI incompatibility in a new shared
            library version:

                $ cat -n test0.h
                     1  struct foo
                     2  {
                     3    int m0;
                     4
                     5    foo()
                     6      : m0()
                     7    {}
                     8  };
                     9
                    10  foo*
                    11  first_func();
                    12
                    13  void
                    14  second_func(foo&);
                    15
                    16  void
                    17  third_func();
                $

                $ cat -n test-app.cc
                     1  // Compile with:
                     2  //  g++ -g -Wall -o test-app -L. -ltest-0 test-app.cc
                     3
                     4  #include "test0.h"
                     5
                     6  int
                     7  main()
                     8  {
                     9    foo* f = first_func();
                    10    second_func(*f);
                    11    return 0;
                    12  }
                $

                $ cat -n test0.cc
                     1  // Compile this with:
                     2  //  g++ -g -Wall -shared -o libtest-0.so test0.cc
                     3
                     4  #include "test0.h"
                     5
                     6  foo*
                     7  first_func()
                     8  {
                     9    foo* f = new foo();
                    10    return f;
                    11  }
                    12
                    13  void
                    14  second_func(foo&)
                    15  {
                    16  }
                    17
                    18  void
                    19  third_func()
                    20  {
                    21  }
                $

                $ cat -n test1.h
                     1  struct foo
                     2  {
                     3    int  m0;
                     4    char m1; /* <-- a new member got added here! */
                     5
                     6    foo()
                     7    : m0(),
                     8      m1()
                     9    {}
                    10  };
                    11
                    12  foo*
                    13  first_func();
                    14
                    15  void
                    16  second_func(foo&);
                    17
                    18  void
                    19  third_func();
                $

                $ cat -n test1.cc
                     1  // Compile this with:
                     2  //  g++ -g -Wall -shared -o libtest-1.so test1.cc
                     3
                     4  #include "test1.h"
                     5
                     6  foo*
                     7  first_func()
                     8  {
                     9    foo* f = new foo();
                    10    return f;
                    11  }
                    12
                    13  void
                    14  second_func(foo&)
                    15  {
                    16  }
                    17
                    18  /* Let's comment out the definition of third_func()
                    19     void
                    20     third_func()
                    21     {
                    22     }
                    23  */
                $

            • Compile the first and second versions of the libraries:
              libtest-0.so and libtest-1.so:

                  $ g++ -g -Wall -shared -o libtest-0.so test0.cc
                  $ g++ -g -Wall -shared -o libtest-1.so test1.cc

            • Compile the application and link it against the first
              version of the library, creating the test-app binary:

                  $ g++ -g -Wall -o test-app -L. -l