---
id: apache-airflow-lineage-https-airflow-apache-org-docs-apache-airflow-stable--b3467d3c
type: concept
title: '[[lineage]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id22)'
description: '> Added in version 3.2.0.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[lineage]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id22)

#### max\_assets\_per\_collector

> Added in version 3.2.0.

Maximum number of asset inputs or outputs that can be collected by a single hook lineage collector
instance. Input assets and output assets are counted separately. Once the maximum is reached, any
additional assets will be dropped.

Type:
:   integer

Default:
:   `100`

Environment Variable:
:   `AIRFLOW__LINEAGE__MAX_ASSETS_PER_COLLECTOR`

#### max\_extras\_per\_collector

> Added in version 3.2.0.

Maximum number of extra metadata entries that can be collected by a single hook lineage collector
instance. Once the maximum is reached, any additional extra metadata will be dropped.

Type:
:   integer

Default:
:   `200`

Environment Variable:
:   `AIRFLOW__LINEAGE__MAX_EXTRAS_PER_COLLECTOR`