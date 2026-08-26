---
id: apache-airflow-auth-managers-9e8d674b
type: concept
title: Auth managers
description: Auth managers are responsible of user authentication and user authorization
  in Airflow. All auth managers are
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Auth managers

Auth managers are responsible of user authentication and user authorization in Airflow. All auth managers are
derived from `BaseAuthManager`.

The auth manager interface itself (the `BaseAuthManager` class) is
public, but the different implementations of auth managers are not (i.e. FabAuthManager).

You can read more about auth managers and how to write your own in [Auth manager](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/auth-manager/index.html).