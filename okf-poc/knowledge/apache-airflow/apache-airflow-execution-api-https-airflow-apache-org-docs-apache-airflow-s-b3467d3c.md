---
id: apache-airflow-execution-api-https-airflow-apache-org-docs-apache-airflow-s-b3467d3c
type: concept
title: '[[execution\_api]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id20)'
description: Settings related to the Execution API server.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[execution\_api]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id20)

Settings related to the Execution API server.

The ExecutionAPI also uses a lot of settings from the [[api\_auth]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-api-auth) section.

#### jwt\_audience

> Added in version 3.0.0.

The audience claim to use when generating and validating JWTs for the Execution API.

This variable can be a single value, or a comma-separated string, in which case the first value is the
one that will be used when generating, and the others are accepted at validation time.

Not required, but strongly encouraged

See also [jwt\_audience](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-api-auth-jwt-audience)

Type:
:   string

Default:
:   `urn:airflow.apache.org:task`

Environment Variable:
:   `AIRFLOW__EXECUTION_API__JWT_AUDIENCE`

#### jwt\_expiration\_time

> Added in version 3.0.0.

Number in seconds until the JWT used for authentication expires. When the token expires,
all API calls using this token will fail on authentication.

Make sure that time on ALL the machines that you run airflow components on is synchronized
(for example using ntpd) otherwise you might get “forbidden” errors.

Type:
:   integer

Default:
:   `600`

Environment Variable:
:   `AIRFLOW__EXECUTION_API__JWT_EXPIRATION_TIME`

#### otel\_trace\_propagation

> Added in version 3.3.0.

Controls when W3C trace context (`traceparent`/`tracestate`) is extracted from
incoming Execution API requests and attached to the OpenTelemetry context.

`only-authenticated` (default): trace context is extracted as a FastAPI dependency
on authenticated routes, after JWT verification succeeds. Unauthenticated requests
(including probes and attack traffic) cannot inject trace context.

`unsafe-always`: trace context is extracted on all routes (including unauthenticated ones
such as health checks), before JWT verification. Use this when you want trace context
propagated even on auth failures. If untrusted traffic can reach your API server this can
result in data pollution or load/cost in your OTel trace store.

`never`: trace context is never extracted. Use this to disable the feature entirely.

Type:
:   string

Default:
:   `only-authenticated`

Environment Variable:
:   `AIRFLOW__EXECUTION_API__OTEL_TRACE_PROPAGATION`