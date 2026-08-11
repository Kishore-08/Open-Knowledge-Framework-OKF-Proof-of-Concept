---
id: python-startup-hooks-https-docs-python-org-3-library-readline-html--0c2cb825
type: concept
title: Startup hooks[¶](https://docs.python.org/3/library/readline.html#startup-hooks
  "Link to this heading")
description: readline.set\_startup\_hook([*function*])[¶](https://docs.python.org/3/library/readline.html#readline.set_startup_hook
  "Link to this definition")
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/readline.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Startup hooks[¶](https://docs.python.org/3/library/readline.html#startup-hooks "Link to this heading")

readline.set\_startup\_hook([*function*])[¶](https://docs.python.org/3/library/readline.html#readline.set_startup_hook "Link to this definition")
:   Set or remove the function invoked by the `rl_startup_hook`
    callback of the underlying library. If *function* is specified, it will
    be used as the new hook function; if omitted or `None`, any function
    already installed is removed. The hook is called with no
    arguments just before readline prints the first prompt.

readline.set\_pre\_input\_hook([*function*])[¶](https://docs.python.org/3/library/readline.html#readline.set_pre_input_hook "Link to this definition")
:   Set or remove the function invoked by the `rl_pre_input_hook`
    callback of the underlying library. If *function* is specified, it will
    be used as the new hook function; if omitted or `None`, any
    function already installed is removed. The hook is called
    with no arguments after the first prompt has been printed and just before
    readline starts reading input characters. This function only exists
    if Python was compiled for a version of the library that supports it.