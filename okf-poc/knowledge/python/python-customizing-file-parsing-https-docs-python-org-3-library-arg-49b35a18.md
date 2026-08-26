---
id: python-customizing-file-parsing-https-docs-python-org-3-library-arg-49b35a18
type: concept
title: Customizing file parsing[¶](https://docs.python.org/3/library/argparse.html#customizing-file-parsing
  "Link to this heading")
description: ArgumentParser.convert\_arg\_line\_to\_args(*arg\_line*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.convert_arg_line_to_args
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Customizing file parsing[¶](https://docs.python.org/3/library/argparse.html#customizing-file-parsing "Link to this heading")

ArgumentParser.convert\_arg\_line\_to\_args(*arg\_line*)[¶](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.convert_arg_line_to_args "Link to this definition")
:   Arguments that are read from a file (see the *fromfile\_prefix\_chars*
    keyword argument to the [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor) are read one
    argument per line. `convert_arg_line_to_args()` can be overridden for
    fancier reading.

    This method takes a single argument *arg\_line* which is a string read from
    the argument file. It returns a list of arguments parsed from this string.
    The method is called once per line read from the argument file, in order.

    A useful override of this method is one that treats each space-separated word
    as an argument. The following example demonstrates how to do this:

    ```
    class MyArgumentParser(argparse.ArgumentParser):
        def convert_arg_line_to_args(self, arg_line):
            return arg_line.split()
    ```

    Note that with this override an argument can no longer contain spaces, since
    each space-separated word becomes a separate argument.