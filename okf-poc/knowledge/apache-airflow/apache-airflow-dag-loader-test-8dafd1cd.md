---
id: apache-airflow-dag-loader-test-8dafd1cd
type: concept
title: Dag Loader Test
description: This test should ensure that your Dag does not contain a piece of code
  that raises error while loading.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Dag Loader Test

This test should ensure that your Dag does not contain a piece of code that raises error while loading.
No additional code needs to be written by the user to run this test.

```
python your-dag-file.py
```

Running the above command without any error ensures your Dag does not contain any uninstalled dependency,
syntax errors, etc. Make sure that you load your Dag in an environment that corresponds to your
scheduler environment - with the same dependencies, environment variables, common code referred from the
Dag.

This is also a great way to check if your Dag loads faster after an optimization, if you want to attempt
to optimize Dag loading time. Simply run the Dag and measure the time it takes, but again you have to
make sure your Dag runs with the same dependencies, environment variables, common code.

There are many ways to measure the time of processing, one of them in Linux environment is to
use built-in `time` command. Make sure to run it several times in succession to account for
caching effects. Compare the results before and after the optimization (in the same conditions - using
the same machine, environment etc.) in order to assess the impact of the optimization.

```
time python airflow/example_dags/example_python_operator.py
```

Result:

```
real    0m0.699s
user    0m0.590s
sys     0m0.108s
```

The important metrics is the “real time” - which tells you how long time it took
to process the Dag. Note that when loading the file this way, you are starting a new interpreter so there is
an initial loading time that is not present when Airflow parses the Dag. You can assess the
time of initialization by running:

```
time python -c ''
```

Result:

```
real    0m0.073s
user    0m0.037s
sys     0m0.039s
```

In this case the initial interpreter startup time is ~ 0.07s which is about 10% of time needed to parse
the example\_python\_operator.py above so the actual parsing time is about ~ 0.62 s for the example Dag.

You can look into [Testing a Dag](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html#testing) for details on how to test individual operators.