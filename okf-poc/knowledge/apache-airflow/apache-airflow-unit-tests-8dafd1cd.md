---
id: apache-airflow-unit-tests-8dafd1cd
type: concept
title: Unit tests
description: Unit tests ensure that there is no incorrect code in your Dag. You can
  write unit tests for both your tasks and your Dag.
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Unit tests

Unit tests ensure that there is no incorrect code in your Dag. You can write unit tests for both your tasks and your Dag.

**Unit test for loading a Dag:**

```
import pytest

from airflow.dag_processing.dagbag import DagBag


@pytest.fixture()
def dagbag():
    return DagBag()


def test_dag_loaded(dagbag):
    dag = dagbag.get_dag(dag_id="hello_world")
    assert dagbag.import_errors == {}
    assert dag is not None
    assert len(dag.tasks) == 1
```

**Unit test a Dag structure:**
This is an example test want to verify the structure of a code-generated Dag against a dict object

```
def assert_dag_dict_equal(source, dag):
    assert dag.task_dict.keys() == source.keys()
    for task_id, downstream_list in source.items():
        assert dag.has_task(task_id)
        task = dag.get_task(task_id)
        assert task.downstream_task_ids == set(downstream_list)


def test_dag():
    assert_dag_dict_equal(
        {
            "DummyInstruction_0": ["DummyInstruction_1"],
            "DummyInstruction_1": ["DummyInstruction_2"],
            "DummyInstruction_2": ["DummyInstruction_3"],
            "DummyInstruction_3": [],
        },
        dag,
    )
```

**Unit test for custom operator:**

```
import pendulum

from airflow.sdk import DAG, TaskInstanceState


def test_my_custom_operator_execute_no_trigger(dag):
    TEST_TASK_ID = "my_custom_operator_task"
    with DAG(
        dag_id="my_custom_operator_dag",
        schedule="@daily",
        start_date=pendulum.datetime(2021, 9, 13, tz="UTC"),
    ) as dag:
        MyCustomOperator(
            task_id=TEST_TASK_ID,
            prefix="s3://bucket/some/prefix",
        )

    dagrun = dag.test()
    ti = dagrun.get_task_instance(task_id=TEST_TASK_ID)
    assert ti.state == TaskInstanceState.SUCCESS
    # Assert something related to tasks results: ti.xcom_pull()
```