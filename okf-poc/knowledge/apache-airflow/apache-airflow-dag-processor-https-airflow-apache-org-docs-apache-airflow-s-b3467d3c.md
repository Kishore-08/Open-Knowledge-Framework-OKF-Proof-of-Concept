---
id: apache-airflow-dag-processor-https-airflow-apache-org-docs-apache-airflow-s-b3467d3c
type: concept
title: '[[dag\_processor]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id17)'
description: 'Configuration for the Airflow DAG processor. This includes, for example:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[dag\_processor]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id17)

Configuration for the Airflow DAG processor. This includes, for example:
:   - DAG bundles, which allows Airflow to load DAGs from different sources
    - Parsing configuration, like:
      :   - how often to refresh DAGs from those sources
          - how many files to parse concurrently

#### bundle\_refresh\_check\_interval

How often the DAG processor should check if any DAG bundles are ready for a refresh, either by hitting
the bundles refresh\_interval or because another DAG processor has seen a newer version of the bundle.
A low value means we check more frequently, and have a smaller window of time where DAG processors are
out of sync with each other, parsing different versions of the same bundle.

Type:
:   integer

Default:
:   `5`

Environment Variable:
:   `AIRFLOW__DAG_PROCESSOR__BUNDLE_REFRESH_CHECK_INTERVAL`

#### dag\_bundle\_config\_list

> Added in version 3.0.0.

List of backend configs. Must supply name, classpath, and kwargs for each backend.

By default, `refresh_interval` is set to `[dag_processor] refresh_interval`, but that can
also be overridden in kwargs if desired.

The default is the dags folder dag bundle.

Note: As shown below, you can split your json config over multiple lines by indenting.
See configparser documentation for an example:
<https://docs.python.org/3/library/configparser.html#supported-ini-file-structure>.

Type:
:   string

Default:
:   ```
    [
      {
        "name": "dags-folder",
        "classpath": "airflow.dag_processing.bundles.local.LocalDagBundle",
        "kwargs": {}
      }
    ]
    ```

Environment Variable:
:   `AIRFLOW__DAG_PROCESSOR__DAG_BUNDLE_CONFIG_LIST`

Example:
:   ```
    [
              {
                "name": "my-git-repo",
                "classpath": "airflow.providers.git.bundles.git.GitDagBundle",
                "kwargs": {
                  "subdir": "dags",
                  "tracking_ref": "main",
                  "refresh_interval": 0
                }
              }
            ]
    ```

#### dag\_bundle\_storage\_path

> Added in version 3.0.0.

String path to folder where Airflow bundles can store files locally. Not templated.
If no path is provided, Airflow will use `Path(tempfile.gettempdir()) / "airflow"`.
This path must be absolute.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__DAG_PROCESSOR__DAG_BUNDLE_STORAGE_PATH`

Example:
:   `/tmp/some-place`

#### dag\_file\_processor\_timeout

How long before timing out a DagFileProcessor, which processes a dag file

Type:
:   integer

Default:
:   `50`

Environment Variable:
:   `AIRFLOW__DAG_PROCESSOR__DAG_FILE_PROCESSOR_TIMEOUT`

#### dag\_version\_inflation\_check\_level

> Added in version 3.2.0.

Controls the behavior of Dag stability checker performed before Dag parsing in the Dag processor.
The check detects detect potential issues such as runtime-varying values in Dag/Task constructors
that could cause Dag version inflation.

- `off`: Disables Dag stability checks entirely. No errors or warnings are generated.
- `warning`: Dags load normally but warnings are displayed in the UI when issues are detected.
- `error`: Treats Dag stability failures as Dag import errors, preventing the Dag from loading.

Default is “warning” to alert users of potential issues without blocking Dag execution.

Type:
:   string

Default:
:   `warning`

Environment Variable:
:   `AIRFLOW__DAG_PROCESSOR__DAG_VERSION_INFLATION_CHECK_LEVEL`

#### disable\_bundle\_versioning

Always run tasks with the latest code. If set to True, the bundle version will not
be stored on the dag run and therefore, the latest code will always be used.

Note

This setting only applies to bundles that support versioning and does not affect
DAG versions displayed in the UI.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__DAG_PROCESSOR__DISABLE_BUNDLE_VERSIONING`

#### fi