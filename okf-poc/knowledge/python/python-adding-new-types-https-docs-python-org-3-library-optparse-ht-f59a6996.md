---
id: python-adding-new-types-https-docs-python-org-3-library-optparse-ht-f59a6996
type: concept
title: Adding new types[¶](https://docs.python.org/3/library/optparse.html#adding-new-types
  "Link to this heading")
description: To add new types, you need to define your own subclass of `optparse`’s
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Adding new types[¶](https://docs.python.org/3/library/optparse.html#adding-new-types "Link to this heading")

To add new types, you need to define your own subclass of `optparse`’s
[`Option`](https://docs.python.org/3/library/optparse.html#optparse.Option "optparse.Option") class. This class has a couple of attributes that define
`optparse`’s types: [`TYPES`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPES "optparse.Option.TYPES") and [`TYPE_CHECKER`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPE_CHECKER "optparse.Option.TYPE_CHECKER").

Option.TYPES[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPES "Link to this definition")
:   A tuple of type names; in your subclass, simply define a new tuple
    [`TYPES`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPES "optparse.Option.TYPES") that builds on the standard one.

Option.TYPE\_CHECKER[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPE_CHECKER "Link to this definition")
:   A dictionary mapping type names to type-checking functions. A type-checking
    function has the following signature:

    ```
    def check_mytype(option, opt, value)
    ```

    where `option` is an [`Option`](https://docs.python.org/3/library/optparse.html#optparse.Option "optparse.Option") instance, `opt` is an option string
    (e.g., `-f`), and `value` is the string from the command line that must
    be checked and converted to your desired type. `check_mytype()` should
    return an object of the hypothetical type `mytype`. The value returned by
    a type-checking function will wind up in the OptionValues instance returned
    by [`OptionParser.parse_args()`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser.parse_args "optparse.OptionParser.parse_args"), or be passed to a callback as the
    `value` parameter.

    Your type-checking function should raise [`OptionValueError`](https://docs.python.org/3/library/optparse.html#optparse.OptionValueError "optparse.OptionValueError") if it
    encounters any problems. `OptionValueError` takes a single string
    argument, which is passed as-is to [`OptionParser`](https://docs.python.org/3/library/optparse.html#optparse.OptionParser "optparse.OptionParser")’s `error()`
    method, which in turn prepends the program name and the string `"error:"`
    and prints everything to stderr before terminating the process.

Here’s a silly example that demonstrates adding a `"complex"` option type to
parse Python-style complex numbers on the command line. (This is even sillier
than it used to be, because `optparse` 1.3 added built-in support for
complex numbers, but never mind.)

First, the necessary imports:

```
from copy import copy
from optparse import Option, OptionValueError
```

You need to define your type-checker first, since it’s referred to later (in the
[`TYPE_CHECKER`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPE_CHECKER "optparse.Option.TYPE_CHECKER") class attribute of your Option subclass):

```
def check_complex(option, opt, value):
    try:
        return complex(value)
    except ValueError:
        raise OptionValueError(
            "option %s: invalid complex value: %r" % (opt, value))
```

Finally, the Option subclass:

```
class MyOption (Option):
    TYPES = Option.TYPES + ("complex",)
    TYPE_CHECKER = copy(Option.TYPE_CHECKER)
    TYPE_CHECKER["complex"] = check_complex
```

(If we didn’t make a [`copy()`](https://docs.python.org/3/library/copy.html#module-copy "copy: Shallow and deep copy operations.") of [`Option.TYPE_CHECKER`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPE_CHECKER "optparse.Option.TYPE_CHECKER"), we would end
up modifying the `TYPE_CHECKER` attribute of `optparse`’s
Option class. This being Python, nothing stops you from doing that except good
manners and common sense.)

That’s it! Now you can write a script that uses the new option type just