---
id: python-option-attributes-https-docs-python-org-3-library-optparse-h-f59a6996
type: concept
title: Option attributes[¶](https://docs.python.org/3/library/optparse.html#option-attributes
  "Link to this heading")
description: '*class* optparse.Option[¶](https://docs.python.org/3/library/optparse.html#optparse.Option
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Option attributes[¶](https://docs.python.org/3/library/optparse.html#option-attributes "Link to this heading")

*class* optparse.Option[¶](https://docs.python.org/3/library/optparse.html#optparse.Option "Link to this definition")
:   A single command line argument,
    with various attributes passed by keyword to the constructor.
    Normally created with [`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option") rather than directly,
    and can be overridden by a custom class via the *option\_class* argument
    to [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser").

The following option attributes may be passed as keyword arguments to
[`OptionParser.add_option()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "optparse.OptionParser.add_option"). If you pass an option attribute that is not
relevant to a particular option, or fail to pass a required option attribute,
`optparse` raises [`OptionError`](https://docs.python.org/3/library/optparse.html#optparse.OptionError "optparse.OptionError").

Option.action[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.action "Link to this definition")
:   (default: `"store"`)

    Determines `optparse`’s behaviour when this option is seen on the
    command line; the available options are documented [here](https://docs.python.org/3/library/optparse.html#optparse-standard-option-actions).

Option.type[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.type "Link to this definition")
:   (default: `"string"`)

    The argument type expected by this option (e.g., `"string"` or `"int"`);
    the available option types are documented [here](https://docs.python.org/3/library/optparse.html#optparse-standard-option-types).

Option.dest[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "Link to this definition")
:   (default: derived from option strings)

    If the option’s action implies writing or modifying a value somewhere, this
    tells `optparse` where to write it: `dest` names an
    attribute of the `options` object that `optparse` builds as it parses
    the command line.

Option.default[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.default "Link to this definition")
:   The value to use for this option’s destination if the option is not seen on
    the command line. See also [`OptionParser.set_defaults()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.set_defaults "optparse.OptionParser.set_defaults").

Option.nargs[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.nargs "Link to this definition")
:   (default: 1)

    How many arguments of type [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") should be consumed when this
    option is seen. If > 1, `optparse` will store a tuple of values to
    [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest").

Option.const[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.const "Link to this definition")
:   For actions that store a constant value, the constant value to store.

Option.choices[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.choices "Link to this definition")
:   For options of type `"choice"`, the list of strings the user may choose
    from.

Option.callback[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.callback "Link to this definition")
:   For options with action `"callback"`, the callable to call when this option
    is seen. See section [Option Callbacks](https://docs.python.org/3/library/optparse.html#optparse-option-callbacks) for detail on the
    arguments passed to the callable.

Option.callback\_args[¶](https://docs.python.org/3/library/optparse.html#optparse.Opt