---
id: python-parsing-arguments-https-docs-python-org-3-library-optparse-h-f59a6996
type: concept
title: Parsing arguments[¶](https://docs.python.org/3/library/optparse.html#parsing-arguments
  "Link to this heading")
description: The whole point of creating and populating an OptionParser is to call
  its
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Parsing arguments[¶](https://docs.python.org/3/library/optparse.html#parsing-arguments "Link to this heading")

The whole point of creating and populating an OptionParser is to call its
[`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args") method.

OptionParser.parse\_args(*args=None*, *values=None*)[¶](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "Link to this definition")
:   Parse the command-line options found in *args*.

    The input parameters are

    `args`
    :   the list of arguments to process (default: `sys.argv[1:]`)

    `values`
    :   a [`Values`](https://docs.python.org/3/library/optparse.html#optparse.Values "optparse.Values") object to store option arguments in (default: a
        new instance of `Values`) – if you give an existing object, the
        option defaults will not be initialized on it

    and the return value is a pair `(options, args)` where

    `options`
    :   the same object that was passed in as *values*, or the `optparse.Values`
        instance created by `optparse`

    `args`
    :   the leftover positional arguments after all options have been processed

The most common usage is to supply neither keyword argument. If you supply
`values`, it will be modified with repeated [`setattr()`](https://docs.python.org/3/library/functions.html#setattr "setattr") calls (roughly one
for every option argument stored to an option destination) and returned by
[`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args").

If [`parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args") encounters any errors in the argument list, it calls the
OptionParser’s `error()` method with an appropriate end-user error message.
This ultimately terminates your process with an exit status of 2 (the
traditional Unix exit status for command-line errors).