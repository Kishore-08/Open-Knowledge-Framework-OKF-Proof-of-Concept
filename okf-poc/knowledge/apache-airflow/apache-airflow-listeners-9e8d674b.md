---
id: apache-airflow-listeners-9e8d674b
type: concept
title: Listeners
description: Listeners enable you to respond to Dag/Task lifecycle events.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Listeners

Listeners enable you to respond to Dag/Task lifecycle events.

This is implemented via `ListenerManager` class that provides hooks that
can be implemented to respond to Dag/Task lifecycle events.

Added in version 2.5: Listener public interface has been added in version 2.5.

You can read more about Listeners in [Listeners](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/listeners.html).