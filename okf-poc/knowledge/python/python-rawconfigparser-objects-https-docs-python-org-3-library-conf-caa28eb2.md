---
id: python-rawconfigparser-objects-https-docs-python-org-3-library-conf-caa28eb2
type: concept
title: RawConfigParser Objects[¶](https://docs.python.org/3/library/configparser.html#rawconfigparser-objects
  "Link to this heading")
description: '*class* configparser.RawConfigParser(*defaults=None*, *dict\_type=dict*,
  *allow\_no\_value=False*, *\**, *delimiters=(''='', '':'')*, *comment\_prefixes=(''#'',
  '';'')*, *inline\_comment\_prefixes=None*, *str'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## RawConfigParser Objects[¶](https://docs.python.org/3/library/configparser.html#rawconfigparser-objects "Link to this heading")

*class* configparser.RawConfigParser(*defaults=None*, *dict\_type=dict*, *allow\_no\_value=False*, *\**, *delimiters=('=', ':')*, *comment\_prefixes=('#', ';')*, *inline\_comment\_prefixes=None*, *strict=True*, *empty\_lines\_in\_values=True*, *default\_section=configparser.DEFAULTSECT*, *interpolation=BasicInterpolation()*, *converters={}*, *allow\_unnamed\_section=False*)[¶](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser "Link to this definition")
:   Legacy variant of the [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser"). It has interpolation
    disabled by default and allows for non-string section names, option
    names, and values via its unsafe `add_section` and `set` methods,
    as well as the legacy `defaults=` keyword argument handling.

    Changed in version 3.2: *allow\_no\_value*, *delimiters*, *comment\_prefixes*, *strict*,
    *empty\_lines\_in\_values*, *default\_section* and *interpolation* were
    added.

    Changed in version 3.5: The *converters* argument was added.

    Changed in version 3.8: The default *dict\_type* is [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict"), since it now preserves
    insertion order.

    Changed in version 3.13: The *allow\_unnamed\_section* argument was added.

    Note

    Consider using [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser") instead which checks types of
    the values to be stored internally. If you don’t want interpolation, you
    can use `ConfigParser(interpolation=None)`.

    add\_section(*section*)[¶](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser.add_section "Link to this definition")
    :   Add a section named *section* or [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION") to the instance.

        If the given section already exists, [`DuplicateSectionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateSectionError "configparser.DuplicateSectionError") is
        raised. If the *default section* name is passed, [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError") is
        raised. If [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION") is passed and support is disabled,
        [`UnnamedSectionDisabledError`](https://docs.python.org/3/library/configparser.html#configparser.UnnamedSectionDisabledError "configparser.UnnamedSectionDisabledError") is raised.

        Type of *section* is not checked which lets users create non-string named
        sections. This behaviour is unsupported and may cause internal errors.

    Changed in version 3.14: Added support for [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION").

    set(*section*, *option*, *value*)[¶](https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser.set "Link to this definition")
    :   If the given section exists, set the given option to the specified value;
        otherwise raise [`NoSectionError`](https://docs.python.org/3/library/configparser.html#configparser.NoSectionError "configparser.NoSectionError"). While it is possible to use
        `RawConfigParser` (or [`ConfigParser`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "configparser.ConfigParser") with *raw* parameters
        set to true) for *internal* storage of non-string values, full
        functionality (including interpolation and output to files) can only be
        achieved using string values