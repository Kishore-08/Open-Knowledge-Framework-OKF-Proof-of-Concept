---
id: apache-airflow-filters-7aae3951
type: concept
title: Filters
description: Airflow defines some Jinja filters that can be used to format values.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Filters

Airflow defines some Jinja filters that can be used to format values.

For example, using `{{ logical_date | ds }}` will output the logical\_date in the `YYYY-MM-DD` format.

| Filter | Operates on | Description |
| --- | --- | --- |
| `ds` | datetime | Format the datetime as `YYYY-MM-DD` |
| `ds_nodash` | datetime | Format the datetime as `YYYYMMDD` |
| `ts` | datetime | Same as `.isoformat()`, Example: `2018-01-01T00:00:00+00:00` |
| `ts_nodash` | datetime | Same as `ts` filter without `-`, `:` or TimeZone info. Example: `20180101T000000` |
| `ts_nodash_with_tz` | datetime | As `ts` filter without `-` or `:`. Example `20180101T000000+0000` |