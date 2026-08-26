---
id: apache-airflow-email-https-airflow-apache-org-docs-apache-airflow-stable-co-b3467d3c
type: concept
title: '[[email]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id19)'
description: Configuration email backend and whether to
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[email]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id19)

Configuration email backend and whether to
send email alerts on retry or failure

#### default\_email\_on\_failure

> Added in version 2.0.0.

Whether email alerts should be sent when a task failed

Type:
:   boolean

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__EMAIL__DEFAULT_EMAIL_ON_FAILURE`

#### default\_email\_on\_retry

> Added in version 2.0.0.

Whether email alerts should be sent when a task is retried

Type:
:   boolean

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__EMAIL__DEFAULT_EMAIL_ON_RETRY`

#### email\_backend

Email backend to use

Type:
:   string

Default:
:   `airflow.utils.email.send_email_smtp`

Environment Variable:
:   `AIRFLOW__EMAIL__EMAIL_BACKEND`

#### email\_conn\_id

> Added in version 2.1.0.

Email connection to use

Type:
:   string

Default:
:   `smtp_default`

Environment Variable:
:   `AIRFLOW__EMAIL__EMAIL_CONN_ID`

#### from\_email

> Added in version 2.2.4.

Email address that will be used as sender address.
It can either be raw email or the complete address in a format `Sender Name <sender@email.com>`

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__EMAIL__FROM_EMAIL`

Example:
:   `Airflow <airflow@example.com>`

#### html\_content\_template

> Added in version 2.0.1.

File that will be used as the template for Email content (which will be rendered using Jinja2).
If not set, Airflow uses a base template.

See also

[Email Configuration](https://airflow.apache.org/docs/apache-airflow/stable/howto/email-config.html)

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__EMAIL__HTML_CONTENT_TEMPLATE`

Example:
:   `/path/to/my_html_content_template_file`

#### ssl\_context

> Added in version 2.7.0.

ssl context to use when using SMTP and IMAP SSL connections. By default, the context is “default”
which sets it to `ssl.create_default_context()` which provides the right balance between
compatibility and security, it however requires that certificates in your operating system are
updated and that SMTP/IMAP servers of yours have valid certificates that have corresponding public
keys installed on your machines. You can switch it to “none” if you want to disable checking
of the certificates, but it is not recommended as it allows MITM (man-in-the-middle) attacks
if your infrastructure is not sufficiently secured. It should only be set temporarily while you
are fixing your certificate configuration. This can be typically done by upgrading to newer
version of the operating system you run Airflow components on,by upgrading/refreshing proper
certificates in the OS or by updating certificates for your mail servers.

Type:
:   string

Default:
:   `default`

Environment Variable:
:   `AIRFLOW__EMAIL__SSL_CONTEXT`

Example:
:   `default`

#### subject\_template

> Added in version 2.0.1.

File that will be used as the template for Email subject (which will be rendered using Jinja2).
If not set, Airflow uses a base template.

See also

[Email Configuration](https://airflow.apache.org/docs/apache-airflow/stable/howto/email-config.html)

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__EMAIL__SUBJECT_TEMPLATE`

Example:
:   `/path/to/my_subject_template_file`