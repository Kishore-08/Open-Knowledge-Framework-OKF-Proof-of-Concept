---
id: apache-airflow-admin-views-a85da58d
type: concept
title: Admin Views
description: The **Admin** tab provides system-level tools for configuring and extending
  Airflow. These views are primarily intended for administrators and platform operators
  responsible for deployment, integratio
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/ui.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Admin Views

The **Admin** tab provides system-level tools for configuring and extending Airflow. These views are primarily intended for administrators and platform operators responsible for deployment, integration, and performance tuning.

Key pages include:

- **Variables** – Store key-value pairs accessible from Dags. Variables can be used to manage environment-specific parameters or secrets.
- **Connections** – Define connection URIs to external systems such as databases, cloud services, or APIs. These are consumed by Airflow operators and hooks.
- **Pools** – Control resource allocation by limiting the number of concurrently running tasks assigned to a named pool. Useful for managing contention or quota-constrained systems.
- **Providers** – View installed provider packages (e.g., `apache-airflow-providers-google`), including available hooks, sensors, and operators. This is helpful for verifying provider versions or troubleshooting import errors.
- **Plugins** – Inspect registered Airflow plugins that extend the platform via custom operators, macros, or UI elements.
- **Config** – View the full effective Airflow configuration as parsed from `airflow.cfg`, environment variables, or overridden defaults. This can help debug issues related to scheduler behavior, secrets backends, and more.

Note

The Admin tab is only visible to users with appropriate RBAC permissions.

---

![_images/variable_hidden.png](https://airflow.apache.org/docs/apache-airflow/stable/_images/variable_hidden.png)


---

![_images/admin_connections.png](https://airflow.apache.org/docs/apache-airflow/stable/_images/admin_connections.png)


---

![_images/admin_connections_add.png](https://airflow.apache.org/docs/apache-airflow/stable/_images/admin_connections_add.png)

Was this entry helpful?