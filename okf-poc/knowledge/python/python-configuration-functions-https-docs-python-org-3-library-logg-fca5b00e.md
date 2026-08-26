---
id: python-configuration-functions-https-docs-python-org-3-library-logg-fca5b00e
type: concept
title: Configuration functions[¶](https://docs.python.org/3/library/logging.config.html#configuration-functions
  "Link to this heading")
description: The following functions configure the logging module. They are located
  in the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.config.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Configuration functions[¶](https://docs.python.org/3/library/logging.config.html#configuration-functions "Link to this heading")

The following functions configure the logging module. They are located in the
`logging.config` module. Their use is optional — you can configure the
logging module using these functions or by making calls to the main API (defined
in [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.") itself) and defining handlers which are declared either in
`logging` or [`logging.handlers`](https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers "logging.handlers: Handlers for the logging module.").

logging.config.dictConfig(*config*)[¶](https://docs.python.org/3/library/logging.config.html#logging.config.dictConfig "Link to this definition")
:   Takes the logging configuration from a dictionary. The contents of
    this dictionary are described in [Configuration dictionary schema](https://docs.python.org/3/library/logging.config.html#logging-config-dictschema)
    below.

    If an error is encountered during configuration, this function will
    raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "ValueError"), [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError"), [`AttributeError`](https://docs.python.org/3/library/exceptions.html#AttributeError "AttributeError")
    or [`ImportError`](https://docs.python.org/3/library/exceptions.html#ImportError "ImportError") with a suitably descriptive message. The
    following is a (possibly incomplete) list of conditions which will
    raise an error:

    - A `level` which is not a string or which is a string not
      corresponding to an actual logging level.
    - A `propagate` value which is not a boolean.
    - An id which does not have a corresponding destination.
    - A non-existent handler id found during an incremental call.
    - An invalid logger name.
    - Inability to resolve to an internal or external object.

    Parsing is performed by the `DictConfigurator` class, whose
    constructor is passed the dictionary used for configuration, and
    has a `configure()` method. The `logging.config` module
    has a callable attribute `dictConfigClass`
    which is initially set to `DictConfigurator`.
    You can replace the value of `dictConfigClass` with a
    suitable implementation of your own.

    `dictConfig()` calls `dictConfigClass` passing
    the specified dictionary, and then calls the `configure()` method on
    the returned object to put the configuration into effect:

    ```
    def dictConfig(config):
        dictConfigClass(config).configure()
    ```

    For example, a subclass of `DictConfigurator` could call
    `DictConfigurator.__init__()` in its own `__init__()`, then
    set up custom prefixes which would be usable in the subsequent
    `configure()` call. `dictConfigClass` would be bound to
    this new subclass, and then `dictConfig()` could be called exactly as
    in the default, uncustomized state.

    Added in version 3.2.

logging.config.fileConfig(*fname*, *defaults=None*, *disable\_existing\_loggers=True*, *encoding=None*)[¶](https://docs.python.org/3/library/logging.config.html#logging.config.fileConfig "Link to this definition")
:   Reads the logging configuration from a [`configparser`](https://docs.python.org/3/library/configparser.html#module-configparser "configparser: Configuration file parser.")-format file. The
    format of the file should be as described in
    [Configuration file format](https://docs.python.org/3/library/logging.config.html#logging-config-fileformat).
    This function can be called several times from an application, allowing an
    end user to select from various pre-canned configurations (if the developer
    provides a mechanism to present the choices and load the chosen
    configuration).

    It will raise [`FileNotFoundE