---
id: apache-airflow-installing-and-using-ruff-8dafd1cd
type: concept
title: Installing and Using ruff
description: '1. **Installation**: Install `ruff` using pip:'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Installing and Using ruff

1. **Installation**: Install `ruff` using pip:

   ```
   pip install "ruff>=0.15.17"
   ```
2. **Running ruff**: Execute `ruff` to check your Dags for potential issues:

   ```
   ruff check dags/ --select AIR3
   ```

   This command will analyze your Dags located in the `dags/` directory and report any issues related to the specified rules.