---
id: apache-airflow-sub-commands-https-airflow-apache-org-docs-apache-airflow-st-5b0ecd17
type: concept
title: '[Sub-commands](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#id2)'
description: Start an Airflow API server instance
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [Sub-commands](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#id2)

#### [api-server](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#id3)

Start an Airflow API server instance

```
airflow api-server [-h] [--apps APPS] [-D] [-d] [-H HOST] [--log-config LOG_CONFIG] [-l LOG_FILE] [--pid [PID]] [-p PORT] [--proxy-headers] [--ssl-ca-file SSL_CA_FILE] [--ssl-cert SSL_CERT]
                   [--ssl-cert-reqs {none,optional,required}] [--ssl-key SSL_KEY] [--stderr STDERR] [--stdout STDOUT] [-t WORKER_TIMEOUT] [-w WORKERS]
```

##### Named Arguments

`--apps`
:   Applications to run (comma-separated). Default is all. Options: core, execution, all

    Default: `'all'`

`-D, --daemon`
:   Daemonize instead of running in the foreground

    Default: `False`

`-d, --dev`
:   Start in development mode with hot-reload enabled

    Default: `False`

`-H, --host`
:   Set the host on which to run the API server

    Default: `'0.0.0.0'`

`--log-config`
:   (Optional) Path to the logging configuration file for the uvicorn server. If not set, the default uvicorn logging configuration will be used.

`-l, --log-file`
:   Location of the log file

`--pid`
:   PID file location

`-p, --port`
:   The port on which to run the API server

    Default: `8080`

`--proxy-headers`
:   Enable X-Forwarded-Proto, X-Forwarded-For, X-Forwarded-Port to populate remote address info.

    Default: `False`

`--ssl-ca-file`
:   (Optional) Path to the SSL CA file

`--ssl-cert`
:   Path to the SSL certificate for the webserver

    Default: `''`

`--ssl-cert-reqs`
:   Possible choices: none, optional, required

    (Optional) Set certificate verification options.

    Default: `'none'`

`--ssl-key`
:   Path to the key to use with the SSL certificate

    Default: `''`

`--stderr`
:   Redirect stderr to this file

`--stdout`
:   Redirect stdout to this file

`-t, --worker-timeout`
:   The timeout for waiting on API server workers

    Default: `120`

`-w, --workers`
:   Number of workers to run on the API server

    Default: `1`

#### [assets](https://airflow.apache.org/docs/apache-airflow/stable/cli-and-env-variables-ref.html#id4)

Manage assets

```
airflow assets [-h] COMMAND ...
```

##### Positional Arguments

`COMMAND`
:   Possible choices: details, list, materialize

##### Sub-commands

###### details

Show asset details

```
airflow assets details [-h] [--alias] [--name NAME] [-o (table, json, yaml, plain)] [--uri URI] [-v]
```

###### Named Arguments

`--alias`
:   Show asset alias

    Default: `False`

`--name`
:   Asset name

    Default: `''`

`-o, --output`
:   Possible choices: table, json, yaml, plain

    Output format. Allowed values: json, yaml, plain, table (default: table)

    Default: `'table'`

`--uri`
:   Asset URI

    Default: `''`

`-v, --verbose`
:   Make logging output more verbose

    Default: `False`

###### list

List assets

```
airflow assets list [-h] [--alias] [--columns COLUMNS] [-o (table, json, yaml, plain)] [-v]
```

###### Named Arguments

`--alias`
:   Show asset alias

    Default: `False`

`--columns`
:   List of columns to render. (default: [‘name’, ‘uri’, ‘group’, ‘extra’])

    Default: `('name', 'uri', 'group', 'extra')`

`-o, --output`
:   Possible choices: table, json, yaml, plain

    Output format. Allowed values: json, yaml, plain, table (default: table)

    Default: `'table'`

`-v, --verbose`
:   Make logging output more verbose

    Default: `False`

###### materialize

Materialize an asset

```
airflow assets materialize [-h] [--name NAME] [-o (table, json, yaml, plain)] [--uri URI] [-v]
```

###### Named Arguments

`--name`
:   Asset name

    Default: `''`

`-o, --output`
:   Possible choices: table, json, yaml, plain

    Output format. Allowed values: json, yaml, plain, table (default: table)

    Default: `'table'`

`--uri`
:   Asset URI

    Default: `''`

`-v, --verbose`
:   Make logging output more verbose

    Default: `