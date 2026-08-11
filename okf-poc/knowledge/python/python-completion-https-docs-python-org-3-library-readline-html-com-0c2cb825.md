---
id: python-completion-https-docs-python-org-3-library-readline-html-com-0c2cb825
type: concept
title: Completion[¶](https://docs.python.org/3/library/readline.html#completion "Link
  to this heading")
description: The following functions relate to implementing a custom word completion
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/readline.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Completion[¶](https://docs.python.org/3/library/readline.html#completion "Link to this heading")

The following functions relate to implementing a custom word completion
function. This is typically operated by the Tab key, and can suggest and
automatically complete a word being typed. By default, Readline is set up
to be used by [`rlcompleter`](https://docs.python.org/3/library/rlcompleter.html#module-rlcompleter "rlcompleter: Python identifier completion, suitable for the GNU readline library.") to complete Python identifiers for
the interactive interpreter. If the `readline` module is to be used
with a custom completer, a different set of word delimiters should be set.

readline.set\_completer([*function*])[¶](https://docs.python.org/3/library/readline.html#readline.set_completer "Link to this definition")
:   Set or remove the completer function. If *function* is specified, it will be
    used as the new completer function; if omitted or `None`, any completer
    function already installed is removed. The completer function is called as
    `function(text, state)`, for *state* in `0`, `1`, `2`, …, until it
    returns a non-string value. It should return the next possible completion
    starting with *text*.

    The installed completer function is invoked by the *entry\_func* callback
    passed to `rl_completion_matches()` in the underlying library.
    The *text* string comes from the first parameter to the
    `rl_attempted_completion_function` callback of the
    underlying library.

readline.get\_completer()[¶](https://docs.python.org/3/library/readline.html#readline.get_completer "Link to this definition")
:   Get the completer function, or `None` if no completer function has been set.

readline.get\_completion\_type()[¶](https://docs.python.org/3/library/readline.html#readline.get_completion_type "Link to this definition")
:   Get the type of completion being attempted. This returns the
    `rl_completion_type` variable in the underlying library as
    an integer.

readline.get\_begidx()[¶](https://docs.python.org/3/library/readline.html#readline.get_begidx "Link to this definition")

readline.get\_endidx()[¶](https://docs.python.org/3/library/readline.html#readline.get_endidx "Link to this definition")
:   Get the beginning or ending index of the completion scope.
    These indexes are the *start* and *end* arguments passed to the
    `rl_attempted_completion_function` callback of the
    underlying library. The values may be different in the same
    input editing scenario based on the underlying C readline implementation.
    Ex: libedit is known to behave differently than libreadline.

readline.set\_completer\_delims(*string*)[¶](https://docs.python.org/3/library/readline.html#readline.set_completer_delims "Link to this definition")

readline.get\_completer\_delims()[¶](https://docs.python.org/3/library/readline.html#readline.get_completer_delims "Link to this definition")
:   Set or get the word delimiters for completion. These determine the
    start of the word to be considered for completion (the completion scope).
    These functions access the `rl_completer_word_break_characters`
    variable in the underlying library.

readline.set\_completion\_display\_matches\_hook([*function*])[¶](https://docs.python.org/3/library/readline.html#readline.set_completion_display_matches_hook "Link to this definition")
:   Set or remove the completion display function. If *function* is
    specified, it will be used as the new completion display function;
    if omitted or `None`, any completion display function already
    installed is removed. This sets or clears the
    `rl_completion_display_matches_hook` callback in the
    underlying library. The completion display function is called as
    `function(substitution, [matches], longest_match_length)` once
    each time matches need to be displayed.