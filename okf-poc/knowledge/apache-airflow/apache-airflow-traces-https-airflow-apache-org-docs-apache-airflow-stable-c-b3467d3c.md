---
id: apache-airflow-traces-https-airflow-apache-org-docs-apache-airflow-stable-c-b3467d3c
type: concept
title: '[[traces]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id34)'
description: Distributed traces integration settings.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[traces]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id34)

Distributed traces integration settings.

#### otel\_debug\_traces\_on

> Added in version 3.1.0.

If True, then traces from Airflow internal methods are exported. Defaults to False.

Deprecated since version 3.2.0: This parameter is no longer used.

Type:
:   string

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__TRACES__OTEL_DEBUG_TRACES_ON`

#### otel\_debugging\_on

> Added in version 2.10.0.

If True, all traces are also emitted to the console. Defaults to False.

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
:   `AIRFLOW__TRACES__OTEL_DEBUGGING_ON`

#### otel\_host

> Added in version 2.10.0.

Specifies the hostname or IP address of the OpenTelemetry Collector to which Airflow sends
traces.

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
:   `AIRFLOW__TRACES__OTEL_HOST`

#### otel\_on

> Added in version 2.10.0.

Enables sending traces to OpenTelemetry.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__TRACES__OTEL_ON`

#### otel\_port

> Added in version 2.10.0.

Specifies the port of the OpenTelemetry Collector that is listening to.

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
:   `8889`

Environment Variable:
:   `AIRFLOW__TRACES__OTEL_PORT`

#### otel\_service

> Added in version 2.10.0.

The default service name of traces.

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
:   `Airflow`

Environment Variable:
:   `AIRFLOW__TRACES__OTEL_SERVICE`

#### otel\_ssl\_active

> Added in version 2.10.0.

If True, SSL will be enabled. Defaults to False.
To establish an HTTPS connection to the OpenTelemetry collector,
you need to configure the SSL certificate and key within the OpenTelemetry coll