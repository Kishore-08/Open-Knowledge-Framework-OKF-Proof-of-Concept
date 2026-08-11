---
id: python-regular-expression-syntax-https-docs-python-org-3-library-re-02d619bb
type: concept
title: Regular Expression Syntax[¶](https://docs.python.org/3/library/re.html#regular-expression-syntax
  "Link to this heading")
description: A regular expression (or RE) specifies a set of strings that matches
  it; the
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Regular Expression Syntax[¶](https://docs.python.org/3/library/re.html#regular-expression-syntax "Link to this heading")

A regular expression (or RE) specifies a set of strings that matches it; the
functions in this module let you check if a particular string matches a given
regular expression (or if a given regular expression matches a particular
string, which comes down to the same thing).

Regular expressions can be concatenated to form new regular expressions; if *A*
and *B* are both regular expressions, then *AB* is also a regular expression.
In general, if a string *p* matches *A* and another string *q* matches *B*, the
string *pq* will match AB. This holds unless *A* or *B* contain low precedence
operations; boundary conditions between *A* and *B*; or have numbered group
references. Thus, complex expressions can easily be constructed from simpler
primitive expressions like the ones described here. For details of the theory
and implementation of regular expressions, consult the Friedl book [[Frie09]](https://docs.python.org/3/library/re.html#frie09),
or almost any textbook about compiler construction.

A brief explanation of the format of regular expressions follows. For further
information and a gentler presentation, consult the [Regular expression HOWTO](https://docs.python.org/3/howto/regex.html#regex-howto).

Regular expressions can contain both special and ordinary characters. Most
ordinary characters, like `'A'`, `'a'`, or `'0'`, are the simplest regular
expressions; they simply match themselves. You can concatenate ordinary
characters, so `last` matches the string `'last'`. (In the rest of this
section, we’ll write RE’s in `this special style`, usually without quotes, and
strings to be matched `'in single quotes'`.)

Some characters, like `'|'` or `'('`, are special. Special
characters either stand for classes of ordinary characters, or affect
how the regular expressions around them are interpreted.

Repetition operators or quantifiers (`*`, `+`, `?`, `{m,n}`, etc) cannot be
directly nested. This avoids ambiguity with the non-greedy modifier suffix
`?`, and with other modifiers in other implementations. To apply a second
repetition to an inner repetition, parentheses may be used. For example,
the expression `(?:a{6})*` matches any multiple of six `'a'` characters.

The special characters are:

`.`
:   (Dot.) In the default mode, this matches any character except a newline. If
    the [`DOTALL`](https://docs.python.org/3/library/re.html#re.DOTALL "re.DOTALL") flag has been specified, this matches any character
    including a newline. `(?s:.)` matches any character regardless of flags.

`^`
:   (Caret.) Matches the start of the string, and in [`MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE "re.MULTILINE") mode also
    matches immediately after each newline.

`$`
:   Matches the end of the string or just before the newline at the end of the
    string, and in [`MULTILINE`](https://docs.python.org/3/library/re.html#re.MULTILINE "re.MULTILINE") mode also matches before a newline. `foo`
    matches both ‘foo’ and ‘foobar’, while the regular expression `foo$` matches
    only ‘foo’. More interestingly, searching for `foo.$` in `'foo1\nfoo2\n'`
    matches ‘foo2’ normally, but ‘foo1’ in `MULTILINE` mode; searching for
    a single `$` in `'foo\n'` will find two (empty) matches: one just before
    the newline, and one at the end of the string.

`*`
:   Causes the resulting RE to match 0 or more repetitions of the preceding RE, as
    many repetitions as are possible. `ab*` will match ‘a’, ‘ab’, or ‘a’ followed
    by any number of ‘b’s.

`+`
:   Causes the resulting RE to match 1 or more repetitions of the preceding RE.
    `ab+` will match ‘a’ followed by any non-zero number of ‘b’s; it will not
    match just ‘a’.

`?`
:   Causes the resulting RE to match 0 or 1 repetitions of the preceding RE.
    `ab?` will match either ‘a’ or ‘ab’.

`*?`, `+?`, `??`
:   The `'*'`, `'+'`, and `'?'` quantifie