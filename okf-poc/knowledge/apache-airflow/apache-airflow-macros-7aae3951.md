---
id: apache-airflow-macros-7aae3951
type: concept
title: Macros
description: Macros are a way to expose objects to your templates and live under the
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Macros

Macros are a way to expose objects to your templates and live under the
`macros` namespace in your templates.

A few commonly used libraries and methods are made available.

| Variable | Description |
| --- | --- |
| `macros.datetime` | The standard lib’s [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.14)"). Note: `utcnow()` is deprecated in Python 3.12+; use `now(macros.dateutil.tz.UTC)` instead. |
| `macros.timedelta` | The standard lib’s [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.14)") |
| `macros.dateutil` | A reference to the `dateutil` package |
| `macros.time` | The standard lib’s [`time`](https://docs.python.org/3/library/time.html#module-time "(in Python v3.14)") |
| `macros.uuid` | The standard lib’s [`uuid`](https://docs.python.org/3/library/uuid.html#module-uuid "(in Python v3.14)") |
| `macros.random` | The standard lib’s `random.random` |

Some Airflow specific macros are also defined:

airflow.sdk.execution\_time.macros.datetime\_diff\_for\_humans(*dt*, *since=None*)[[source]](https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/sdk/execution_time/macros.html#datetime_diff_for_humans)
:   Return a human-readable/approximate difference between datetimes.

    When only one datetime is provided, the comparison will be based on now.

    Parameters:
    :   - **dt** (*Any*) – The datetime to display the diff for
        - **since** (*DateTime* *|* *None*) – When to display the date from. If `None` then the diff is
          between `dt` and now.

airflow.sdk.execution\_time.macros.ds\_add(*ds*, *days*)[[source]](https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/sdk/execution_time/macros.html#ds_add)
:   Add or subtract days from a YYYY-MM-DD.

    Parameters:
    :   - **ds** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – anchor date in `YYYY-MM-DD` format to add to
        - **days** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – number of days to add to the ds, you can use negative values

    ```
    >>> ds_add("2015-01-01", 5)
    '2015-01-06'
    >>> ds_add("2015-01-06", -5)
    '2015-01-01'
    ```

airflow.sdk.execution\_time.macros.ds\_format(*ds*, *input\_format*, *output\_format*)[[source]](https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/sdk/execution_time/macros.html#ds_format)
:   Output datetime string in a given format.

    Parameters:
    :   - **ds** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Input string which contains a date.
        - **input\_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Input string format (e.g., ‘%Y-%m-%d’).
        - **output\_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Output string format (e.g., ‘%Y-%m-%d’).

    ```
    >>> ds_format("2015-01-01", "%Y-%m-%d", "%m-%d-%y")
    '01-01-15'
    >>> ds_format("1/5/2015", "%m/%d/%Y", "%Y-%m-%d")
    '2015-01-05'
    >>> ds_format("12/07/2024", "%d/%m/%Y", "%A %d %B %Y", "en_US")
    'Friday 12 July 2024'
    ```

airflow.sdk.execution\_time.macros.ds\_format\_locale(*ds*, *input\_format*, *output\_format*, *locale=None*)[[source]](https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/sdk/execution_time/macros.html#ds_format_locale)
:   Output localized datetime string in a given Babel format.

    Parameters:
    :   - **ds** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Input string which contains a date.
        - **input\_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Input string format (e.g., ‘%Y-%m-%d’).
        - **output\_format** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Outpu