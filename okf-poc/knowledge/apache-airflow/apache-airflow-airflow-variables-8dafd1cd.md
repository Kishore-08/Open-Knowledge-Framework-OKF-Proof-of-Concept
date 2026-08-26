---
id: apache-airflow-airflow-variables-8dafd1cd
type: concept
title: Airflow Variables
description: Using Airflow Variables yields network calls and database access, so
  their usage in top-level Python code for Dags
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Airflow Variables

Using Airflow Variables yields network calls and database access, so their usage in top-level Python code for Dags
should be avoided as much as possible, as mentioned in the previous chapter, [Top level Python Code](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html#best-practices-top-level-code).
If Airflow Variables must be used in top-level Dag code, then their impact on Dag parsing can be mitigated by
[enabling the experimental cache](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-secrets-use-cache), configured with a sensible [ttl](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-secrets-cache-ttl-seconds).

You can use the Airflow Variables freely inside the `execute()` methods of the operators, but you can also pass the
Airflow Variables to the existing operators via Jinja template, which will delay reading the value until the task execution.

The template syntax to do this is:

```
{{ var.value.<variable_name> }}
```

or if you need to deserialize a json object from the variable :

```
{{ var.json.<variable_name> }}
```

In top-level code, variables using jinja templates do not produce a request until a task is running, whereas,
`Variable.get()` produces a request every time the Dag file is parsed by the scheduler if caching is not enabled.
Using `Variable.get()` without [enabling caching](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-secrets-use-cache) will lead to suboptimal
performance in the Dag file processing.
In some cases this can cause the Dag file to timeout before it is fully parsed.

Bad example:

```
from airflow.sdk import Variable

foo_var = Variable.get("foo")  # AVOID THAT
bash_use_variable_bad_1 = BashOperator(
    task_id="bash_use_variable_bad_1", bash_command="echo variable foo=${foo_env}", env={"foo_env": foo_var}
)

bash_use_variable_bad_2 = BashOperator(
    task_id="bash_use_variable_bad_2",
    bash_command=f"echo variable foo=${Variable.get('foo')}",  # AVOID THAT
)

bash_use_variable_bad_3 = BashOperator(
    task_id="bash_use_variable_bad_3",
    bash_command="echo variable foo=${foo_env}",
    env={"foo_env": Variable.get("foo")},  # AVOID THAT
)
```

Good example:

```
bash_use_variable_good = BashOperator(
    task_id="bash_use_variable_good",
    bash_command="echo variable foo=${foo_env}",
    env={"foo_env": "{{ var.value.get('foo') }}"},
)
```

```
@task
def my_task():
    var = Variable.get("foo")  # This is ok since my_task is called only during task run, not during Dag scan.
    print(var)
```

For security purpose, you’re recommended to use the [Secrets Backend](https://airflow.apache.org/docs/apache-airflow/stable/security/secrets/secrets-backend/index.html#secrets-backend-configuration)
for any variable that contains sensitive data.