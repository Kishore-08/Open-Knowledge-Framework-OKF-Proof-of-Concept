---
id: apache-airflow-api-https-airflow-apache-org-docs-apache-airflow-stable-conf-b3467d3c
type: concept
title: '[[api]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id12)'
description: '> Added in version 2.1.0.'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[api]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id12)

#### access\_control\_allow\_headers

> Added in version 2.1.0.

Used in response to a preflight request to indicate which HTTP
headers can be used when making the actual request. This header is
the server side response to the browser’s
Access-Control-Request-Headers header.

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__API__ACCESS_CONTROL_ALLOW_HEADERS`

#### access\_control\_allow\_methods

> Added in version 2.1.0.

Specifies the method or methods allowed when accessing the resource.

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__API__ACCESS_CONTROL_ALLOW_METHODS`

#### access\_control\_allow\_origins

> Added in version 2.2.0.

Indicates whether the response can be shared with requesting code from the given origins.
Separate URLs with space. Wildcard (`*`) is not allowed: Airflow’s API requires
credentialed CORS, which is incompatible with a wildcard origin per the CORS spec, and
browsers reject any response that combines the two. List exact origins instead
(for example `https://airflow.mycompany.com`).

Type:
:   string

Default:
:   `''`

Environment Variable:
:   `AIRFLOW__API__ACCESS_CONTROL_ALLOW_ORIGINS`

#### auto\_refresh\_interval

> Added in version 2.2.0.

How frequently, in seconds, the DAG data will auto-refresh in graph or grid view
when auto-refresh is turned on

Type:
:   integer

Default:
:   `3`

Environment Variable:
:   `AIRFLOW__API__AUTO_REFRESH_INTERVAL`

#### base\_url

The base url of the API server. Airflow cannot guess what domain or CNAME you are using.
If the Airflow console (the front-end) and the API server are on a different domain, this config
should contain the API server endpoint.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__API__BASE_URL`

Example:
:   `https://my-airflow.company.com`

#### client\_ssl\_cert

Path to a PEM-encoded client SSL certificate to use
when the Task SDK connects to the Airflow Execution API.
Must be set together with `client_ssl_key`.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__API__CLIENT_SSL_CERT`

Example:
:   `/etc/airflow/certs/client.crt`

#### client\_ssl\_key

Path to the PEM-encoded private key corresponding to `client_ssl_cert`.
Must be set together with `client_ssl_cert`.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__API__CLIENT_SSL_KEY`

Example:
:   `/etc/airflow/certs/client.key`

#### client\_use\_public\_certs

Enable loading of public CA certificates from certifi into the client SSL context.

Type:
:   boolean

Default:
:   `True`

Environment Variable:
:   `AIRFLOW__API__CLIENT_USE_PUBLIC_CERTS`

#### dag\_cache\_size

> Added in version 3.3.0.

Size of the LRU cache for SerializedDAG objects in the API server.
Set to 0 to use an unbounded dict (no eviction, matching pre-3.2 behavior).
The cache is keyed by Dag version ID, so lookups by Dag ID
(e.g., viewing a Dag’s details) always query the database for the latest
version, but the deserialized result is cached for subsequent
version-specific lookups.

Type:
:   integer

Default:
:   `64`

Environment Variable:
:   `AIRFLOW__API__DAG_CACHE_SIZE`

#### dag\_cache\_ttl

> Added in version 3.3.0.

Time-to-live (seconds) for cached SerializedDAG objects in the API server.
After this time, cached DAGs will be re-fetched from the database on next access.
Set to 0 to disable TTL (cache entries will only be evicted by LRU policy).

Note: After a DAG is updated, the API server may serve the previous version
until the cached entry expires. Lower values reduce staleness but increase
database load.

Type:
:   integer

Default:
:   `3600`

Environment Variable:
:   `AIRFLOW__API__DAG_CACHE_TTL`

#### default\_wrap

> Added in version 1.10.4.

Default setting for wrap toggle on DAG code and TI log views.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
: