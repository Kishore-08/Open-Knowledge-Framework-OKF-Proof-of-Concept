---
id: kubernetes-derived-attributes-c976d546
type: concept
title: Derived attributes
description: 'FEATURE STATE:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/resource-management/dynamic-resource-allocation/dra-api/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Derived attributes

FEATURE STATE:
`Kubernetes v1.37 [alpha]`(disabled by default)

The `matchAttribute` and `distinctAttribute` constraints normally require
devices to publish attributes under the exact same name. If a GPU driver
publishes `pcie_locality` and a NIC driver publishes `pcie_root` (or embeds
the same information in a string like `numa0-pcie1`), the scheduler has no
way to recognize that these represent the same thing, so devices from the
two drivers can't be co-located without first agreeing on a shared
attribute name.

`derivedAttributes` lets you bridge this gap inline, without waiting for
drivers to standardize on shared attribute names. Add one or more
`derivedAttributes` entries to a request, under
`.spec.devices.requests[].exactly` or
`.spec.devices.requests[].firstAvailable[]`. Each entry defines a CEL
expression that the scheduler evaluates against every candidate device for
that request. The result becomes a virtual attribute that can be referenced
from a `matchAttribute` or `distinctAttribute` constraint exactly like a
driver-provided device attribute.

```
apiVersion: resource.k8s.io/v1
kind: ResourceClaim
metadata:
  name: gpu-nic-numa-alignment
spec:
  devices:
    requests:
    - name: gpu
      exactly:
        deviceClassName: gpu.example.com
        count: 1
        derivedAttributes:
        - name: derived/numa
          expression: device.attributes["gpu.example.com"].numa
    - name: nic
      exactly:
        deviceClassName: nic.example.com
        count: 1
        derivedAttributes:
        - name: derived/numa
          expression: device.attributes["nic.example.com"].numaNode
    constraints:
    - requests: ["gpu", "nic"]
      matchAttribute: derived/numa
```

In this example, the `gpu` and `nic` drivers publish topology information
under different attribute names (`numa` and `numaNode`). Each request
computes a common `derived/numa` value from its own device's attributes,
and the `matchAttribute` constraint aligns the two requests on that virtual
attribute, even though the underlying drivers never agreed on a shared
attribute name.

A few things to know about `derivedAttributes`:

- **Naming**: `name` must be a DNS subdomain followed by a `/` and a C
  identifier, the same format used for driver-provided attribute names (for
  example, `example.com/numaNode` or `derived/numaNode`). If the name
  matches a driver-provided attribute already published by the driver,
  the derived attribute's value shadows the driver-provided one for
  constraint matching. Use a domain prefix that no driver would use,
  such as `derived/`, if you want to avoid shadowing unintentionally.
  You can define up to 32 derived attributes per request.
- **Must be used by a constraint**: every derived attribute must be
  referenced by at least one `matchAttribute` or `distinctAttribute`
  constraint that applies to the request (or subrequest) that defines it.
  Otherwise the ResourceClaim fails validation.
- **Evaluation scope and order**: `expression` is evaluated once per
  candidate device, after the request's own CEL selectors
  (`.selectors[].cel`) have already filtered that device. As a result,
  derived attributes can't be referenced from selector expressions, and
  aren't exposed through `device.attributes` in the CEL environment.
- **Return type**: `expression` must evaluate to a scalar (`string`, `int`,
  `bool`, or a semantic version) or, when the `DRAListTypeAttributes`
  feature gate is also enabled, a list of one of those scalar types.
- **Cost limits**: each expression has a maximum length and a limit on its
  estimated CEL evaluation cost. On top of that, the combined estimated cost
  of all `derivedAttributes` expressions in a ResourceClaim is also capped,
  to bound the total overhead added to a single scheduling attempt. The
  ResourceClaim is rejected if any of these limits are exceeded.
- **Runtime errors abort scheduling**: if evaluating an expression fails for
  a candidate device, for ex