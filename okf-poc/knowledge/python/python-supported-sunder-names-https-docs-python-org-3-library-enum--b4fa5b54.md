---
id: python-supported-sunder-names-https-docs-python-org-3-library-enum--b4fa5b54
type: concept
title: Supported `_sunder_` names[¶](https://docs.python.org/3/library/enum.html#supported-sunder-names
  "Link to this heading")
description: '- [`_name_`](https://docs.python.org/3/library/enum.html#enum.Enum._name_
  "enum.Enum._name_") – name of the member'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/enum.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

### Supported `_sunder_` names[¶](https://docs.python.org/3/library/enum.html#supported-sunder-names "Link to this heading")

- [`_name_`](https://docs.python.org/3/library/enum.html#enum.Enum._name_ "enum.Enum._name_") – name of the member
- [`_value_`](https://docs.python.org/3/library/enum.html#enum.Enum._value_ "enum.Enum._value_") – value of the member; can be set in `__new__`
- [`_missing_()`](https://docs.python.org/3/library/enum.html#enum.Enum._missing_ "enum.Enum._missing_") – a lookup function used when a value is not found;
  may be overridden
- [`_ignore_`](https://docs.python.org/3/library/enum.html#enum.Enum._ignore_ "enum.Enum._ignore_") – a list of names, either as a [`list`](https://docs.python.org/3/library/stdtypes.html#list "list") or a
  [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), that will not be transformed into members, and will be removed
  from the final class
- [`_order_`](https://docs.python.org/3/library/enum.html#enum.Enum._order_ "enum.Enum._order_") – no longer used, kept for backward
  compatibility (class attribute, removed during class creation)
- [`_generate_next_value_()`](https://docs.python.org/3/library/enum.html#enum.Enum._generate_next_value_ "enum.Enum._generate_next_value_") – used to get an appropriate value for
  an enum member; may be overridden
- [`_add_alias_()`](https://docs.python.org/3/library/enum.html#enum.Enum._add_alias_ "enum.Enum._add_alias_") – adds a new name as an alias to an existing
  member.
- [`_add_value_alias_()`](https://docs.python.org/3/library/enum.html#enum.Enum._add_value_alias_ "enum.Enum._add_value_alias_") – adds a new value as an alias to an
  existing member.
- While `_sunder_` names are generally reserved for the further development
  of the [`Enum`](https://docs.python.org/3/library/enum.html#enum.Enum "enum.Enum") class and can not be used, some are explicitly allowed:

  - `_repr_*` (e.g. `_repr_html_`), as used in [IPython’s rich display](https://ipython.readthedocs.io/en/stable/config/integrating.html#rich-display)

Added in version 3.6: `_missing_`, `_order_`, `_generate_next_value_`

Added in version 3.7: `_ignore_`

Added in version 3.13: `_add_alias_`, `_add_value_alias_`, `_repr_*`

---