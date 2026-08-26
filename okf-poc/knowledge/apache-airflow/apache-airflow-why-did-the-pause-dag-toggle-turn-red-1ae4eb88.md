---
id: apache-airflow-why-did-the-pause-dag-toggle-turn-red-1ae4eb88
type: concept
title: Why did the pause Dag toggle turn red?
description: If pausing or unpausing a Dag fails for any reason, the Dag toggle will
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/faq.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Why did the pause Dag toggle turn red?

If pausing or unpausing a Dag fails for any reason, the Dag toggle will
revert to its previous state and turn red. If you observe this behavior,
try pausing the Dag again, or check the console or server logs if the
issue recurs.

## API Server