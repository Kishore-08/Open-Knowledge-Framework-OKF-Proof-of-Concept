---
id: apache-airflow-miscellaneous-51425edb
type: concept
title: Miscellaneous
description: '- Move secrets masker to shared distribution for better modularity (#54449)'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release_notes.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### Miscellaneous

- Move secrets masker to shared distribution for better modularity (#54449)
- Move email notifications from scheduler to DAG processor for better architecture (#55238)
- Add graph UI load optimization with latest run info endpoint (#53429)
- Optimize UI bundle size by moving translations to dynamic loading (#51735)
- Relocate Task SDK components for improved separation (#55174, #54795)
- Refactor trigger rule utilities and weight rule consolidation (#54797, #53393)
- Remove deprecated Airflow 2.x modules and legacy imports (#50482)
- Clean up unused code and improve module organization (#52176, #52173, #53031)
- Add SQLAlchemy 2.0 CI support for future compatibility (#52233)
- Improve test fixtures and SDK communication testing (#54795, #50603)
- Add translation completeness linting and validation tools (#51166)
- Upgrade to latest versions of important dependencies (#55350)
- Move webserver configuration options to API section (#50693, #50656)
- Improve DAG bundle handling and versioning support (#47592)
- Add database management CLI tools for external database operations (#50657)
- Add comprehensive HITL operator documentation and examples (#54618)
- Add guards for registering middlewares from plugins (#55399)
- Optimize Gantt group expansion with de-bouncing and deferred rendering (#55334)
- Differentiate between triggers and watchers currently running for better visibility (#55376)
- Removed unused config: `dag_stale_not_seen_duration` (#55601, #55684)
- Update UI’s query client strategy for improved performance (#55528)
- Unify datetime format across the UI for consistency (#55572)
- Mark React Apps as Experimental for Airflow 3.1 release (#55478)
- Improve OOM error messaging for clearer task failure diagnosis (#55602)
- Display responder username for better audit trail in HITL workflows (#55509)
- The constraint file do not contain developer dependencies anymore (#53631)
- Add hyperlinks to `dag_id` column in DAG Runs and Task Instances pages for better navigation (#55648)
- Add responsive web design (RWD) support to Grid view (#55745)