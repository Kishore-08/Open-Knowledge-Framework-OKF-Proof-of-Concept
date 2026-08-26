---
id: python-smtphandler-https-docs-python-org-3-library-logging-handlers-41e6f1c2
type: concept
title: SMTPHandler[¶](https://docs.python.org/3/library/logging.handlers.html#smtphandler
  "Link to this heading")
description: The [`SMTPHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler
  "logging.handlers.SMTPHandler") class, located in the `logging.handlers` module,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## SMTPHandler[¶](https://docs.python.org/3/library/logging.handlers.html#smtphandler "Link to this heading")

The [`SMTPHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler "logging.handlers.SMTPHandler") class, located in the `logging.handlers` module,
supports sending logging messages to an email address via SMTP.

*class* logging.handlers.SMTPHandler(*mailhost*, *fromaddr*, *toaddrs*, *subject*, *credentials=None*, *secure=None*, *timeout=1.0*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler "Link to this definition")
:   Returns a new instance of the `SMTPHandler` class. The instance is
    initialized with the from and to addresses and subject line of the email. The
    *toaddrs* should be a list of strings. To specify a non-standard SMTP port, use
    the (host, port) tuple format for the *mailhost* argument. If you use a string,
    the standard SMTP port is used. If your SMTP server requires authentication, you
    can specify a (username, password) tuple for the *credentials* argument.

    To specify the use of a secure protocol (TLS), pass in a tuple to the
    *secure* argument. This will only be used when authentication credentials are
    supplied. The tuple should be either an empty tuple, or a single-value tuple
    with the name of a keyfile, or a 2-value tuple with the names of the keyfile
    and certificate file. (This tuple is passed to the
    [`smtplib.SMTP.starttls()`](https://docs.python.org/3/library/smtplib.html#smtplib.SMTP.starttls "smtplib.SMTP.starttls") method.)

    A timeout can be specified for communication with the SMTP server using the
    *timeout* argument.

    Changed in version 3.3: Added the *timeout* parameter.

    emit(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler.emit "Link to this definition")
    :   Formats the record and sends it to the specified addressees.

    getSubject(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SMTPHandler.getSubject "Link to this definition")
    :   If you want to specify a subject line which is record-dependent, override
        this method.