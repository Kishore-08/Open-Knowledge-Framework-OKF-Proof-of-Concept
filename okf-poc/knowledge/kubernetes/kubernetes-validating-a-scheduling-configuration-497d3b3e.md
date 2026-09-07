---
id: kubernetes-validating-a-scheduling-configuration-497d3b3e
type: concept
title: Validating a scheduling configuration
description: '`Validate` checks a configuration in two layers:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### Validating a scheduling configuration

`Validate` checks a configuration in two layers:

- **Structural validation** of the building blocks themselves: required fields, value ranges,
  the rule that exactly one member of a union is set, and immutability. These checks come from
  [declarative validation](https://kubernetes.io/docs/reference/using-api/declarative-validation/) rules generated
  from the API types.
- **Controller-policy checks** that declarative validation cannot express: the allow-lists
  described below, and cross-field rules such as rejecting the `all` disruption mode alongside
  the `basic` policy.

Validation also differs between creating and updating an object. On an update, the library
additionally enforces the fields that are frozen after creation, which means the controller
has to supply the previously stored configuration along with the new one. On a create there is
nothing to compare against, so those checks do not apply.

#### Opting out of declarative validation

Whether you want the first layer depends on where your controller runs, and one option
controls it:

- **Out-of-tree controllers** leave declarative validation enabled, which is the default.
  Nothing else applies those structural rules to a custom resource, so a single `Validate`
  call covers both layers.
- **In-tree controllers** set `DisableDeclarativeValidation`, because the API server already
  runs declarative validation on the embedded blocks while validating the parent object.
  Skipping the first layer avoids checking the same fields twice, leaving `Validate` to run
  only the controller-policy checks.

#### Opting in to scheduling options

Because the building-block types are shared across controllers, future releases may add
scheduling options that do not make sense for every controller. To keep new options from
silently leaking in, `workloadbuilder` uses an allow-list model: a controller declares the
policies and disruption modes it supports, and `Validate` rejects anything outside that set,
reporting the error at the offending block's field path.

Options are therefore denied by default. When a new policy is introduced, an existing
controller keeps rejecting it until its maintainers extend the allow-list, which for an
out-of-tree controller means updating its vendored copy of the library as well.

```
builder := workloadbuilder.NewBuilder(item, workloadbuilder.BuildOptions{
    Owner:                  owner,
    AllowedPolicies:        []workloadbuilder.SchedulingPolicyOption{workloadbuilder.BasicPolicy, workloadbuilder.GangPolicy},
    AllowedDisruptionModes: []workloadbuilder.DisruptionModeOption{workloadbuilder.SingleMode, workloadbuilder.AllMode},
})
allErrs := builder.Validate(ctx, workloadbuilder.ValidationInput{})
```