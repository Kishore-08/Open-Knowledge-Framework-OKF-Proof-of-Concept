---
id: python-httphandler-https-docs-python-org-3-library-logging-handlers-41e6f1c2
type: concept
title: HTTPHandler[¶](https://docs.python.org/3/library/logging.handlers.html#httphandler
  "Link to this heading")
description: The [`HTTPHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.HTTPHandler
  "logging.handlers.HTTPHandler") class, located in the `logging.handlers` module,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## HTTPHandler[¶](https://docs.python.org/3/library/logging.handlers.html#httphandler "Link to this heading")

The [`HTTPHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.HTTPHandler "logging.handlers.HTTPHandler") class, located in the `logging.handlers` module,
supports sending logging messages to a web server, using either `GET` or
`POST` semantics.

*class* logging.handlers.HTTPHandler(*host*, *url*, *method='GET'*, *secure=False*, *credentials=None*, *context=None*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.HTTPHandler "Link to this definition")
:   Returns a new instance of the `HTTPHandler` class. The *host* can be
    of the form `host:port`, should you need to use a specific port number. If
    no *method* is specified, `GET` is used. If *secure* is true, a HTTPS
    connection will be used. The *context* parameter may be set to a
    [`ssl.SSLContext`](https://docs.python.org/3/library/ssl.html#ssl.SSLContext "ssl.SSLContext") instance to configure the SSL settings used for the
    HTTPS connection. If *credentials* is specified, it should be a 2-tuple
    consisting of userid and password, which will be placed in a HTTP
    ‘Authorization’ header using Basic authentication. If you specify
    credentials, you should also specify secure=True so that your userid and
    password are not passed in cleartext across the wire.

    Changed in version 3.5: The *context* parameter was added.

    mapLogRecord(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.HTTPHandler.mapLogRecord "Link to this definition")
    :   Provides a dictionary, based on `record`, which is to be URL-encoded
        and sent to the web server. The default implementation just returns
        `record.__dict__`. This method can be overridden if e.g. only a
        subset of [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") is to be sent to the web server, or
        if more specific customization of what’s sent to the server is required.

    emit(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.HTTPHandler.emit "Link to this definition")
    :   Sends the record to the web server as a URL-encoded dictionary. The
        [`mapLogRecord()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.HTTPHandler.mapLogRecord "logging.handlers.HTTPHandler.mapLogRecord") method is used to convert the record to the
        dictionary to be sent.

    Note

    Since preparing a record for sending it to a web server is not
    the same as a generic formatting operation, using
    [`setFormatter()`](https://docs.python.org/3/library/logging.html#logging.Handler.setFormatter "logging.Handler.setFormatter") to specify a
    [`Formatter`](https://docs.python.org/3/library/logging.html#logging.Formatter "logging.Formatter") for a `HTTPHandler` has no effect.
    Instead of calling [`format()`](https://docs.python.org/3/library/logging.html#logging.Handler.format "logging.Handler.format"), this handler calls
    [`mapLogRecord()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.HTTPHandler.mapLogRecord "logging.handlers.HTTPHandler.mapLogRecord") and then [`urllib.parse.urlencode()`](https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlencode "urllib.parse.urlencode") to encode the
    dictionary in a form suitable for sending to a web server.