---
id: python-argparse-parser-for-command-line-options-arguments-and-subco-49b35a18
type: concept
title: '`argparse` — Parser for command-line options, arguments and subcommands[¶](https'
description: Added in version 3.2.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

# `argparse` — Parser for command-line options, arguments and subcommands[¶](https://docs.python.org/3/library/argparse.html#module-argparse "Link to this heading")

Added in version 3.2.

**Source code:** [Lib/argparse.py](https://github.com/python/cpython/tree/3.14/Lib/argparse.py)

Note

While `argparse` is the default recommended standard library module
for implementing basic command line applications, authors with more
exacting requirements for exactly how their command line applications
behave may find it doesn’t provide the necessary level of control.
Refer to [Choosing an argument parsing library](https://docs.python.org/3/library/optparse.html#choosing-an-argument-parser) for alternatives to
consider when `argparse` doesn’t support behaviors that the application
requires (such as entirely disabling support for interspersed options and
positional arguments, or accepting option parameter values that start
with `-` even when they correspond to another defined option).

---

The `argparse` module makes it easy to write user-friendly command-line
interfaces. The program defines what arguments it requires, and `argparse`
will figure out how to parse those out of [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv "sys.argv"). The `argparse`
module also automatically generates help and usage messages. The module
will also issue errors when users give the program invalid arguments.

The `argparse` module’s support for command-line interfaces is built
around an instance of [`argparse.ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser"). It is a container for
argument specifications and has options that apply to the parser as whole:

```
parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
```

The [`ArgumentParser.add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") method attaches individual argument
specifications to the parser. It supports positional arguments, options that
accept values, and on/off flags:

```
parser.add_argument('filename')           # positional argument
parser.add_argument('-c', '--count')      # option that takes a value
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag
```

The [`ArgumentParser.parse_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args "argparse.ArgumentParser.parse_args") method runs the parser and places
the extracted data in a [`argparse.Namespace`](https://docs.python.org/3/library/argparse.html#argparse.Namespace "argparse.Namespace") object:

```
args = parser.parse_args()
print(args.filename, args.count, args.verbose)
```

Note

If you’re looking for a guide about how to upgrade [`optparse`](https://docs.python.org/3/library/optparse.html#module-optparse "optparse: Command-line option parsing library.") code
to `argparse`, see [Upgrading Optparse Code](https://docs.python.org/3/howto/argparse-optparse.html#upgrading-optparse-code).