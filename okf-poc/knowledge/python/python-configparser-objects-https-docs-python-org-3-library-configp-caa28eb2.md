---
id: python-configparser-objects-https-docs-python-org-3-library-configp-caa28eb2
type: concept
title: ConfigParser Objects[¶](https://docs.python.org/3/library/configparser.html#configparser-objects
  "Link to this heading")
description: '*class* configparser.ConfigParser(*defaults=None*, *dict\_type=dict*,
  *allow\_no\_value=False*, *\**, *delimiters=(''='', '':'')*, *comment\_prefixes=(''#'',
  '';'')*, *inline\_comment\_prefixes=None*, *strict'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## ConfigParser Objects[¶](https://docs.python.org/3/library/configparser.html#configparser-objects "Link to this heading")

*class* configparser.ConfigParser(*defaults=None*, *dict\_type=dict*, *allow\_no\_value=False*, *\**, *delimiters=('=', ':')*, *comment\_prefixes=('#', ';')*, *inline\_comment\_prefixes=None*, *strict=True*, *empty\_lines\_in\_values=True*, *default\_section=configparser.DEFAULTSECT*, *interpolation=BasicInterpolation()*, *converters={}*, *allow\_unnamed\_section=False*)[¶](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser "Link to this definition")
:   The main configuration parser. When *defaults* is given, it is initialized
    into the dictionary of intrinsic defaults. When *dict\_type* is given, it
    will be used to create the dictionary objects for the list of sections, for
    the options within a section, and for the default values.

    When *delimiters* is given, it is used as the set of substrings that
    divide keys from values. When *comment\_prefixes* is given, it will be used
    as the set of substrings that prefix comments in otherwise empty lines.
    Comments can be indented. When *inline\_comment\_prefixes* is given, it will
    be used as the set of substrings that prefix comments in non-empty lines.

    When *strict* is `True` (the default), the parser won’t allow for
    any section or option duplicates while reading from a single source (file,
    string or dictionary), raising [`DuplicateSectionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateSectionError "configparser.DuplicateSectionError") or
    [`DuplicateOptionError`](https://docs.python.org/3/library/configparser.html#configparser.DuplicateOptionError "configparser.DuplicateOptionError"). When *empty\_lines\_in\_values* is `False`
    (default: `True`), each empty line marks the end of an option. Otherwise,
    internal empty lines of a multiline option are kept as part of the value.
    When *allow\_no\_value* is `True` (default: `False`), options without
    values are accepted; the value held for these is `None` and they are
    serialized without the trailing delimiter.

    When *default\_section* is given, it specifies the name for the special
    section holding default values for other sections and interpolation purposes
    (normally named `"DEFAULT"`). This value can be retrieved and changed at
    runtime using the `default_section` instance attribute. This won’t
    re-evaluate an already parsed config file, but will be used when writing
    parsed settings to a new config file.

    Interpolation behaviour may be customized by providing a custom handler
    through the *interpolation* argument. `None` can be used to turn off
    interpolation completely, `ExtendedInterpolation()` provides a more
    advanced variant inspired by `zc.buildout`. More on the subject in the
    [dedicated documentation section](https://docs.python.org/3/library/configparser.html#interpolation-of-values).

    All option names used in interpolation will be passed through the
    [`optionxform()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.optionxform "configparser.ConfigParser.optionxform") method just like any other option name reference. For
    example, using the default implementation of `optionxform()` (which
    converts option names to lower case), the values `foo %(bar)s` and `foo
    %(BAR)s` are equivalent.

    When *converters* is given, it should be a dictionary where each key
    represents the name of a type converter and each value is a callable
    implementing the conversion from string to the desired datatype. Every
    converter gets its own corresponding `get*()` method on the parser
    object and section proxies.

    When *allow\_unnamed\_section* is `True` (default: `False`),
    the first section name can be omitted. See the
    [“Unnamed Sections” section](https://docs.python.org/3/library/configparser.html#