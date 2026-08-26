---
id: python-exceptions-https-docs-python-org-3-library-configparser-html-caa28eb2
type: concept
title: Exceptions[¶](https://docs.python.org/3/library/configparser.html#exceptions
  "Link to this heading")
description: '*exception* configparser.Error[¶](https://docs.python.org/3/library/configparser.html#configparser.Error
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Exceptions[¶](https://docs.python.org/3/library/configparser.html#exceptions "Link to this heading")

*exception* configparser.Error[¶](https://docs.python.org/3/library/configparser.html#configparser.Error "Link to this definition")
:   Base class for all other `configparser` exceptions.

*exception* configparser.NoSectionError[¶](https://docs.python.org/3/library/configparser.html#configparser.NoSectionError "Link to this definition")
:   Exception raised when a specified section is not found.

*exception* configparser.DuplicateSectionError[¶](https://docs.python.org/3/library/configparser.html#configparser.DuplicateSectionError "Link to this definition")
:   Exception raised if [`add_section()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.add_section "configparser.ConfigParser.add_section") is called with the name of a section
    that is already present or in strict parsers when a section if found more
    than once in a single input file, string or dictionary.

    Changed in version 3.2: Added the optional *source* and *lineno* attributes and parameters to
    `__init__()`.

*exception* configparser.DuplicateOptionError[¶](https://docs.python.org/3/library/configparser.html#configparser.DuplicateOptionError "Link to this definition")
:   Exception raised by strict parsers if a single option appears twice during
    reading from a single file, string or dictionary. This catches misspellings
    and case sensitivity-related errors, e.g. a dictionary may have two keys
    representing the same case-insensitive configuration key.

*exception* configparser.NoOptionError[¶](https://docs.python.org/3/library/configparser.html#configparser.NoOptionError "Link to this definition")
:   Exception raised when a specified option is not found in the specified
    section.

*exception* configparser.InterpolationError[¶](https://docs.python.org/3/library/configparser.html#configparser.InterpolationError "Link to this definition")
:   Base class for exceptions raised when problems occur performing string
    interpolation.

*exception* configparser.InterpolationDepthError[¶](https://docs.python.org/3/library/configparser.html#configparser.InterpolationDepthError "Link to this definition")
:   Exception raised when string interpolation cannot be completed because the
    number of iterations exceeds [`MAX_INTERPOLATION_DEPTH`](https://docs.python.org/3/library/configparser.html#configparser.MAX_INTERPOLATION_DEPTH "configparser.MAX_INTERPOLATION_DEPTH"). Subclass of
    [`InterpolationError`](https://docs.python.org/3/library/configparser.html#configparser.InterpolationError "configparser.InterpolationError").

*exception* configparser.InterpolationMissingOptionError[¶](https://docs.python.org/3/library/configparser.html#configparser.InterpolationMissingOptionError "Link to this definition")
:   Exception raised when an option referenced from a value does not exist.
    Subclass of [`InterpolationError`](https://docs.python.org/3/library/configparser.html#configparser.InterpolationError "configparser.InterpolationError").

*exception* configparser.InterpolationSyntaxError[¶](https://docs.python.org/3/library/configparser.html#configparser.InterpolationSyntaxError "Link to this definition")
:   Exception raised when the source text into which substitutions are made does
    not conform to the required syntax. Subclass of [`InterpolationError`](https://docs.python.org/3/library/configparser.html#configparser.InterpolationError "configparser.InterpolationError").

*exception* configparser.MissingSectionHeaderError[¶](https://docs.python.org/3/library/configparser.html#configparser.MissingSectionHeaderError "Link to this definition")
:   Exception raised when attempting to parse a file which has no section
    headers.

*exception* configparser.ParsingError[¶](https://docs.python.org/3/library/configparser.html#configparser.ParsingError "Link to this definition")
:   Exception raised when errors occur atte