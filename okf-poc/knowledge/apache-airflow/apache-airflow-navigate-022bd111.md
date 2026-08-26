---
id: apache-airflow-navigate-022bd111
type: concept
title: '`↑↓` Navigate'
description: '`↑↓` Navigate'
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/release-process.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

`↑↓` Navigate
`⏎` Select
`Esc` Close



# Airflow’s release process and version policy

Since Airflow 2.0.0 and providers 1.0.0 we aim to follow SemVer, meaning the release numbering works as follows:

- Versions are numbered in the form X.Y.Z.
- X is the major version number.
- Y is the minor version number, also called the *feature release* version number.
- Z is the patch number, which is incremented for bugfix and security releases.
  Before every new release, we’ll make a release candidate available, and often alpha or beta release too.
  These are of the form X.Y.Z alpha/beta/rc N, which means the Nth alpha/beta/release candidate of version X.Y.Z

In git, each minor version will have its own branch, called `vX-Y-stable` where bugfix/security releases will be issued from.
Commits and PRs should not normally go direct to these branches, but instead should target the main branch and then be cherry-picked by the release managers to these release branches.
As a general rule of thumb, changes that will be included in a bugfix/security release will be associated with the corresponding github milestone in the PR but this is currently a manual process and deviations may occur.
In all cases, the release managers reserve the right to postpone a PR to a later release if they deem it prudent.
Additionally, no new features will be added to a patch release and minor releases are currently targeted at a roughly 2-3 month cadence.

Each Airflow release will also have a tag in git indicating its version number, signed with the release manager’s key.
Tags for the main Airflow release have the form `X.Y.Z` (no leading `v`) and providers are tagged with the form `providers-<name>/X.Y.Z`.

Although Airflow follows SemVer this is not a promise of 100% compatibility between minor or patch releases, simply because this is not possible: what is a bug to one person might be a feature another person is depending on.

> Knowing the *intentions* of a maintainer can be valuable – especially *when* things break. Because that’s all SemVer is: **a TL;DR of the changelog**.
>
> —Hynek Schlawack <https://hynek.me/articles/semver-will-not-save-you/>

That is all SemVer is – it’s a statement of our intent as package authors, and a clear statement of our goals.

Major release
:   Major releases (X.0.0, X+1.0.0 etc.) indicate a backwards-incompatible change.

    These releases do not happen with any regular interval or on any predictable schedule.

    Each time a new major version is released previously deprecated features will be removed.

Feature releases
:   Feature releases (X.Y.0, X.Y+1.0, etc.) will happen roughly every two or three months – see release process for details.
    These releases will contain new features, improvements to existing features, and such.

Patch releases
:   Patch releases (X.Y.Z, X.Y.Z+1, etc.) will happen, on an as-needed basis, as issues are reported and fixed.

    These releases will be 100% compatible with the associated feature release.
    So the answer to “should I upgrade to the latest patch release?” will always be “yes.”

    The only exception to the above with respect to 100% backwards compatibility is when a security or data loss issue can’t be fixed without breaking backwards-compatibility.
    If this happens, the release notes will provide detailed upgrade instructions.
    **No new features will be added in patch releases**