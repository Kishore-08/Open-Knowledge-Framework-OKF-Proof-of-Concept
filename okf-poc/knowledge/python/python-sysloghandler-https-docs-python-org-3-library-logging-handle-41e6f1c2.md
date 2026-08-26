---
id: python-sysloghandler-https-docs-python-org-3-library-logging-handle-41e6f1c2
type: concept
title: SysLogHandler[¶](https://docs.python.org/3/library/logging.handlers.html#sysloghandler
  "Link to this heading")
description: The [`SysLogHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler
  "logging.handlers.SysLogHandler") class, located in the `logging.handlers` module,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## SysLogHandler[¶](https://docs.python.org/3/library/logging.handlers.html#sysloghandler "Link to this heading")

The [`SysLogHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler "logging.handlers.SysLogHandler") class, located in the `logging.handlers` module,
supports sending logging messages to a remote or local Unix syslog.

*class* logging.handlers.SysLogHandler(*address=('localhost', SYSLOG\_UDP\_PORT)*, *facility=LOG\_USER*, *socktype=socket.SOCK\_DGRAM*, *timeout=None*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler "Link to this definition")
:   Returns a new instance of the `SysLogHandler` class intended to
    communicate with a remote Unix machine whose address is given by *address* in
    the form of a `(host, port)` tuple. If *address* is not specified,
    `('localhost', 514)` is used. The address is used to open a socket. An
    alternative to providing a `(host, port)` tuple is providing an address as a
    string, for example ‘/dev/log’. In this case, a Unix domain socket is used to
    send the message to the syslog. If *facility* is not specified,
    `LOG_USER` is used. The type of socket opened depends on the
    *socktype* argument, which defaults to [`socket.SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM") and thus
    opens a UDP socket. To open a TCP socket (for use with the newer syslog
    daemons such as rsyslog), specify a value of [`socket.SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM").
    If *timeout* is specified, it sets a timeout (in seconds) for the socket operations.
    This can help prevent the program from hanging indefinitely if the syslog server is
    unreachable. By default, *timeout* is `None`, meaning no timeout is applied.

    Note that if your server is not listening on UDP port 514,
    `SysLogHandler` may appear not to work. In that case, check what
    address you should be using for a domain socket - it’s system dependent.
    For example, on Linux it’s usually ‘/dev/log’ but on OS/X it’s
    ‘/var/run/syslog’. You’ll need to check your platform and use the
    appropriate address (you may need to do this check at runtime if your
    application needs to run on several platforms). On Windows, you pretty
    much have to use the UDP option.

    Note

    On macOS 12.x (Monterey), Apple has changed the behaviour of their
    syslog daemon - it no longer listens on a domain socket. Therefore, you cannot
    expect `SysLogHandler` to work on this system.

    See [gh-91070](https://github.com/python/cpython/issues/91070) for more information.

    Changed in version 3.2: *socktype* was added.

    Changed in version 3.14: *timeout* was added.

    close()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler.close "Link to this definition")
    :   Closes the socket to the remote host.

    createSocket()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler.createSocket "Link to this definition")
    :   Tries to create a socket and, if it’s not a datagram socket, connect it
        to the other end. This method is called during handler initialization,
        but it’s not regarded as an error if the other end isn’t listening at
        this point - the method will be called again when emitting an event, if
        there is no socket at that point.

        Added in version 3.11.

    emit(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SysLogHandler.emit "Link to this definition")
    :   The record is formatted, and then sent to the syslog server. If exception
        information is present, it is *not* sent to the server.

        Changed in version 3.2.1: (See: [bpo-12168](https://bugs.python.org/issue?@action=redirect&bpo=12168).) In earlier versions, the message sent to the