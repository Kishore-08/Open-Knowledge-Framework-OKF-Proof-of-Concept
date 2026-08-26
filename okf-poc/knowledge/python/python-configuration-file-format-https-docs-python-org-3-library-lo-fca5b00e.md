---
id: python-configuration-file-format-https-docs-python-org-3-library-lo-fca5b00e
type: concept
title: Configuration file format[¶](https://docs.python.org/3/library/logging.config.html#configuration-file-format
  "Link to this heading")
description: The configuration file format understood by [`fileConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig
  "logging.config.fileConfig") is based on
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.config.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Configuration file format[¶](https://docs.python.org/3/library/logging.config.html#configuration-file-format "Link to this heading")

The configuration file format understood by [`fileConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "logging.config.fileConfig") is based on
[`configparser`](https://docs.python.org/3/library/configparser.html#module-configparser "configparser: Configuration file parser.") functionality. The file must contain sections called
`[loggers]`, `[handlers]` and `[formatters]` which identify by name the
entities of each type which are defined in the file. For each such entity, there
is a separate section which identifies how that entity is configured. Thus, for
a logger named `log01` in the `[loggers]` section, the relevant
configuration details are held in a section `[logger_log01]`. Similarly, a
handler called `hand01` in the `[handlers]` section will have its
configuration held in a section called `[handler_hand01]`, while a formatter
called `form01` in the `[formatters]` section will have its configuration
specified in a section called `[formatter_form01]`. The root logger
configuration must be specified in a section called `[logger_root]`.

Note

The [`fileConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "logging.config.fileConfig") API is older than the [`dictConfig()`](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig "logging.config.dictConfig") API and does
not provide functionality to cover certain aspects of logging. For example,
you cannot configure [`Filter`](https://docs.python.org/3/library/logging.html#logging.Filter "logging.Filter") objects, which provide for
filtering of messages beyond simple integer levels, using `fileConfig()`.
If you need to have instances of `Filter` in your logging
configuration, you will need to use `dictConfig()`. Note that future
enhancements to configuration functionality will be added to
`dictConfig()`, so it’s worth considering transitioning to this newer
API when it’s convenient to do so.

Examples of these sections in the file are given below.

```
[loggers]
keys=root,log02,log03,log04,log05,log06,log07

[handlers]
keys=hand01,hand02,hand03,hand04,hand05,hand06,hand07,hand08,hand09

[formatters]
keys=form01,form02,form03,form04,form05,form06,form07,form08,form09
```

The root logger must specify a level and a list of handlers. An example of a
root logger section is given below.

```
[logger_root]
level=NOTSET
handlers=hand01
```

The `level` entry can be one of `DEBUG, INFO, WARNING, ERROR, CRITICAL` or
`NOTSET`. For the root logger only, `NOTSET` means that all messages will be
logged. Level values are [evaluated](https://docs.python.org/3/library/functions.html#func-eval) in the context of the `logging`
package’s namespace.

The `handlers` entry is a comma-separated list of handler names, which must
appear in the `[handlers]` section. These names must appear in the
`[handlers]` section and have corresponding sections in the configuration
file.

For loggers other than the root logger, some additional information is required.
This is illustrated by the following example.

```
[logger_parser]
level=DEBUG
handlers=hand01
propagate=1
qualname=compiler.parser
```

The `level` and `handlers` entries are interpreted as for the root logger,
except that if a non-root logger’s level is specified as `NOTSET`, the system
consults loggers higher up the hierarchy to determine the effective level of the
logger. The `propagate` entry is set to 1 to indicate that messages must
propagate to handlers higher up the logger hierarchy from this logger, or 0 to
indicate that messages are **not** propagated to handlers up the hierarchy. The
`qualname` entry is the hierarchical channel name of the logger, that is to
say the name used by the application to get the logger.

Sections which specify handler configuration are exemplified by the following.

```
[handler_h