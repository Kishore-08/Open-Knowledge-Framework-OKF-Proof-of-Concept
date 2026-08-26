---
id: python-type-https-docs-python-org-3-library-argparse-html-type-link-49b35a18
type: concept
title: type[¶](https://docs.python.org/3/library/argparse.html#type "Link to this
  heading")
description: By default, the parser reads command-line arguments in as simple
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/argparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### type[¶](https://docs.python.org/3/library/argparse.html#type "Link to this heading")

By default, the parser reads command-line arguments in as simple
strings. However, quite often the command-line string should instead be
interpreted as another type, such as a [`float`](https://docs.python.org/3/library/functions.html#float "float") or [`int`](https://docs.python.org/3/library/functions.html#int "int"). The
`type` keyword for [`add_argument()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument "argparse.ArgumentParser.add_argument") allows any
necessary type-checking and type conversions to be performed.

If the [type](https://docs.python.org/3/library/argparse.html#type) keyword is used with the [default](https://docs.python.org/3/library/argparse.html#default) keyword, the type converter
is only applied if the default is a string.

The argument to `type` can be a callable that accepts a single string or
the name of a registered type (see [`register()`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.register "argparse.ArgumentParser.register"))
If the function raises [`ArgumentTypeError`](https://docs.python.org/3/library/argparse.html#argparse.ArgumentTypeError "argparse.ArgumentTypeError"), [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"), or
[`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"), the exception is caught and a nicely formatted error
message is displayed. Other exception types are not handled.

Common built-in types and functions can be used as type converters:

```
import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('count', type=int)
parser.add_argument('distance', type=float)
parser.add_argument('street', type=ascii)
parser.add_argument('code_point', type=ord)
parser.add_argument('datapath', type=pathlib.Path)
```

User defined functions can be used as well:

```
>>> def hyphenated(string):
...     return '-'.join([word[:4] for word in string.casefold().split()])
...
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('short_title', type=hyphenated)
>>> parser.parse_args(['"The Tale of Two Cities"'])
Namespace(short_title='"the-tale-of-two-citi')
```

The [`bool()`](https://docs.python.org/3/library/functions.html#bool "bool") function is not recommended as a type converter. All it does
is convert empty strings to `False` and non-empty strings to `True`.
This is usually not what is desired:

```
>>> parser = argparse.ArgumentParser()
>>> _ = parser.add_argument('--verbose', type=bool)
>>> parser.parse_args(['--verbose', 'False'])
Namespace(verbose=True)
```

See [`BooleanOptionalAction`](https://docs.python.org/3/library/argparse.html#argparse.BooleanOptionalAction "argparse.BooleanOptionalAction") or `action='store_true'` for common
alternatives.

In general, the `type` keyword is a convenience that should only be used for
simple conversions that can only raise one of the three supported exceptions.
Anything with more interesting error-handling or resource management should be
done downstream after the arguments are parsed.

For example, JSON or YAML conversions have complex error cases that require
better reporting than can be given by the `type` keyword. A
[`JSONDecodeError`](https://docs.python.org/3/library/json.html#json.JSONDecodeError "json.JSONDecodeError") would not be well formatted and a
[`FileNotFoundError`](https://docs.python.org/3/library/exceptions.html#FileNotFoundError "FileNotFoundError") exception would not be handled at all.

Even [`FileType`](https://docs.python.org/3/library/argparse.html#argparse.FileType "argparse.FileType") has its limitations for use with the `type`
keyword. If one argument uses `FileType` and then a
subsequent argument fails, an error is reported but the file is not
automatically closed. In this case, it would be better to wait until after
the parser has run and then use the