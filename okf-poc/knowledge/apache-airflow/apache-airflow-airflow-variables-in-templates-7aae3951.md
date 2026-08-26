---
id: apache-airflow-airflow-variables-in-templates-7aae3951
type: concept
title: Airflow Variables in Templates
description: The `var` template variable allows you to access Airflow Variables.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Airflow Variables in Templates

The `var` template variable allows you to access Airflow Variables.
You can access them as either plain-text or JSON. If you use JSON, you are
also able to walk nested structures, such as dictionaries like:
`{{ var.json.my_dict_var.key1 }}`.

It is also possible to fetch a variable by string if needed (for example your variable key contains dots) with
`{{ var.value.get('my.var', 'fallback') }}` or
`{{ var.json.get('my.dict.var', {'key1': 'val1'}) }}`. Defaults can be
supplied in case the variable does not exist.