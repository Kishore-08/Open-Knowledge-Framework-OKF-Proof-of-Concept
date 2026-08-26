---
id: python-handler-configuration-order-https-docs-python-org-3-library--fca5b00e
type: concept
title: Handler configuration order[¶](https://docs.python.org/3/library/logging.config.html#handler-configuration-order
  "Link to this heading")
description: Handlers are configured in alphabetical order of their keys, and a configured
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/logging.config.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Handler configuration order[¶](https://docs.python.org/3/library/logging.config.html#handler-configuration-order "Link to this heading")

Handlers are configured in alphabetical order of their keys, and a configured
handler replaces the configuration dictionary in (a working copy of) the
`handlers` dictionary in the schema. If you use a construct such as
`cfg://handlers.foo`, then initially `handlers['foo']` points to the
configuration dictionary for the handler named `foo`, and later (once that
handler has been configured) it points to the configured handler instance.
Thus, `cfg://handlers.foo` could resolve to either a dictionary or a handler
instance. In general, it is wise to name handlers in a way such that dependent
handlers are configured *after* any handlers they depend on; that allows
something like `cfg://handlers.foo` to be used in configuring a handler that
depends on handler `foo`. If that dependent handler were named `bar`,
problems would result, because the configuration of `bar` would be attempted
before that of `foo`, and `foo` would not yet have been configured.
However, if the dependent handler were named `foobar`, it would be configured
after `foo`, with the result that `cfg://handlers.foo` would resolve to
configured handler `foo`, and not its configuration dictionary.