---
id: python-supported-ini-file-structure-https-docs-python-org-3-library-caa28eb2
type: concept
title: Supported INI File Structure[¶](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure
  "Link to this heading")
description: A configuration file consists of sections, each led by a `[section]`
  header,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Supported INI File Structure[¶](https://docs.python.org/3/library/configparser.html#supported-ini-file-structure "Link to this heading")

A configuration file consists of sections, each led by a `[section]` header,
followed by key/value entries separated by a specific string (`=` or `:` by
default [[1]](https://docs.python.org/3/library/configparser.html#id16)). By default, section names are case sensitive but keys are not
[[1]](https://docs.python.org/3/library/configparser.html#id16). Leading and trailing whitespace is removed from keys and values.
Values can be omitted if the parser is configured to allow it [[1]](https://docs.python.org/3/library/configparser.html#id16),
in which case the key/value delimiter may also be left
out. Values can also span multiple lines, as long as they are indented deeper
than the first line of the value. Depending on the parser’s mode, blank lines
may be treated as parts of multiline values or ignored.

By default, a valid section name can be any string that does not contain ‘\n’.
To change this, see [`ConfigParser.SECTCRE`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.SECTCRE "configparser.ConfigParser.SECTCRE").

The first section name may be omitted if the parser is configured to allow an
unnamed top level section with `allow_unnamed_section=True`. In this case,
the keys/values may be retrieved by [`UNNAMED_SECTION`](https://docs.python.org/3/library/configparser.html#configparser.UNNAMED_SECTION "configparser.UNNAMED_SECTION") as in
`config[UNNAMED_SECTION]`.

Configuration files may include comments, prefixed by specific
characters (`#` and `;` by default [[1]](https://docs.python.org/3/library/configparser.html#id16)). Comments may appear on
their own on an otherwise empty line, possibly indented. [[1]](https://docs.python.org/3/library/configparser.html#id16)

For example:

```
[Simple Values]
key=value
spaces in keys=allowed
spaces in values=allowed as well
spaces around the delimiter = obviously
you can also use : to delimit keys from values

[All Values Are Strings]
values like this: 1000000
or this: 3.14159265359
are they treated as numbers? : no
integers, floats and booleans are held as: strings
can use the API to get converted values directly: true

[Multiline Values]
chorus: I'm a lumberjack, and I'm okay
    I sleep all night and I work all day

[No Values]
key_without_value
empty string value here =

[You can use comments]
# like this
; or this

# By default only in an empty line.
# Inline comments can be harmful because they prevent users
# from using the delimiting characters as parts of values.
# That being said, this can be customized.

    [Sections Can Be Indented]
        can_values_be_as_well = True
        does_that_mean_anything_special = False
        purpose = formatting for readability
        multiline_values = are
            handled just fine as
            long as they are indented
            deeper than the first line
            of a value
        # Did I mention we can indent comments, too?
```