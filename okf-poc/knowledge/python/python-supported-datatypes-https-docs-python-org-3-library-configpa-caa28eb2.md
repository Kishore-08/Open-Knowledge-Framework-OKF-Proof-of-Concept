---
id: python-supported-datatypes-https-docs-python-org-3-library-configpa-caa28eb2
type: concept
title: Supported Datatypes[¶](https://docs.python.org/3/library/configparser.html#supported-datatypes
  "Link to this heading")
description: Config parsers do not guess datatypes of values in configuration files,
  always
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Supported Datatypes[¶](https://docs.python.org/3/library/configparser.html#supported-datatypes "Link to this heading")

Config parsers do not guess datatypes of values in configuration files, always
storing them internally as strings. This means that if you need other
datatypes, you should convert on your own:

```
>>> int(topsecret['Port'])
50022
>>> float(topsecret['CompressionLevel'])
9.0
```

Since this task is so common, config parsers provide a range of handy getter
methods to handle integers, floats and booleans. The last one is the most
interesting because simply passing the value to `bool()` would do no good
since `bool('False')` is still `True`. This is why config parsers also
provide [`getboolean()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "configparser.ConfigParser.getboolean"). This method is case-insensitive and
recognizes Boolean values from `'yes'`/`'no'`, `'on'`/`'off'`,
`'true'`/`'false'` and `'1'`/`'0'` [[1]](https://docs.python.org/3/library/configparser.html#id16). For example:

```
>>> topsecret.getboolean('ForwardX11')
False
>>> config['forge.example'].getboolean('ForwardX11')
True
>>> config.getboolean('forge.example', 'Compression')
True
```

Apart from [`getboolean()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "configparser.ConfigParser.getboolean"), config parsers also
provide equivalent [`getint()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getint "configparser.ConfigParser.getint") and
[`getfloat()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getfloat "configparser.ConfigParser.getfloat") methods. You can register your own
converters and customize the provided ones. [[1]](https://docs.python.org/3/library/configparser.html#id16)