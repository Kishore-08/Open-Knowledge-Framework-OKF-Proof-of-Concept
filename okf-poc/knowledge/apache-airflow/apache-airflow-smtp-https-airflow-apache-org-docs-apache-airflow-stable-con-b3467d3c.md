---
id: apache-airflow-smtp-https-airflow-apache-org-docs-apache-airflow-stable-con-b3467d3c
type: concept
title: '[[smtp]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id32)'
description: If you want airflow to send emails on retries, failure, and you want
  to use
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[smtp]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id32)

If you want airflow to send emails on retries, failure, and you want to use
the airflow.utils.email.send\_email\_smtp function, you have to configure an
smtp server here

#### smtp\_host

Specifies the host server address used by Airflow when sending out email notifications via SMTP.

Type:
:   string

Default:
:   `localhost`

Environment Variable:
:   `AIRFLOW__SMTP__SMTP_HOST`

#### smtp\_mail\_from

Specifies the default **from** email address used when Airflow sends email notifications.

Type:
:   string

Default:
:   `airflow@example.com`

Environment Variable:
:   `AIRFLOW__SMTP__SMTP_MAIL_FROM`

#### smtp\_port

Defines the port number on which Airflow connects to the SMTP server to send email notifications.

Type:
:   integer

Default:
:   `25`

Environment Variable:
:   `AIRFLOW__SMTP__SMTP_PORT`

#### smtp\_retry\_limit

> Added in version 2.0.0.

Defines the number of times Airflow will attempt to connect to the SMTP server after the first
attempt.

Type:
:   integer

Default:
:   `5`

Environment Variable:
:   `AIRFLOW__SMTP__SMTP_RETRY_LIMIT`

#### smtp\_ssl

Determines whether to use an SSL connection when talking to the SMTP server.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__SMTP__SMTP_SSL`

#### smtp\_starttls

Determines whether to use the STARTTLS command when connecting to the SMTP server.

Type:
:   boolean

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__SMTP__SMTP_STARTTLS`

#### smtp\_timeout

> Added in version 2.0.0.

Determines the maximum time (in seconds) the Apache Airflow system will wait for a
connection to the SMTP server to be established.

Type:
:   integer

Default:
:   `30`

Environment Variable:
:   `AIRFLOW__SMTP__SMTP_TIMEOUT`