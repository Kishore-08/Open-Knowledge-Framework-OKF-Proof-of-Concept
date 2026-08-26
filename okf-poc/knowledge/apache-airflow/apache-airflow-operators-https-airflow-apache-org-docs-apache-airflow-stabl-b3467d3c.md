---
id: apache-airflow-operators-https-airflow-apache-org-docs-apache-airflow-stabl-b3467d3c
type: concept
title: '[[operators]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id25)'
description: Indicates the default number of CPU units allocated to each operator
  when no specific CPU request
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[operators]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id25)

#### default\_cpus

Indicates the default number of CPU units allocated to each operator when no specific CPU request
is specified in the operator’s configuration

Type:
:   string

Default:
:   `1`

Environment Variable:
:   `AIRFLOW__OPERATORS__DEFAULT_CPUS`

#### default\_deferrable

> Added in version 2.7.0.

The default value of attribute “deferrable” in operators and sensors.

Type:
:   boolean

Default:
:   `false`

Environment Variable:
:   `AIRFLOW__OPERATORS__DEFAULT_DEFERRABLE`

#### default\_disk

Indicates the default number of disk storage allocated to each operator when no specific disk request
is specified in the operator’s configuration

Type:
:   string

Default:
:   `512`

Environment Variable:
:   `AIRFLOW__OPERATORS__DEFAULT_DISK`

#### default\_gpus

Indicates the default number of GPUs allocated to each operator when no specific GPUs request
is specified in the operator’s configuration

Type:
:   string

Default:
:   `0`

Environment Variable:
:   `AIRFLOW__OPERATORS__DEFAULT_GPUS`

#### default\_owner

The default owner assigned to each new operator, unless
provided explicitly or passed via `default_args`

Type:
:   string

Default:
:   `airflow`

Environment Variable:
:   `AIRFLOW__OPERATORS__DEFAULT_OWNER`

#### default\_queue

> Added in version 2.1.0.

Default queue that tasks get assigned to and that worker listen on.

Type:
:   string

Default:
:   `default`

Environment Variable:
:   `AIRFLOW__OPERATORS__DEFAULT_QUEUE`

#### default\_ram

Indicates the default number of RAM allocated to each operator when no specific RAM request
is specified in the operator’s configuration

Type:
:   string

Default:
:   `512`

Environment Variable:
:   `AIRFLOW__OPERATORS__DEFAULT_RAM`