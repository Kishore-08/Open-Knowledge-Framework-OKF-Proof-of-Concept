---
id: python-adding-new-actions-https-docs-python-org-3-library-optparse--f59a6996
type: concept
title: Adding new actions[¶](https://docs.python.org/3/library/optparse.html#adding-new-actions
  "Link to this heading")
description: Adding new actions is a bit trickier, because you have to understand
  that
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/optparse.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Adding new actions[¶](https://docs.python.org/3/library/optparse.html#adding-new-actions "Link to this heading")

Adding new actions is a bit trickier, because you have to understand that
`optparse` has a couple of classifications for actions:

“store” actions
:   actions that result in `optparse` storing a value to an attribute of the
    current OptionValues instance; these options require a [`dest`](https://docs.python.org/3/library/optparse.html#optparse.Option.dest "optparse.Option.dest")
    attribute to be supplied to the Option constructor.

“typed” actions
:   actions that take a value from the command line and expect it to be of a
    certain type; or rather, a string that can be converted to a certain type.
    These options require a [`type`](https://docs.python.org/3/library/optparse.html#optparse.Option.type "optparse.Option.type") attribute to the Option
    constructor.

These are overlapping sets: some default “store” actions are `"store"`,
`"store_const"`, `"append"`, and `"count"`, while the default “typed”
actions are `"store"`, `"append"`, and `"callback"`.

When you add an action, you need to categorize it by listing it in at least one
of the following class attributes of Option (all are lists of strings):

Option.ACTIONS[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.ACTIONS "Link to this definition")
:   All actions must be listed in ACTIONS.

Option.STORE\_ACTIONS[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.STORE_ACTIONS "Link to this definition")
:   “store” actions are additionally listed here.

Option.TYPED\_ACTIONS[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPED_ACTIONS "Link to this definition")
:   “typed” actions are additionally listed here.

Option.ALWAYS\_TYPED\_ACTIONS[¶](https://docs.python.org/3/library/optparse.html#optparse.Option.ALWAYS_TYPED_ACTIONS "Link to this definition")
:   Actions that always take a type (i.e. whose options always take a value) are
    additionally listed here. The only effect of this is that `optparse`
    assigns the default type, `"string"`, to options with no explicit type
    whose action is listed in [`ALWAYS_TYPED_ACTIONS`](https://docs.python.org/3/library/optparse.html#optparse.Option.ALWAYS_TYPED_ACTIONS "optparse.Option.ALWAYS_TYPED_ACTIONS").

In order to actually implement your new action, you must override Option’s
`take_action()` method and add a case that recognizes your action.

For example, let’s add an `"extend"` action. This is similar to the standard
`"append"` action, but instead of taking a single value from the command-line
and appending it to an existing list, `"extend"` will take multiple values in
a single comma-delimited string, and extend an existing list with them. That
is, if `--names` is an `"extend"` option of type `"string"`, the command
line

```
--names=foo,bar --names blah --names ding,dong
```

would result in a list

```
["foo", "bar", "blah", "ding", "dong"]
```

Again we define a subclass of Option:

```
class MyOption(Option):

    ACTIONS = Option.ACTIONS + ("extend",)
    STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
    TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)
    ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

    def take_action(self, action, dest, opt, value, values, parser):
        if action == "extend":
            lvalue = value.split(",")
            values.ensure_value(dest, []).extend(lvalue)
        else:
            Option.take_action(
                self, action, dest, opt, value, values, parser)
```

Features of note:

- `"extend"` both expects a value on the command-line and stores that value
  somewhere, so it goes in both [`STORE_ACTIONS`](https://docs.python.org/3/library/optparse.html#optparse.Option.STORE_ACTIONS "optparse.Option.STORE_ACTIONS") and
  [`TYPED_ACTIONS`](https://docs.python.org/3/library/optparse.html#optparse.Option.TYPED_ACTIONS "optparse.Option.TYPED_ACTIONS").
- to ensure tha