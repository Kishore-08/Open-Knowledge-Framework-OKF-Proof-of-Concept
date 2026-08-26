---
id: python-sockethandler-https-docs-python-org-3-library-logging-handle-41e6f1c2
type: concept
title: SocketHandler[¶](https://docs.python.org/3/library/logging.handlers.html#sockethandler
  "Link to this heading")
description: The [`SocketHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler
  "logging.handlers.SocketHandler") class, located in the `logging.handlers` module,
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.handlers.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## SocketHandler[¶](https://docs.python.org/3/library/logging.handlers.html#sockethandler "Link to this heading")

The [`SocketHandler`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler "logging.handlers.SocketHandler") class, located in the `logging.handlers` module,
sends logging output to a network socket. The base class uses a TCP socket.

*class* logging.handlers.SocketHandler(*host*, *port*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler "Link to this definition")
:   Returns a new instance of the `SocketHandler` class intended to
    communicate with a remote machine whose address is given by *host* and *port*.

    Changed in version 3.4: If `port` is specified as `None`, a Unix domain socket is created
    using the value in `host` - otherwise, a TCP socket is created.

    close()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.close "Link to this definition")
    :   Closes the socket.

    emit()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.emit "Link to this definition")
    :   Pickles the record’s attribute dictionary and writes it to the socket in
        binary format. If there is an error with the socket, silently drops the
        packet. If the connection was previously lost, re-establishes the
        connection. To unpickle the record at the receiving end into a
        [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord"), use the [`makeLogRecord()`](https://docs.python.org/3/library/logging.html#logging.makeLogRecord "logging.makeLogRecord")
        function.

    handleError()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.handleError "Link to this definition")
    :   Handles an error which has occurred during [`emit()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.emit "logging.handlers.SocketHandler.emit"). The most likely
        cause is a lost connection. Closes the socket so that we can retry on the
        next event.

    makeSocket()[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.makeSocket "Link to this definition")
    :   This is a factory method which allows subclasses to define the precise
        type of socket they want. The default implementation creates a TCP socket
        ([`socket.SOCK_STREAM`](https://docs.python.org/3/library/socket.html#socket.SOCK_STREAM "socket.SOCK_STREAM")).

    makePickle(*record*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.makePickle "Link to this definition")
    :   Pickles the record’s attribute dictionary in binary format with a length
        prefix, and returns it ready for transmission across the socket. The
        details of this operation are equivalent to:

        ```
        data = pickle.dumps(record_attr_dict, 1)
        datalen = struct.pack('>L', len(data))
        return datalen + data
        ```

        Note that pickles aren’t completely secure. If you are concerned about
        security, you may want to override this method to implement a more secure
        mechanism. For example, you can sign pickles using HMAC and then verify
        them on the receiving end, or alternatively you can disable unpickling of
        global objects on the receiving end.

    send(*packet*)[¶](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.send "Link to this definition")
    :   Send a pickled byte-string *packet* to the socket. The format of the sent
        byte-string is as described in the documentation for
        [`makePickle()`](https://docs.python.org/3/library/logging.handlers.html#logging.handlers.SocketHandler.makePickle "logging.handlers.SocketHandler.makePickle").

        This function allows for partial sends, wh