---
id: apache-airflow-kerberos-https-airflow-apache-org-docs-apache-airflow-stable-b3467d3c
type: concept
title: '[[kerberos]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id21)'
description: Location of your ccache file once kinit has been performed.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[kerberos]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id21)

#### ccache

Location of your ccache file once kinit has been performed.

Type:
:   string

Default:
:   `/tmp/airflow_krb5_ccache`

Environment Variable:
:   `AIRFLOW__KERBEROS__CCACHE`

#### forwardable

> Added in version 2.2.0.

Allow to disable ticket forwardability.

Type:
:   boolean

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__KERBEROS__FORWARDABLE`

#### include\_ip

> Added in version 2.2.0.

Allow to remove source IP from token, useful when using token behind NATted Docker host.

Type:
:   boolean

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__KERBEROS__INCLUDE_IP`

#### keytab

Designates the path to the Kerberos keytab file for the Airflow user

Type:
:   string

Default:
:   `airflow.keytab`

Environment Variable:
:   `AIRFLOW__KERBEROS__KEYTAB`

#### kinit\_path

Path to the kinit executable

Type:
:   string

Default:
:   `kinit`

Environment Variable:
:   `AIRFLOW__KERBEROS__KINIT_PATH`

#### principal

gets augmented with fqdn

Type:
:   string

Default:
:   `airflow`

Environment Variable:
:   `AIRFLOW__KERBEROS__PRINCIPAL`

#### reinit\_frequency

Determines the frequency at which initialization or re-initialization processes occur.

Type:
:   string

Default:
:   `3600`

Environment Variable:
:   `AIRFLOW__KERBEROS__REINIT_FREQUENCY`