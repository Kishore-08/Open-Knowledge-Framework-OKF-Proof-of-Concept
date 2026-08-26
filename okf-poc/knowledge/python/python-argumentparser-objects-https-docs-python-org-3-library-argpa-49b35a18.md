---
id: python-argumentparser-objects-https-docs-python-org-3-library-argpa-49b35a18
type: concept
title: ArgumentParser objects[¶](https://docs.python.org/3/library/argparse.html#argumentparser-objects
  "Link to this heading")
description: '*class* argparse.ArgumentParser(*prog=None*, *usage=None*, *description=None*,
  *epilog=None*, *parents=[]*, *formatter\_class=argparse.HelpFormatter*, *prefix\_chars=''-''*,
  *fromfile\_prefix\_chars=Non'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## ArgumentParser objects[¶](https://docs.python.org/3/library/argparse.html#argumentparser-objects "Link to this heading")

*class* argparse.ArgumentParser(*prog=None*, *usage=None*, *description=None*, *epilog=None*, *parents=[]*, *formatter\_class=argparse.HelpFormatter*, *prefix\_chars='-'*, *fromfile\_prefix\_chars=None*, *argument\_default=None*, *conflict\_handler='error'*, *add\_help=True*, *allow\_abbrev=True*, *exit\_on\_error=True*, *\**, *suggest\_on\_error=False*, *color=True*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "Link to this definition")
:   Create a new `ArgumentParser` object. All parameters should be passed
    as keyword arguments. Each parameter has its own more detailed description
    below, but in short they are:

    - [prog](https://docs.python.org/3/library/argparse.html#prog) - The name of the program (default: generated from the `__main__`
      module attributes and `sys.argv[0]`)
    - [usage](https://docs.python.org/3/library/argparse.html#usage) - The string describing the program usage (default: generated from
      arguments added to parser)
    - [description](https://docs.python.org/3/library/argparse.html#description) - Text to display before the argument help
      (by default, no text)
    - [epilog](https://docs.python.org/3/library/argparse.html#epilog) - Text to display after the argument help (by default, no text)
    - [parents](https://docs.python.org/3/library/argparse.html#parents) - A list of `ArgumentParser` objects whose arguments should
      also be included
    - [formatter\_class](https://docs.python.org/3/library/argparse.html#formatter-class) - A class for customizing the help output
    - [prefix\_chars](https://docs.python.org/3/library/argparse.html#prefix-chars) - The set of characters that prefix optional arguments
      (default: ‘-‘)
    - [fromfile\_prefix\_chars](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars) - The set of characters that prefix files from
      which additional arguments should be read (default: `None`)
    - [argument\_default](https://docs.python.org/3/library/argparse.html#argument-default) - The global default value for arguments
      (default: `None`)
    - [conflict\_handler](https://docs.python.org/3/library/argparse.html#conflict-handler) - The strategy for resolving conflicting optionals
      (usually unnecessary)
    - [add\_help](https://docs.python.org/3/library/argparse.html#add-help) - Add a `-h/--help` option to the parser (default: `True`)
    - [allow\_abbrev](https://docs.python.org/3/library/argparse.html#allow-abbrev) - Allows long options to be abbreviated if the
      abbreviation is unambiguous (default: `True`)
    - [exit\_on\_error](https://docs.python.org/3/library/argparse.html#exit-on-error) - Determines whether or not `ArgumentParser` exits with
      error info when an error occurs. (default: `True`)
    - [suggest\_on\_error](https://docs.python.org/3/library/argparse.html#suggest-on-error) - Enables suggestions for mistyped argument choices
      and subparser names (default: `False`)
    - [color](https://docs.python.org/3/library/argparse.html#color) - Allow color output (default: `True`)

    Changed in version 3.5: *allow\_abbrev* parameter was added.

    Changed in version 3.8: In previous versions, *allow\_abbrev* also disabled grouping of short
    flags such as `-vv` to mean `-v -v`.

    Changed in version 3.9: *exit\_on\_error* parameter was added.

    Changed in version 3.14: *suggest\_on\_error* and *color* parameters were added.

The following sections describe how each of these are used.