---
id: apache-airflow-improvements-51425edb
type: concept
title: Improvements
description: '- Allow depth-first execution (#27827)'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Improvements

- Allow depth-first execution (#27827)
- UI: Update offset height if data changes (#27865)
- Improve TriggerRuleDep typing and readability (#27810)
- Make views requiring session, keyword only args (#27790)
- Optimize `TI.xcom_pull()` with explicit task\_ids and map\_indexes (#27699)
- Allow hyphens in pod id used by k8s executor (#27737)
- optimise task instances filtering (#27102)
- Use context managers to simplify log serve management (#27756)
- Fix formatting leftovers (#27750)
- Improve task deadlock messaging (#27734)
- Improve “sensor timeout” messaging (#27733)
- Replace urlparse with `urlsplit` (#27389)
- Align TaskGroup semantics to AbstractOperator (#27723)
- Add new files to parsing queue on every loop of dag processing (#27060)
- Make Kubernetes Executor & Scheduler resilient to error during PMH execution (#27611)
- Separate dataset deps into individual graphs (#27356)
- Use log.exception where more economical than log.error (#27517)
- Move validation `branch_task_ids` into `SkipMixin` (#27434)
- Coerce LazyXComAccess to list when pushed to XCom (#27251)
- Update cluster-policies.rst docs (#27362)
- Add warning if connection type already registered within the provider (#27520)
- Activate debug logging in commands with –verbose option (#27447)
- Add classic examples for Python Operators (#27403)
- change `.first()` to `.scalar()` (#27323)
- Improve reset\_dag\_run description (#26755)
- Add examples and `howtos` about sensors (#27333)
- Make grid view widths adjustable (#27273)
- Sorting plugins custom menu links by category before name (#27152)
- Simplify DagRun.verify\_integrity (#26894)
- Add mapped task group info to serialization (#27027)
- Correct the JSON style used for Run config in Grid View (#27119)
- No `extra__conn_type__` prefix required for UI behaviors (#26995)
- Improve dataset update blurb (#26878)
- Rename kubernetes config section to kubernetes\_executor (#26873)
- decode params for dataset searches (#26941)
- Get rid of the DAGRun details page & rely completely on Grid (#26837)
- Fix scheduler `crashloopbackoff` when using `hostname_callable` (#24999)
- Reduce log verbosity in KubernetesExecutor. (#26582)
- Don’t iterate tis list twice for no reason (#26740)
- Clearer code for PodGenerator.deserialize\_model\_file (#26641)
- Don’t import kubernetes unless you have a V1Pod (#26496)
- Add updated\_at column to DagRun and Ti tables (#26252)
- Move the deserialization of custom XCom Backend to 2.4.0 (#26392)
- Avoid calculating all elements when one item is needed (#26377)
- Add `__future__`.annotations automatically by isort (#26383)
- Handle list when serializing expand\_kwargs (#26369)
- Apply PEP-563 (Postponed Evaluation of Annotations) to core airflow (#26290)
- Add more weekday operator and sensor examples #26071 (#26098)
- Align TaskGroup semantics to AbstractOperator (#27723)