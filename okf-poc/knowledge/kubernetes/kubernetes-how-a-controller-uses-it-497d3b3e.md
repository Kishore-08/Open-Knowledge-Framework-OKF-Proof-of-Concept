---
id: kubernetes-how-a-controller-uses-it-497d3b3e
type: concept
title: How a controller uses it
description: A controller describes its workload as a tree of `WorkloadItem` nodes,
  one per logical
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/workloads/workload-api/workloadbuilder/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

### How a controller uses it

A controller describes its workload as a tree of `WorkloadItem` nodes, one per logical
component. A node with no children becomes a single `PodGroupTemplate`, while a node with
children becomes a `CompositePodGroupTemplate` over them, which is how a multi-level
controller represents a group of groups. Each node carries:

- a *default config*, the controller's own defaults for anything the user leaves unset. This
  is where a controller decides, for example, that an unconfigured Job stays on `basic`
  scheduling.
- an *input*, the user's intent taken from the controller's API. The controller records each
  building block together with the field path it lives at, so validation errors point at the
  exact field the user set.
- optional *callbacks*, which adjust the merged configuration. This is how a controller
  supplies a context-specific default, such as filling in an unset gang minimum count from
  the Job's parallelism.

The controller then hands that tree to a `Builder` and works through four calls:

1. `NewBuilder` constructs the builder from the tree, along with the name, namespace, and
   owner reference for the object to be produced. The owner becomes the Workload's
   controller reference, which is used for discovery and garbage collection.
2. `Validate` resolves the tree and reports any problems as a list of field errors, which a
   controller returns from its own API validation.
3. `BuildWorkload` compiles the tree into a Workload. The result is cached, so several
   PodGroups can be created from one compiled result.
4. `NewPodGroup` creates a runtime PodGroup from one of the compiled templates, naming the
   template it should be built from.

```
builder := workloadbuilder.NewBuilder(item, opts)
if errs := builder.Validate(ctx, workloadbuilder.ValidationInput{}); len(errs) > 0 {
    // reject the request
}
workload, err := builder.BuildWorkload()
podGroup, err := builder.NewPodGroup("trainer-pg", item.Name)
```

For complete, runnable versions of this flow, including how the Job controller wires it up,
see the examples in the
[package reference](https://pkg.go.dev/k8s.io/component-helpers/scheduling/schedulingv1/workloadbuilder).