---
id: python-constants-added-by-the-site-https-docs-python-org-3-library--a8c4ec5e
type: concept
title: 'Constants added by the [`site`](https://docs.python.org/3/library/site.html#module-site
  "site: Module responsible for site-specific configuration.") module[¶](https://docs.python.org/3/library/constants.html#constants-added-by-the-site-module
  "Link to this heading")'
description: 'The [`site`](https://docs.python.org/3/library/site.html#module-site
  "site: Module responsible for site-specific configuration.") module (which is imported
  automatically during startup, except'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/constants.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Constants added by the [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") module[¶](https://docs.python.org/3/library/constants.html#constants-added-by-the-site-module "Link to this heading")

The [`site`](https://docs.python.org/3/library/site.html#module-site "site: Module responsible for site-specific configuration.") module (which is imported automatically during startup, except
if the [`-S`](https://docs.python.org/3/using/cmdline.html#cmdoption-S) command-line option is given) adds several constants to the
built-in namespace. They are useful for the interactive interpreter shell and
should not be used in programs.

quit(*code=None*)[¶](https://docs.python.org/3/library/constants.html#quit "Link to this definition")

exit(*code=None*)[¶](https://docs.python.org/3/library/constants.html#exit "Link to this definition")
:   Objects that when printed, print a message like “Use quit() or Ctrl-D
    (i.e. EOF) to exit”, and when accessed directly in the interactive
    interpreter or called as functions, raise [`SystemExit`](https://docs.python.org/3/library/exceptions.html#SystemExit "SystemExit") with the
    specified exit code.

help
:   Object that when printed, prints the message “Type help() for interactive
    help, or help(object) for help about object.”, and when accessed directly
    in the interactive interpreter, invokes the built-in help system
    (see [`help()`](https://docs.python.org/3/library/functions.html#help "help")).

copyright[¶](https://docs.python.org/3/library/constants.html#copyright "Link to this definition")

credits[¶](https://docs.python.org/3/library/constants.html#credits "Link to this definition")
:   Objects that when printed or called, print the text of copyright or
    credits, respectively.

license[¶](https://docs.python.org/3/library/constants.html#license "Link to this definition")
:   Object that when printed, prints the message “Type license() to see the
    full license text”, and when called, displays the full license text in a
    pager-like fashion (one screen at a time).