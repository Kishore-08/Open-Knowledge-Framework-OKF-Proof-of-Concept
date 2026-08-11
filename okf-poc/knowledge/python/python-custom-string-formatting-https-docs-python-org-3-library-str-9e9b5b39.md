---
id: python-custom-string-formatting-https-docs-python-org-3-library-str-9e9b5b39
type: concept
title: Custom string formatting[¶](https://docs.python.org/3/library/string.html#custom-string-formatting
  "Link to this heading")
description: The built-in string class provides the ability to do complex variable
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/string.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Custom string formatting[¶](https://docs.python.org/3/library/string.html#custom-string-formatting "Link to this heading")

The built-in string class provides the ability to do complex variable
substitutions and value formatting via the [`format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") method described in
[**PEP 3101**](https://peps.python.org/pep-3101/). The [`Formatter`](https://docs.python.org/3/library/string.html#string.Formatter "string.Formatter") class in the `string` module allows
you to create and customize your own string formatting behaviors using the same
implementation as the built-in `format()` method.

*class* string.Formatter[¶](https://docs.python.org/3/library/string.html#string.Formatter "Link to this definition")
:   The `Formatter` class has the following public methods:

    format(*format\_string*, */*, *\*args*, *\*\*kwargs*)[¶](https://docs.python.org/3/library/string.html#string.Formatter.format "Link to this definition")
    :   The primary API method. It takes a format string and
        an arbitrary set of positional and keyword arguments.
        It is just a wrapper that calls [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat").

        Changed in version 3.7: A format string argument is now [positional-only](https://docs.python.org/3/glossary.html#positional-only-parameter).

    vformat(*format\_string*, *args*, *kwargs*)[¶](https://docs.python.org/3/library/string.html#string.Formatter.vformat "Link to this definition")
    :   This function does the actual work of formatting. It is exposed as a
        separate function for cases where you want to pass in a predefined
        dictionary of arguments, rather than unpacking and repacking the
        dictionary as individual arguments using the `*args` and `**kwargs`
        syntax. `vformat()` does the work of breaking up the format string
        into character data and replacement fields. It calls the various
        methods described below.

    In addition, the `Formatter` defines a number of methods that are
    intended to be replaced by subclasses:

    parse(*format\_string*)[¶](https://docs.python.org/3/library/string.html#string.Formatter.parse "Link to this definition")
    :   Loop over the format\_string and return an iterable of tuples
        (*literal\_text*, *field\_name*, *format\_spec*, *conversion*). This is used
        by [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat") to break the string into either literal text, or
        replacement fields.

        The values in the tuple conceptually represent a span of literal text
        followed by a single replacement field. If there is no literal text
        (which can happen if two replacement fields occur consecutively), then
        *literal\_text* will be a zero-length string. If there is no replacement
        field, then the values of *field\_name*, *format\_spec* and *conversion*
        will be `None`. The value of *field\_name* is unmodified and
        auto-numbering of non-numbered positional fields is done by [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat").

    get\_field(*field\_name*, *args*, *kwargs*)[¶](https://docs.python.org/3/library/string.html#string.Formatter.get_field "Link to this definition")
    :   Given *field\_name*, convert it to an object to be formatted.
        Auto-numbering of *field\_name* returned from [`parse()`](https://docs.python.org/3/library/string.html#string.Formatter.parse "string.Formatter.parse") is done by
        [`vformat()`](https://docs.python.org/3/library/string.html#string.Formatter.vformat "string.Formatter.vformat") before calling this method. Returns a tuple (obj, used\_key).
        The default version takes strings of the form defined in [**PEP 3101**](https://peps.python.org/pep-3101/),