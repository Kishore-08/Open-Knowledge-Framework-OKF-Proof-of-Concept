---
id: apache-airflow-airflow-connections-in-templates-7aae3951
type: concept
title: Airflow Connections in Templates
description: Similarly, Airflow Connections data can be accessed via the `conn` template
  variable. For example, you could use expressions in your templates like `{{ conn.my_conn_id.login
  }}`,
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Airflow Connections in Templates

Similarly, Airflow Connections data can be accessed via the `conn` template variable. For example, you could use expressions in your templates like `{{ conn.my_conn_id.login }}`,
`{{ conn.my_conn_id.password }}`, etc.

Just like with `var` it’s possible to fetch a connection by string (e.g. `{{ conn.get('my_conn_id_'+index).host }}`
) or provide defaults (e.g `{{ conn.get('my_conn_id', {"host": "host1", "login": "user1"}).host }}`).

Additionally, the `extras` field of a connection can be fetched as a Python Dictionary with the `extra_dejson` field, e.g.
`conn.my_aws_conn_id.extra_dejson.region_name` would fetch `region_name` out of `extras`.
This way, defaults in `extras` can be provided as well (e.g. `{{ conn.my_aws_conn_id.extra_dejson.get('region_name', 'Europe (Frankfurt)') }}`).