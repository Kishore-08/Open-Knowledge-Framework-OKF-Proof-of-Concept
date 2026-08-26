---
id: apache-airflow-sdk-https-airflow-apache-org-docs-apache-airflow-stable-conf-b3467d3c
type: concept
title: '[[sdk]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id28)'
description: Settings for non-Python SDK runtime coordination
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[sdk]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id28)

Settings for non-Python SDK runtime coordination

#### coordinators

> Added in version 3.3.0.

JSON object mapping of coordinator keys to coordinator definitions.

Each value is an object with `classpath` and optional `kwargs`.
`classpath` is resolved via `import_string` and constructed with
`kwargs` on first use. Entries are
independent instances, so the same `classpath` can be configured
multiple times under different names with different `kwargs` (for
example, two `JavaCoordinator` instances pinned to different JDK
versions).

An entry may also carry an optional `extra` object for additional
information associated with the coordinator that the coordinator itself
does not receive; other components read it as needed. For example,
KubernetesExecutor reads `extra.pod_template_file` to launch a queue’s
worker pod from a specific pod template, and
`extra.worker_container_repository` + `extra.worker_container_tag` to
override the worker base image for that queue (both are required).

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__SDK__COORDINATORS`

Example:
:   ```
    {
          "jdk-17": {
            "classpath": "airflow.sdk.coordinators.java.JavaCoordinator",
            "kwargs": {
              "jars_root": ["/opt/airflow/java-bundles"],
              "java_executable": "/usr/lib/jvm/java-17-openjdk/bin/java",
              "jvm_args": ["-Xmx1024m"]
            },
            "extra": {
              "pod_template_file": "/opt/airflow/pod_templates/java.yaml",
              "worker_container_repository": "apache/airflow",
              "worker_container_tag": "3.3.0"
            }
          },
          "go-sdk": {
            "classpath": "airflow.sdk.coordinators.executable.ExecutableCoordinator",
            "kwargs": {
              "executables_root": ["/opt/airflow/executable-bundles"]
            }
          }
        }
    ```

#### queue\_to\_coordinator

> Added in version 3.3.0.

JSON mapping of queue names to a coordinator key from
`[sdk] coordinators`.

This mapping is checked to route a task to a configured coordinator
instance based on its queue. An entry in this mapping is needed if
tasks of a queue should be handled by a custom coordinator instead of
the default Python task-running mechanism.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__SDK__QUEUE_TO_COORDINATOR`

Example:
:   `{"legacy-java": "jdk-11", "modern-java": "jdk-17"}`