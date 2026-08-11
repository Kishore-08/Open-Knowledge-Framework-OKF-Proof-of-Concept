---
id: python-types-https-docs-python-org-3-library-string-templatelib-htm-465b2467
type: concept
title: Types[¶](https://docs.python.org/3/library/string.templatelib.html#types "Link
  to this heading")
description: '*class* string.templatelib.Template[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template
  "Link to this definition")'
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/string.templatelib.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## Types[¶](https://docs.python.org/3/library/string.templatelib.html#types "Link to this heading")

*class* string.templatelib.Template[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "Link to this definition")
:   The `Template` class describes the contents of a template string.
    It is immutable, meaning that attributes of a template cannot be reassigned.

    The most common way to create a `Template` instance is to use the
    [template string literal syntax](https://docs.python.org/3/reference/lexical_analysis.html#t-strings).
    This syntax is identical to that of [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings),
    except that it uses a `t` prefix in place of an `f`:

    ```
    >>> cheese = 'Red Leicester'
    >>> template = t"We're fresh out of {cheese}, sir."
    >>> type(template)
    <class 'string.templatelib.Template'>
    ```

    Templates are stored as sequences of literal [`strings`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.strings "string.templatelib.Template.strings")
    and dynamic [`interpolations`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.interpolations "string.templatelib.Template.interpolations").
    A [`values`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.values "string.templatelib.Template.values") attribute holds the values of the interpolations:

    ```
    >>> cheese = 'Camembert'
    >>> template = t'Ah! We do have {cheese}.'
    >>> template.strings
    ('Ah! We do have ', '.')
    >>> template.interpolations
    (Interpolation('Camembert', ...),)
    >>> template.values
    ('Camembert',)
    ```

    The `strings` tuple has one more element than `interpolations`
    and `values`; the interpolations “belong” between the strings.
    This may be easier to understand when tuples are aligned

    ```
    template.strings:  ('Ah! We do have ',              '.')
    template.values:   (                   'Camembert',    )
    ```

    Attributes

    strings*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "tuple")[[str](https://docs.python.org/3/library/stdtypes.html#str "str"), ...]*[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.strings "Link to this definition")
    :   A [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") of the static strings in the template.

        ```
        >>> cheese = 'Camembert'
        >>> template = t'Ah! We do have {cheese}.'
        >>> template.strings
        ('Ah! We do have ', '.')
        ```

        Empty strings *are* included in the tuple:

        ```
        >>> response = 'We do have '
        >>> cheese = 'Camembert'
        >>> template = t'Ah! {response}{cheese}.'
        >>> template.strings
        ('Ah! ', '', '.')
        ```

        The `strings` tuple is never empty, and always contains one more
        string than the `interpolations` and `values` tuples:

        ```
        >>> t''.strings
        ('',)
        >>> t''.values
        ()
        >>> t'{'cheese'}'.strings
        ('', '')
        >>> t'{'cheese'}'.values
        ('cheese',)
        ```

    interpolations*: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "tuple")[[Interpolation](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation"), ...]*[¶](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template.interpolations "Link to this definition")
    :   A [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") of the interpolations in the template.

        ```
        >>> cheese = 'Camembert'
        >>> template = t'Ah! We do have {cheese}.'
        >>> template.interpolations
        (Interpolation('Camembert', 'cheese', None, ''),)
        ```

        The `int