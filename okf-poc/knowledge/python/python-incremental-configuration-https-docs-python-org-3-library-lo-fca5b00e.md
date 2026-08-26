---
id: python-incremental-configuration-https-docs-python-org-3-library-lo-fca5b00e
type: concept
title: Incremental Configuration[¶](https://docs.python.org/3/library/logging.config.html#incremental-configuration
  "Link to this heading")
description: It is difficult to provide complete flexibility for incremental
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.config.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Incremental Configuration[¶](https://docs.python.org/3/library/logging.config.html#incremental-configuration "Link to this heading")

It is difficult to provide complete flexibility for incremental
configuration. For example, because objects such as filters
and formatters are anonymous, once a configuration is set up, it is
not possible to refer to such anonymous objects when augmenting a
configuration.

Furthermore, there is not a compelling case for arbitrarily altering
the object graph of loggers, handlers, filters, formatters at
run-time, once a configuration is set up; the verbosity of loggers and
handlers can be controlled just by setting levels (and, in the case of
loggers, propagation flags). Changing the object graph arbitrarily in
a safe way is problematic in a multi-threaded environment; while not
impossible, the benefits are not worth the complexity it adds to the
implementation.

Thus, when the `incremental` key of a configuration dict is present
and is `True`, the system will completely ignore any `formatters` and
`filters` entries, and process only the `level`
settings in the `handlers` entries, and the `level` and
`propagate` settings in the `loggers` and `root` entries.

Using a value in the configuration dict lets configurations to be sent
over the wire as pickled dicts to a socket listener. Thus, the logging
verbosity of a long-running application can be altered over time with
no need to stop and restart the application.