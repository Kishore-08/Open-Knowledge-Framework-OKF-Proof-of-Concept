---
id: python-customizing-parser-behaviour-https-docs-python-org-3-library-caa28eb2
type: concept
title: Customizing Parser Behaviour[¶](https://docs.python.org/3/library/configparser.html#customizing-parser-behaviour
  "Link to this heading")
description: There are nearly as many INI format variants as there are applications
  using it.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Customizing Parser Behaviour[¶](https://docs.python.org/3/library/configparser.html#customizing-parser-behaviour "Link to this heading")

There are nearly as many INI format variants as there are applications using it.
`configparser` goes a long way to provide support for the largest sensible
set of INI styles available. The default functionality is mainly dictated by
historical background and it’s very likely that you will want to customize some
of the features.

The most common way to change the way a specific config parser works is to use
the `__init__()` options:

- *defaults*, default value: `None`

  This option accepts a dictionary of key-value pairs which will be initially
  put in the `DEFAULT` section. This makes for an elegant way to support
  concise configuration files that don’t specify values which are the same as
  the documented default.

  Hint: if you want to specify default values for a specific section, use
  [`read_dict()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.read_dict "configparser.ConfigParser.read_dict") before you read the actual file.
- *dict\_type*, default value: [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "dict")

  This option has a major impact on how the mapping protocol will behave and how
  the written configuration files look. With the standard dictionary, every
  section is stored in the order they were added to the parser. Same goes for
  options within sections.

  An alternative dictionary type can be used for example to sort sections and
  options on write-back.

  Please note: there are ways to add a set of key-value pairs in a single
  operation. When you use a regular dictionary in those operations, the order
  of the keys will be ordered. For example:

  ```
  >>> parser = configparser.ConfigParser()
  >>> parser.read_dict({'section1': {'key1': 'value1',
  ...                                'key2': 'value2',
  ...                                'key3': 'value3'},
  ...                   'section2': {'keyA': 'valueA',
  ...                                'keyB': 'valueB',
  ...                                'keyC': 'valueC'},
  ...                   'section3': {'foo': 'x',
  ...                                'bar': 'y',
  ...                                'baz': 'z'}
  ... })
  >>> parser.sections()
  ['section1', 'section2', 'section3']
  >>> [option for option in parser['section3']]
  ['foo', 'bar', 'baz']
  ```
- *allow\_no\_value*, default value: `False`

  Some configuration files are known to include settings without values, but
  which otherwise conform to the syntax supported by `configparser`. The
  *allow\_no\_value* parameter to the constructor can be used to
  indicate that such values should be accepted:

  ```
  >>> import configparser

  >>> sample_config = """
  ... [mysqld]
  ...   user = mysql
  ...   pid-file = /var/run/mysqld/mysqld.pid
  ...   skip-external-locking
  ...   old_passwords = 1
  ...   skip-bdb
  ...   # we don't need ACID today
  ...   skip-innodb
  ... """
  >>> config = configparser.ConfigParser(allow_no_value=True)
  >>> config.read_string(sample_config)

  >>> # Settings with values are treated as before:
  >>> config["mysqld"]["user"]
  'mysql'

  >>> # Settings without values provide None:
  >>> config["mysqld"]["skip-bdb"]

  >>> # Settings which aren't specified still raise an error:
  >>> config["mysqld"]["does-not-exist"]
  Traceback (most recent call last):
    ...
  KeyError: 'does-not-exist'
  ```
- *delimiters*, default value: `('=', ':')`

  Delimiters are substrings that delimit keys from values within a section.
  The first occurrence of a delimiting substring on a line is considered
  a delimiter. This means values (but not keys) can contain the delimiters.

  See also the *space\_around\_delimiters* argument to
  [`ConfigParser.write()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.write "configparser.ConfigParser.write").
- *commen