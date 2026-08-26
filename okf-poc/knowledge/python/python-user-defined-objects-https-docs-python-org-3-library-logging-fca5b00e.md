---
id: python-user-defined-objects-https-docs-python-org-3-library-logging-fca5b00e
type: concept
title: User-defined objects[¶](https://docs.python.org/3/library/logging.config.html#user-defined-objects
  "Link to this heading")
description: The schema supports user-defined objects for handlers, filters and
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.config.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### User-defined objects[¶](https://docs.python.org/3/library/logging.config.html#user-defined-objects "Link to this heading")

The schema supports user-defined objects for handlers, filters and
formatters. (Loggers do not need to have different types for
different instances, so there is no support in this configuration
schema for user-defined logger classes.)

Objects to be configured are described by dictionaries
which detail their configuration. In some places, the logging system
will be able to infer from the context how an object is to be
instantiated, but when a user-defined object is to be instantiated,
the system will not know how to do this. In order to provide complete
flexibility for user-defined object instantiation, the user needs
to provide a ‘factory’ - a callable which is called with a
configuration dictionary and which returns the instantiated object.
This is signalled by an absolute import path to the factory being
made available under the special key `'()'`. Here’s a concrete
example:

```
formatters:
  brief:
    format: '%(message)s'
  default:
    format: '%(asctime)s %(levelname)-8s %(name)-15s %(message)s'
    datefmt: '%Y-%m-%d %H:%M:%S'
  custom:
      (): my.package.customFormatterFactory
      bar: baz
      spam: 99.9
      answer: 42
```

The above YAML snippet defines three formatters. The first, with id
`brief`, is a standard [`logging.Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter") instance with the
specified format string. The second, with id `default`, has a
longer format and also defines the time format explicitly, and will
result in a `logging.Formatter` initialized with those two format
strings. Shown in Python source form, the `brief` and `default`
formatters have configuration sub-dictionaries:

```
{
  'format' : '%(message)s'
}
```

and:

```
{
  'format' : '%(asctime)s %(levelname)-8s %(name)-15s %(message)s',
  'datefmt' : '%Y-%m-%d %H:%M:%S'
}
```

respectively, and as these dictionaries do not contain the special key
`'()'`, the instantiation is inferred from the context: as a result,
standard [`logging.Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter") instances are created. The
configuration sub-dictionary for the third formatter, with id
`custom`, is:

```
{
  '()' : 'my.package.customFormatterFactory',
  'bar' : 'baz',
  'spam' : 99.9,
  'answer' : 42
}
```

and this contains the special key `'()'`, which means that
user-defined instantiation is wanted. In this case, the specified
factory callable will be used. If it is an actual callable it will be
used directly - otherwise, if you specify a string (as in the example)
the actual callable will be located using normal import mechanisms.
The callable will be called with the **remaining** items in the
configuration sub-dictionary as keyword arguments. In the above
example, the formatter with id `custom` will be assumed to be
returned by the call:

```
my.package.customFormatterFactory(bar='baz', spam=99.9, answer=42)
```

Warning

The values for keys such as `bar`, `spam` and `answer` in
the above example should not be configuration dictionaries or references such
as `cfg://foo` or `ext://bar`, because they will not be processed by the
configuration machinery, but passed to the callable as-is.

The key `'()'` has been used as the special key because it is not a
valid keyword parameter name, and so will not clash with the names of
the keyword arguments used in the call. The `'()'` also serves as a
mnemonic that the corresponding value is a callable.

Changed in version 3.11: The `filters` member of `handlers` and `loggers` can take
filter instances in addition to ids.

You can also specify a special key `'.'` whose value is a
mapping of attribute names to values. If found, the specified attributes will
be set on the user-defined object before it is returned. Thus, with the
following configuration:

```
{
  '()' : 'my.package.customForma