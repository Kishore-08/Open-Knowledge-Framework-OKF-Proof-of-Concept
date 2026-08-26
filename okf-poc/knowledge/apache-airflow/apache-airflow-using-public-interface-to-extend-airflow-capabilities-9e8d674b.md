---
id: apache-airflow-using-public-interface-to-extend-airflow-capabilities-9e8d674b
type: concept
title: Using Public Interface to extend Airflow capabilities
description: Airflow uses Plugin mechanism to extend Airflow platform capabilities.
  They allow to extend
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Using Public Interface to extend Airflow capabilities

Airflow uses Plugin mechanism to extend Airflow platform capabilities. They allow to extend
Airflow UI but also they are the way to expose the below customizations (Triggers, Timetables, Listeners, etc.).
Providers can also implement plugin endpoints and customize Airflow UI and the customizations.

You can read more about plugins in [Plugins](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/plugins.html). You can read how to extend
Airflow UI in [Customize view of Apache from Airflow web UI](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-view-plugin.html). Note that there are some simple customizations of the UI
that do not require plugins - you can read more about them in [Customizing the UI](https://airflow.apache.org/docs/apache-airflow/stable/howto/customize-ui.html).

Here are the ways how Plugins can be used to extend Airflow: