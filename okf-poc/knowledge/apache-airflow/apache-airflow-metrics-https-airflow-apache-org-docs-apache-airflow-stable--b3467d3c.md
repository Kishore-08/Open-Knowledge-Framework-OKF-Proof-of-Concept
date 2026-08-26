---
id: apache-airflow-metrics-https-airflow-apache-org-docs-apache-airflow-stable--b3467d3c
type: concept
title: '[[metrics]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id24)'
description: '[StatsD](https://github.com/statsd/statsd) integration settings.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[metrics]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id24)

[StatsD](https://github.com/statsd/statsd) integration settings.

#### legacy\_names\_on

> Added in version 3.2.0.

If true, it exports both new and legacy metric names.
Legacy names contain variables such as dag\_id and task\_id,
while the new names set these variables inside tags.

Type:
:   string

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__METRICS__LEGACY_NAMES_ON`

#### metrics\_allow\_list

> Added in version 2.6.0.

Configure an allow list (comma separated regex patterns to match) to send only certain metrics.

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__METRICS__METRICS_ALLOW_LIST`

Example:
:   `"scheduler,executor,dagrun,pool,triggerer,celery" or "^scheduler,^executor,heartbeat|timeout"`

#### metrics\_block\_list

> Added in version 2.6.0.

Configure a block list (comma separated regex patterns to match) to block certain metrics
from being emitted.
If `[metrics] metrics_allow_list` and `[metrics] metrics_block_list` are both configured,
`[metrics] metrics_block_list` is ignored.

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__METRICS__METRICS_BLOCK_LIST`

Example:
:   `"scheduler,executor,dagrun,pool,triggerer,celery" or "^scheduler,^executor,heartbeat|timeout"`

#### otel\_debugging\_on

> Added in version 2.7.0.

If `True`, all metrics are also emitted to the console. Defaults to `False`.

Deprecated since version 3.2.0: According to the OpenTelemetry specification, configuration is expected to happen through
the standard OpenTelemetry environment variables rather than project-specific settings.

> This option has been deprecated to ensure consistent behavior across different environments
> and deployments that use OpenTelemetry.
>
> OpenTelemetry should be configured exclusively using the standard OpenTelemetry environment variables
> such as ‘OTEL\_EXPORTER\_OTLP\_ENDPOINT’, ‘OTEL\_EXPORTER\_OTLP\_PROTOCOL’, ‘OTEL\_SERVICE\_NAME’, etc.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__METRICS__OTEL_DEBUGGING_ON`

#### otel\_host

> Added in version 2.6.0.

Specifies the hostname or IP address of the OpenTelemetry Collector to which Airflow sends
metrics and traces.

Deprecated since version 3.2.0: According to the OpenTelemetry specification, configuration is expected to happen through
the standard OpenTelemetry environment variables rather than project-specific settings.

> This option has been deprecated to ensure consistent behavior across different environments
> and deployments that use OpenTelemetry.
>
> OpenTelemetry should be configured exclusively using the standard OpenTelemetry environment variables
> such as ‘OTEL\_EXPORTER\_OTLP\_ENDPOINT’, ‘OTEL\_EXPORTER\_OTLP\_PROTOCOL’, ‘OTEL\_SERVICE\_NAME’, etc.

Type:
:   string

Default:
:   `localhost`

Environment Variable:
:   `AIRFLOW__METRICS__OTEL_HOST`

#### otel\_interval\_milliseconds

> Added in version 2.6.0.

Defines the interval, in milliseconds, at which Airflow sends batches of metrics and traces
to the configured OpenTelemetry Collector.

Deprecated since version 3.2.0: According to the OpenTelemetry specification, configuration is expected to happen through
the standard OpenTelemetry environment variables rather than project-specific settings.

> This option has been deprecated to ensure consistent behavior across different environments
> and deployments that use OpenTelemetry.
>
> OpenTelemetry should be configured exclusively using the standard OpenTelemetry environment variables
> such as ‘OTEL\_EXPORTER\_OTLP\_ENDPOINT’, ‘OTEL\_EXPORTER\_OTLP\_PROTOCOL’, ‘OTEL\_SERVICE\_NAME’, etc.

Type:
:   integer

Default:
:   `60000`

Environment Variable:
:   `AIRFLOW__METRICS__OTEL_INTERVAL_MILLISECONDS`

#### otel\_on

> Added in version 2.6.0.

Enables sending metrics to OpenTelemetry.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
: