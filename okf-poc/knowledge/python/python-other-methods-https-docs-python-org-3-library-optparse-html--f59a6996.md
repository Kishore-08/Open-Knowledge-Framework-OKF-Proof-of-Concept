---
id: python-other-methods-https-docs-python-org-3-library-optparse-html--f59a6996
type: concept
title: Other methods[¶](https://docs.python.org/3/library/optparse.html#other-methods
  "Link to this heading")
description: 'OptionParser supports several other public methods:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Other methods[¶](https://docs.python.org/3/library/optparse.html#other-methods "Link to this heading")

OptionParser supports several other public methods:

OptionParser.set\_usage(*usage*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.set_usage "Link to this definition")
:   Set the usage string according to the rules described above for the `usage`
    constructor keyword argument. Passing `None` sets the default usage
    string; use `optparse.SUPPRESS_USAGE` to suppress a usage message.

OptionParser.print\_usage(*file=None*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.print_usage "Link to this definition")
:   Print the usage message for the current program (`self.usage`) to *file*
    (default stdout). Any occurrence of the string `%prog` in `self.usage`
    is replaced with the name of the current program. Does nothing if
    `self.usage` is empty or not defined.

OptionParser.get\_usage()[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.get_usage "Link to this definition")
:   Same as [`print_usage()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.print_usage "optparse.OptionParser.print_usage") but returns the usage string instead of
    printing it.

OptionParser.set\_defaults(*dest=value*, *...*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.set_defaults "Link to this definition")
:   Set default values for several option destinations at once. Using
    `set_defaults()` is the preferred way to set default values for options,
    since multiple options can share the same destination. For example, if
    several “mode” options all set the same destination, any one of them can set
    the default, and the last one wins:

    ```
    parser.add_option("--advanced", action="store_const",
                      dest="mode", const="advanced",
                      default="novice")    # overridden below
    parser.add_option("--novice", action="store_const",
                      dest="mode", const="novice",
                      default="advanced")  # overrides above setting
    ```

    To avoid this confusion, use `set_defaults()`:

    ```
    parser.set_defaults(mode="advanced")
    parser.add_option("--advanced", action="store_const",
                      dest="mode", const="advanced")
    parser.add_option("--novice", action="store_const",
                      dest="mode", const="novice")
    ```