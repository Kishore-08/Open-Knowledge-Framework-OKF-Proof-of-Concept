---
id: python-match-objects-https-docs-python-org-3-library-re-html-match--02d619bb
type: concept
title: Match Objects[¶](https://docs.python.org/3/library/re.html#match-objects "Link
  to this heading")
description: Match objects always have a boolean value of `True`.
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/re.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Match Objects[¶](https://docs.python.org/3/library/re.html#match-objects "Link to this heading")

Match objects always have a boolean value of `True`.
Since [`match()`](https://docs.python.org/3/library/re.html#re.Pattern.match "re.Pattern.match") and [`search()`](https://docs.python.org/3/library/re.html#re.Pattern.search "re.Pattern.search") return `None`
when there is no match, you can test whether there was a match with a simple
`if` statement:

```
match = re.search(pattern, string)
if match:
    process(match)
```

*class* re.Match[¶](https://docs.python.org/3/library/re.html#re.Match "Link to this definition")
:   Match object returned by successful `match`es and `search`es.

    Matches are [generic](https://docs.python.org/3/library/typing.html#generics) over the type of string which was
    matched ([`str`](https://docs.python.org/3/library/stdtypes.html#str "str") or [`bytes`](https://docs.python.org/3/library/stdtypes.html#bytes "bytes")).

    Changed in version 3.9: `re.Match` supports `[]` to indicate a Unicode (str) or bytes match.
    See [Generic Alias Type](https://docs.python.org/3/library/stdtypes.html#types-genericalias).

Match.expand(*template*)[¶](https://docs.python.org/3/library/re.html#re.Match.expand "Link to this definition")
:   Return the string obtained by doing backslash substitution on the template
    string *template*, as done by the [`sub()`](https://docs.python.org/3/library/re.html#re.Pattern.sub "re.Pattern.sub") method.
    Escapes such as `\n` are converted to the appropriate characters,
    and numeric backreferences (`\1`, `\2`) and named backreferences
    (`\g<1>`, `\g<name>`) are replaced by the contents of the
    corresponding group. The backreference `\g<0>` will be
    replaced by the entire match.

    Changed in version 3.5: Unmatched groups are replaced with an empty string.

Match.group([*group1*, *...*])[¶](https://docs.python.org/3/library/re.html#re.Match.group "Link to this definition")
:   Returns one or more subgroups of the match. If there is a single argument, the
    result is a single string; if there are multiple arguments, the result is a
    tuple with one item per argument. Without arguments, *group1* defaults to zero
    (the whole match is returned). If a *groupN* argument is zero, the corresponding
    return value is the entire matching string; if it is a positive integer, it is
    the string matching the corresponding parenthesized group. If a group number is
    negative or larger than the number of groups defined in the pattern, an
    [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError") exception is raised. If a group is contained in a
    part of the pattern that did not match, the corresponding result is `None`.
    If a group is contained in a part of the pattern that matched multiple times,
    the last match is returned.

    ```
    >>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
    >>> m.group(0)       # The entire match
    'Isaac Newton'
    >>> m.group(1)       # The first parenthesized subgroup.
    'Isaac'
    >>> m.group(2)       # The second parenthesized subgroup.
    'Newton'
    >>> m.group(1, 2)    # Multiple arguments give us a tuple.
    ('Isaac', 'Newton')
    ```

    If the regular expression uses the `(?P<name>...)` syntax, the *groupN*
    arguments may also be strings identifying groups by their group name. If a
    string argument is not used as a group name in the pattern, an [`IndexError`](https://docs.python.org/3/library/exceptions.html#IndexError "IndexError")
    exception is raised.

    A moderately complicated example:

    ```
    >>> m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
    >>> m.group('first_name')
    'Malcolm'
    >>> m.group('last_name')
    'Reynolds'
    ```

    Named groups can also be referred to by their index:

    ```
    >>> m.group(1)
    'Malcolm'
    >>> m.group(2)
    'Reynolds'
    ```

    If a group ma