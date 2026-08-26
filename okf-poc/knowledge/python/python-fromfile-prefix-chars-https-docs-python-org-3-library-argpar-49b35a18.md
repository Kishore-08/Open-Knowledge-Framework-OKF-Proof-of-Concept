---
id: python-fromfile-prefix-chars-https-docs-python-org-3-library-argpar-49b35a18
type: concept
title: fromfile\_prefix\_chars[¶](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars
  "Link to this heading")
description: Sometimes, when dealing with a particularly long argument list, it
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### fromfile\_prefix\_chars[¶](https://docs.python.org/3/library/argparse.html#fromfile-prefix-chars "Link to this heading")

Sometimes, when dealing with a particularly long argument list, it
may make sense to keep the list of arguments in a file rather than typing it out
at the command line. If the `fromfile_prefix_chars=` argument is given to the
[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") constructor, then arguments that start with any of the
specified characters will be treated as files, and will be replaced by the
arguments they contain. For example:

```
>>> with open('args.txt', 'w', encoding=sys.getfilesystemencoding()) as fp:
...     fp.write('-f\nbar')
...
>>> parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
>>> parser.add_argument('-f')
>>> parser.parse_args(['-f', 'foo', '@args.txt'])
Namespace(f='bar')
```

Arguments read from a file must be one per line by default (but see also
[`convert_arg_line_to_args()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.convert_arg_line_to_args "argparse.ArgumentParser.convert_arg_line_to_args")) and are treated as if they
were in the same place as the original file referencing argument on the command
line. So in the example above, the expression `['-f', 'foo', '@args.txt']`
is considered equivalent to the expression `['-f', 'foo', '-f', 'bar']`.

Note

Each line is treated as a single argument, so an empty line is read as an
empty string (`''`).

[`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") uses [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
to read the file containing arguments.

The `fromfile_prefix_chars=` argument defaults to `None`, meaning that
arguments will never be treated as file references.

Changed in version 3.12: [`ArgumentParser`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser "argparse.ArgumentParser") changed encoding and errors to read arguments files
from default (e.g. [`locale.getpreferredencoding(False)`](https://docs.python.org/3/library/locale.html#locale.getpreferredencoding "locale.getpreferredencoding")
and `"strict"`) to the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler).
Arguments file should be encoded in UTF-8 instead of ANSI Codepage on Windows.