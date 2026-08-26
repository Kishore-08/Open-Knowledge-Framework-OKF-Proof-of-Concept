---
id: python-fallback-values-https-docs-python-org-3-library-configparser-caa28eb2
type: concept
title: Fallback Values[¶](https://docs.python.org/3/library/configparser.html#fallback-values
  "Link to this heading")
description: As with a dictionary, you can use a section’s [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get
  "configparser.ConfigParser.get") method to
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/configparser.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Fallback Values[¶](https://docs.python.org/3/library/configparser.html#fallback-values "Link to this heading")

As with a dictionary, you can use a section’s [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get") method to
provide fallback values:

```
>>> topsecret.get('Port')
'50022'
>>> topsecret.get('CompressionLevel')
'9'
>>> topsecret.get('Cipher')
>>> topsecret.get('Cipher', '3des-cbc')
'3des-cbc'
```

Please note that default values have precedence over fallback values.
For instance, in our example the `'CompressionLevel'` key was
specified only in the `'DEFAULT'` section. If we try to get it from
the section `'topsecret.server.example'`, we will always get the default,
even if we specify a fallback:

```
>>> topsecret.get('CompressionLevel', '3')
'9'
```

One more thing to be aware of is that the parser-level [`get()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.get "configparser.ConfigParser.get") method
provides a custom, more complex interface, maintained for backwards
compatibility. When using this method, a fallback value can be provided via
the `fallback` keyword-only argument:

```
>>> config.get('forge.example', 'monster',
...            fallback='No such things as monsters')
'No such things as monsters'
```

The same `fallback` argument can be used with the
[`getint()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getint "configparser.ConfigParser.getint"), [`getfloat()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getfloat "configparser.ConfigParser.getfloat") and
[`getboolean()`](https://docs.python.org/3/library/configparser.html#configparser.ConfigParser.getboolean "configparser.ConfigParser.getboolean") methods, for example:

```
>>> 'BatchMode' in topsecret
False
>>> topsecret.getboolean('BatchMode', fallback=True)
True
>>> config['DEFAULT']['BatchMode'] = 'no'
>>> topsecret.getboolean('BatchMode', fallback=True)
False
```