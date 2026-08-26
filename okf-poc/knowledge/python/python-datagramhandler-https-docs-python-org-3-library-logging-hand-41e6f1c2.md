---
id: python-datagramhandler-https-docs-python-org-3-library-logging-hand-41e6f1c2
type: concept
title: DatagramHandler[¶](https://docs.python.org/3/library/logging.handlers.html#datagramhandler
  "Link to this heading")
description: The [`DatagramHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.DatagramHandler
  "logging.handlers.DatagramHandler") class, located in the `logging.handlers`
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## DatagramHandler[¶](https://docs.python.org/3/library/logging.handlers.html#datagramhandler "Link to this heading")

The [`DatagramHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.DatagramHandler "logging.handlers.DatagramHandler") class, located in the `logging.handlers`
module, inherits from [`SocketHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler "logging.handlers.SocketHandler") to support sending logging messages
over UDP sockets.

*class* logging.handlers.DatagramHandler(*host*, *port*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.DatagramHandler "Link to this definition")
:   Returns a new instance of the `DatagramHandler` class intended to
    communicate with a remote machine whose address is given by *host* and *port*.

    Note

    As UDP is not a streaming protocol, there is no persistent connection
    between an instance of this handler and *host*. For this reason, when using a
    network socket, a DNS lookup might have to be made each time an event is
    logged, which can introduce some latency into the system. If this affects you,
    you can do a lookup yourself and initialize this handler using the looked-up IP
    address rather than the hostname.

    Changed in version 3.4: If `port` is specified as `None`, a Unix domain socket is created
    using the value in `host` - otherwise, a UDP socket is created.

    emit()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.DatagramHandler.emit "Link to this definition")
    :   Pickles the record’s attribute dictionary and writes it to the socket in
        binary format. If there is an error with the socket, silently drops the
        packet. To unpickle the record at the receiving end into a
        [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord"), use the [`makeLogRecord()`](https://docs.python.org/3/library/logging.html#logging.makeLogRecord "logging.makeLogRecord")
        function.

    makeSocket()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.DatagramHandler.makeSocket "Link to this definition")
    :   The factory method of [`SocketHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler "logging.handlers.SocketHandler") is here overridden to create
        a UDP socket ([`socket.SOCK_DGRAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_DGRAM "socket.SOCK_DGRAM")).

    send(*s*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.DatagramHandler.send "Link to this definition")
    :   Send a pickled byte-string to a socket. The format of the sent byte-string
        is as described in the documentation for [`SocketHandler.makePickle()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.makePickle "logging.handlers.SocketHandler.makePickle").