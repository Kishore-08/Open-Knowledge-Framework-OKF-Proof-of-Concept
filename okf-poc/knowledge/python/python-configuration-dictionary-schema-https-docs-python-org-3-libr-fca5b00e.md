---
id: python-configuration-dictionary-schema-https-docs-python-org-3-libr-fca5b00e
type: concept
title: Configuration dictionary schema[¶](https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema
  "Link to this heading")
description: Describing a logging configuration requires listing the various
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.config.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Configuration dictionary schema[¶](https://docs.python.org/3/library/logging.config.html#configuration-dictionary-schema "Link to this heading")

Describing a logging configuration requires listing the various
objects to create and the connections between them; for example, you
may create a handler named ‘console’ and then say that the logger
named ‘startup’ will send its messages to the ‘console’ handler.
These objects aren’t limited to those provided by the [`logging`](https://docs.python.org/3/library/logging.html#module-logging "logging: Flexible event logging system for applications.")
module because you might write your own formatter or handler class.
The parameters to these classes may also need to include external
objects such as `sys.stderr`. The syntax for describing these
objects and connections is defined in [Object connections](https://docs.python.org/3/library/logging.config.html#logging-config-dict-connections)
below.