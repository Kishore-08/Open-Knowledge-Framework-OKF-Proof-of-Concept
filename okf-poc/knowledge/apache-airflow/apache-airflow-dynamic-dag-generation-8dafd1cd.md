---
id: apache-airflow-dynamic-dag-generation-8dafd1cd
type: concept
title: Dynamic Dag Generation
description: Sometimes writing Dags manually isn’t practical.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Dynamic Dag Generation

Sometimes writing Dags manually isn’t practical.
Maybe you have a lot of Dags that do similar things with just a parameter changing between them.
Or maybe you need a set of Dags to load tables, but don’t want to manually update Dags every time those tables change.
In these and other cases, it can be more useful to dynamically generate Dags.

Avoiding excessive processing at the top level code described in the previous chapter is especially important
in case of dynamic Dag configuration, which can be configured essentially in one of those ways:

- via [environment variables](https://wiki.archlinux.org/title/environment_variables) (not to be mistaken
  with the [Airflow Variables](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/variables.html))
- via externally provided, generated Python code, containing meta-data in the Dag folder
- via externally provided, generated configuration meta-data file in the Dag folder

Some cases of dynamic Dag generation are described in the [Dynamic Dag Generation](https://airflow.apache.org/docs/apache-airflow/stable/howto/dynamic-dag-generation.html) section.