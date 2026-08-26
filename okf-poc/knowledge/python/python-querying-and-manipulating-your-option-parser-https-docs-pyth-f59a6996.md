---
id: python-querying-and-manipulating-your-option-parser-https-docs-pyth-f59a6996
type: concept
title: Querying and manipulating your option parser[¶](https://docs.python.org/3/library/optparse.html#querying-and-manipulating-your-option-parser
  "Link to this heading")
description: The default behavior of the option parser can be customized slightly,
  and you
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Querying and manipulating your option parser[¶](https://docs.python.org/3/library/optparse.html#querying-and-manipulating-your-option-parser "Link to this heading")

The default behavior of the option parser can be customized slightly, and you
can also poke around your option parser and see what’s there. OptionParser
provides several methods to help you out:

OptionParser.disable\_interspersed\_args()[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.disable_interspersed_args "Link to this definition")
:   Set parsing to stop on the first non-option. For example, if `-a` and
    `-b` are both simple options that take no arguments, `optparse`
    normally accepts this syntax:

    ```
    prog -a arg1 -b arg2
    ```

    and treats it as equivalent to

    ```
    prog -a -b arg1 arg2
    ```

    To disable this feature, call `disable_interspersed_args()`. This
    restores traditional Unix syntax, where option parsing stops with the first
    non-option argument.

    Use this if you have a command processor which runs another command which has
    options of its own and you want to make sure these options don’t get
    confused. For example, each command might have a different set of options.

OptionParser.enable\_interspersed\_args()[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.enable_interspersed_args "Link to this definition")
:   Set parsing to not stop on the first non-option, allowing interspersing
    switches with command arguments. This is the default behavior.

OptionParser.get\_option(*opt\_str*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.get_option "Link to this definition")
:   Returns the Option instance with the option string *opt\_str*, or `None` if
    no options have that option string.

OptionParser.has\_option(*opt\_str*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.has_option "Link to this definition")
:   Return `True` if the OptionParser has an option with option string *opt\_str*
    (e.g., `-q` or `--verbose`).

OptionParser.remove\_option(*opt\_str*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.remove_option "Link to this definition")
:   If the [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser") has an option corresponding to *opt\_str*, that
    option is removed. If that option provided any other option strings, all of
    those option strings become invalid. If *opt\_str* does not occur in any
    option belonging to this `OptionParser`, raises [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError").