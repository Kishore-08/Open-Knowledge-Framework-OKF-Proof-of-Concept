---
id: python-line-buffer-https-docs-python-org-3-library-readline-html-li-0c2cb825
type: concept
title: Line buffer[¶](https://docs.python.org/3/library/readline.html#line-buffer
  "Link to this heading")
description: 'The following functions operate on the line buffer:'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/readline.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Line buffer[¶](https://docs.python.org/3/library/readline.html#line-buffer "Link to this heading")

The following functions operate on the line buffer:

readline.get\_line\_buffer()[¶](https://docs.python.org/3/library/readline.html#readline.get_line_buffer "Link to this definition")
:   Return the current contents of the line buffer (`rl_line_buffer`
    in the underlying library).

readline.insert\_text(*string*)[¶](https://docs.python.org/3/library/readline.html#readline.insert_text "Link to this definition")
:   Insert text into the line buffer at the cursor position. This calls
    `rl_insert_text()` in the underlying library, but ignores
    the return value.

readline.redisplay()[¶](https://docs.python.org/3/library/readline.html#readline.redisplay "Link to this definition")
:   Change what’s displayed on the screen to reflect the current contents of the
    line buffer. This calls `rl_redisplay()` in the underlying library.