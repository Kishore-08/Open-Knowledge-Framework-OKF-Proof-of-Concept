---
id: apache-airflow-profiling-https-airflow-apache-org-docs-apache-airflow-stabl-b3467d3c
type: concept
title: '[[profiling]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id26)'
description: Configuration for memory profiling in Airflow component.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[profiling]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id26)

Configuration for memory profiling in Airflow component.
Currently, we provide profiling using Memray and additional tools may be added in the future
Also, see the guide in Link (TBD)

#### memray\_detailed\_tracing

> Added in version 3.3.0.

Whether to enable memray’s `native_traces` and `trace_python_allocators` options
when `memray_trace_components` is set. Captures C/C++ stack frames for compiled
extensions (numpy, pandas, etc.) and small `pymalloc` allocations that would
otherwise be invisible.

This adds significant runtime overhead and produces much larger profile files, so
leave it disabled unless the default trace lacks the detail you need. Native symbol
resolution is most accurate on Linux and less precise on macOS. See
<https://bloomberg.github.io/memray/api.html> for the underlying `Tracker` options.

Type:
:   boolean

Default:
:   `False`

Environment Variable:
:   `AIRFLOW__PROFILING__MEMRAY_DETAILED_TRACING`

#### memray\_trace\_components

> Added in version 3.2.0.

Comma-separated list of Airflow components to profile with memray.
Valid components are: scheduler, api, dag\_processor, triggerer

This option only takes effect when it is not set to blank (default option).
start tracing memory allocation and store the metrics in “$AIRFLOW\_HOME/<component>\_memory.bin”
To generate analyzed view, run this command in base directory where the bin file is generated
`` `
# see also https://bloomberg.github.io/memray/run.html#aggregated-capture-files
memray flamegraph $AIRFLOW_HOME/<component>_memory.bin
` ``
This is an expensive operation and generally should not be used except for debugging purposes.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__PROFILING__MEMRAY_TRACE_COMPONENTS`

Example:
:   `scheduler,api,dag_processor`