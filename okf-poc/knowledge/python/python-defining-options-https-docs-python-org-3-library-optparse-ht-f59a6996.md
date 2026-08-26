---
id: python-defining-options-https-docs-python-org-3-library-optparse-ht-f59a6996
type: concept
title: Defining options[¶](https://docs.python.org/3/library/optparse.html#defining-options
  "Link to this heading")
description: Each Option instance represents a set of synonymous command-line option
  strings,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Defining options[¶](https://docs.python.org/3/library/optparse.html#defining-options "Link to this heading")

Each Option instance represents a set of synonymous command-line option strings,
e.g. `-f` and `--file`. You can specify any number of short or
long option strings, but you must specify at least one overall option string.

The canonical way to create an [`Option`](https://docs.python.org/3/library/optparse.html#optparse.Option "optparse.Option") instance is with the
`add_option()` method of [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser").

OptionParser.add\_option(*option*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.add_option "Link to this definition")

OptionParser.add\_option(*\*opt\_str*, *attr=value*, *...*)
:   To define an option with only a short option string:

    ```
    parser.add_option("-f", attr=value, ...)
    ```

    And to define an option with only a long option string:

    ```
    parser.add_option("--foo", attr=value, ...)
    ```

    The keyword arguments define attributes of the new Option object. The most
    important option attribute is [`action`](https://docs.python.org/3/library/optparse.html#optparse.Option.action "optparse.Option.action"), and it largely
    determines which other attributes are relevant or required. If you pass
    irrelevant option attributes, or fail to pass required ones, `optparse`
    raises an [`OptionError`](https://docs.python.org/3/library/optparse.html#optparse.OptionError "optparse.OptionError") exception explaining your mistake.

    An option’s *action* determines what `optparse` does when it encounters
    this option on the command-line. The standard option actions hard-coded into
    `optparse` are:

    `"store"`
    :   store this option’s argument (default)

    `"store_const"`
    :   store a constant value, pre-set via [`Option.const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const")

    `"store_true"`
    :   store `True`

    `"store_false"`
    :   store `False`

    `"append"`
    :   append this option’s argument to a list

    `"append_const"`
    :   append a constant value to a list, pre-set via [`Option.const`](https://docs.python.org/3/library/optparse.html#optparse.Option.const "optparse.Option.const")

    `"count"`
    :   increment a counter by one

    `"callback"`
    :   call a specified function

    `"help"`
    :   print a usage message including all options and the documentation for them

    (If you don’t supply an action, the default is `"store"`. For this action,
    you may also supply [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") and [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest") option
    attributes; see [Standard option actions](https://docs.python.org/3/library/optparse.html#optparse-standard-option-actions).)

As you can see, most actions involve storing or updating a value somewhere.
`optparse` always creates a special object for this, conventionally called
`options`, which is an instance of [`optparse.Values`](https://docs.python.org/3/library/optparse.html#optparse.Values "optparse.Values").

*class* optparse.Values[¶](https://docs.python.org/3/library/optparse.html#optparse.Values "Link to this definition")
:   An object holding parsed argument names and values as attributes.
    Normally created by calling when calling [`OptionParser.parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args"),
    and can be overridden by a custom subclass passed to the *values* argument of
    `OptionParser.parse_args()` (as described in [Parsing arguments](https://docs.python.org/3/library/optparse.html#optparse-parsing-arguments)).

Option
arguments (and various other values) are stored as attributes of t