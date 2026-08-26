---
id: python-printing-a-version-string-https-docs-python-org-3-library-op-f59a6996
type: concept
title: Printing a version string[¶](https://docs.python.org/3/library/optparse.html#printing-a-version-string
  "Link to this heading")
description: Similar to the brief usage string, `optparse` can also print a version
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Printing a version string[¶](https://docs.python.org/3/library/optparse.html#printing-a-version-string "Link to this heading")

Similar to the brief usage string, `optparse` can also print a version
string for your program. You have to supply the string as the `version`
argument to OptionParser:

```
parser = OptionParser(usage="%prog [-f] [-q]", version="%prog 1.0")
```

`%prog` is expanded just like it is in `usage`. Apart from that,
`version` can contain anything you like. When you supply it, `optparse`
automatically adds a `--version` option to your parser. If it encounters
this option on the command line, it expands your `version` string (by
replacing `%prog`), prints it to stdout, and exits.

For example, if your script is called `/usr/bin/foo`:

```
$ /usr/bin/foo --version
foo 1.0
```

The following two methods can be used to print and get the `version` string:

OptionParser.print\_version(*file=None*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.print_version "Link to this definition")
:   Print the version message for the current program (`self.version`) to
    *file* (default stdout). As with [`print_usage()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.print_usage "optparse.OptionParser.print_usage"), any occurrence
    of `%prog` in `self.version` is replaced with the name of the current
    program. Does nothing if `self.version` is empty or undefined.

OptionParser.get\_version()[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.get_version "Link to this definition")
:   Same as [`print_version()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.print_version "optparse.OptionParser.print_version") but returns the version string instead of
    printing it.