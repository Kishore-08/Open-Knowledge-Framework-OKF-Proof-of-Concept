---
id: kubernetes-2-create-the-corresponding-runtimeclass-resources-3540e4aa
type: concept
title: 2. Create the corresponding RuntimeClass resources
description: The configurations setup in step 1 should each have an associated `handler`
  name, which identifies
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/runtime-class/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### 2. Create the corresponding RuntimeClass resources

The configurations setup in step 1 should each have an associated `handler` name, which identifies
the configuration. For each handler, create a corresponding RuntimeClass object.

The RuntimeClass resource currently only has 2 significant fields: the RuntimeClass name
(`metadata.name`) and the handler (`handler`). The object definition looks like this:

```
# RuntimeClass is defined in the node.k8s.io API group
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  # The name the RuntimeClass will be referenced by.
  # RuntimeClass is a non-namespaced resource.
  name: myclass 
# The name of the corresponding CRI configuration
handler: myconfiguration
```

The name of a RuntimeClass object must be a valid
[DNS subdomain name](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#dns-subdomain-names).

#### Note:

It is recommended that RuntimeClass write operations (create/update/patch/delete) be
restricted to the cluster administrator. This is typically the default. See
[Authorization Overview](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) for more details.