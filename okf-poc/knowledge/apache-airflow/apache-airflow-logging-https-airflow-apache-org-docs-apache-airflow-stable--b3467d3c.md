---
id: apache-airflow-logging-https-airflow-apache-org-docs-apache-airflow-stable--b3467d3c
type: concept
title: '[[logging]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id23)'
description: '> Added in version 2.0.0.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[logging]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id23)

#### base\_log\_folder

> Added in version 2.0.0.

The folder where airflow should store its log files.
This path must be absolute.
There are a few existing configurations that assume this is set to the default.
If you choose to override this you may need to update the
`[logging] dag_processor_manager_log_location` and
`[logging] dag_processor_child_process_log_directory settings` as well.

Type:
:   string

Default:
:   `{AIRFLOW_HOME}/logs`

Environment Variable:
:   `AIRFLOW__LOGGING__BASE_LOG_FOLDER`

#### callsite\_parameters

> Added in version 3.1.0.

A comma separated list of information about the callsite (such as line number of filename etc) of
logger calls to include in each message.

See `structlog.processors.CallsiteParameter` for the possible values.The values should be the
constant names (`FUNC_NAME`) or the values (`func_name`)

Including these in a log message adds a lot to the usability to the logs, but collecting these has a
(tiny) cost – if you are super concerned with eking out every last ounce of performance you could
turn these off (by setting this value to an empty string)

Type:
:   string

Default:
:   `filename,lineno`

Environment Variable:
:   `AIRFLOW__LOGGING__CALLSITE_PARAMETERS`

#### celery\_logging\_level

> Added in version 2.3.0.

Logging level for celery. If not set, it uses the value of logging\_level

Supported values: `CRITICAL`, `ERROR`, `WARNING`, `INFO`, `DEBUG`.

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__LOGGING__CELERY_LOGGING_LEVEL`

#### celery\_stdout\_stderr\_separation

> Added in version 2.7.0.

By default Celery sends all logs into stderr.
If enabled any previous logging handlers will get *removed*.
With this option AirFlow will create new handlers
and send low level logs like INFO and WARNING to stdout,
while sending higher severity logs to stderr.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__LOGGING__CELERY_STDOUT_STDERR_SEPARATION`

#### color\_log\_error\_keywords

> Added in version 2.10.0.

A comma separated list of keywords related to errors whose presence should display the line in red
color in UI

Type:
:   string

Default:
:   `error,exception`

Environment Variable:
:   `AIRFLOW__LOGGING__COLOR_LOG_ERROR_KEYWORDS`

#### color\_log\_warning\_keywords

> Added in version 2.10.0.

A comma separated list of keywords related to warning whose presence should display the line in yellow
color in UI

Type:
:   string

Default:
:   `warn`

Environment Variable:
:   `AIRFLOW__LOGGING__COLOR_LOG_WARNING_KEYWORDS`

#### colored\_console\_log

> Added in version 2.0.0.

Flag to enable/disable Colored logs in Console
Colour the logs when the controlling terminal is a TTY.

Type:
:   string

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__LOGGING__COLORED_CONSOLE_LOG`

#### dag\_processor\_child\_process\_log\_directory

Determines the directory where logs for the child processes of the dag processor will be stored

Type:
:   string

Default:
:   `{AIRFLOW_HOME}/logs/dag_processor`

Environment Variable:
:   `AIRFLOW__LOGGING__DAG_PROCESSOR_CHILD_PROCESS_LOG_DIRECTORY`

#### dag\_processor\_log\_format

> Added in version 2.4.0.

Format of Dag Processor Log line

Type:
:   string

Default:
:   `[%%(asctime)s] [SOURCE:DAG_PROCESSOR] {%%(filename)s:%%(lineno)d} %%(levelname)s - %%(message)s`

Environment Variable:
:   `AIRFLOW__LOGGING__DAG_PROCESSOR_LOG_FORMAT`

#### dag\_processor\_log\_target

> Added in version 2.4.0.

Where to send dag parser logs. If “file”, logs are sent to log files defined by child\_process\_log\_directory.

Type:
:   string

Default:
:   `file`

Environment Variable:
:   `AIRFLOW__LOGGING__DAG_PROCESSOR_LOG_TARGET`

#### delete\_local\_logs

> Added in version 2.6.0.

Whether the local log files for GCS, S3, WASB, HDFS and OSS remote logging should be deleted after
they are uploaded t