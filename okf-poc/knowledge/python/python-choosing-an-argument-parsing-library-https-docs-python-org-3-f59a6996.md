---
id: python-choosing-an-argument-parsing-library-https-docs-python-org-3-f59a6996
type: concept
title: Choosing an argument parsing library[¶](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parsing-library
  "Link to this heading")
description: 'The standard library includes three argument parsing libraries:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Choosing an argument parsing library[¶](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parsing-library "Link to this heading")

The standard library includes three argument parsing libraries:

- [`getopt`](https://docs.python.org/3/library/getopt.html#module-getopt "getopt: Portable parser for command line options; support both short and long option names."): a module that closely mirrors the procedural C `getopt` API.
  Included in the standard library since before the initial Python 1.0 release.
- `optparse`: a declarative replacement for `getopt` that
  provides equivalent functionality without requiring each application
  to implement its own procedural option parsing logic. Included
  in the standard library since the Python 2.3 release.
- [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library."): a more opinionated alternative to `optparse` that
  provides more functionality by default, at the expense of reduced application
  flexibility in controlling exactly how arguments are processed. Included in
  the standard library since the Python 2.7 and Python 3.2 releases.

In the absence of more specific argument parsing design constraints, [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
is the recommended choice for implementing command line applications, as it offers
the highest level of baseline functionality with the least application level code.

[`getopt`](https://docs.python.org/3/library/getopt.html#module-getopt "getopt: Portable parser for command line options; support both short and long option names.") is retained almost entirely for backwards compatibility reasons.
However, it also serves a niche use case as a tool for prototyping and testing
command line argument handling in `getopt`-based C applications.

`optparse` should be considered as an alternative to [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.") in the
following cases:

- an application is already using `optparse` and doesn’t want to risk the
  subtle behavioural changes that may arise when migrating to [`argparse`](https://docs.python.org/3/library/argparse.html#module-argparse "argparse: Command-line option and argument parsing library.")
- the application requires additional control over the way options and
  positional parameters are interleaved on the command line (including
  the ability to disable the interleaving feature completely)
- the application requires additional control over the incremental parsing
  of command line elements (while `argparse` does support this, the
  exact way it works in practice is undesirable for some use cases)
- the application requires additional control over the handling of options
  which accept parameter values that may start with `-` (such as delegated
  options to be passed to invoked subprocesses)
- the application requires some other command line parameter processing
  behavior which `argparse` does not support, but which can be implemented
  in terms of the lower level interface offered by `optparse`

These considerations also mean that `optparse` is likely to provide a
better foundation for library authors writing third party command line
argument processing libraries.

As a concrete example, consider the following two command line argument
parsing configurations, the first using `optparse`, and the second
using `argparse`:

```
import optparse

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-o', '--output')
    parser.add_option('-v', dest='verbose', action='store_true')
    opts, args = parser.parse_args()
    process(args, output=opts.output, verbose=opts.verbose)
```

```
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argumen