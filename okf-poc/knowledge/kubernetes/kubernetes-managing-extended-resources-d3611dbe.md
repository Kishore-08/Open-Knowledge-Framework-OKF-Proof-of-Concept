---
id: kubernetes-managing-extended-resources-d3611dbe
type: concept
title: Managing extended resources
description: Node-level extended resources are tied to nodes.
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### Managing extended resources

#### Node-level extended resources

Node-level extended resources are tied to nodes.

##### Device plugin managed resources

See [Device
Plugin](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/)
for how to advertise device plugin managed resources on each node.

##### Other resources

To advertise a new node-level extended resource, the cluster operator can
submit a `PATCH` HTTP request to the API server to specify the available
quantity in the `status.capacity` for a node in the cluster. After this
operation, the node's `status.capacity` will include a new resource. The
`status.allocatable` field is updated automatically with the new resource
asynchronously by the kubelet.

Because the scheduler uses the node's `status.allocatable` value when
evaluating Pod fitness, the scheduler only takes account of the new value after
that asynchronous update. There may be a short delay between patching the
node capacity with a new resource and the time when the first Pod that requests
the resource can be scheduled on that node.

**Example:**

Here is an example showing how to use `curl` to form an HTTP request that
advertises five "example.com/foo" resources on node `k8s-node-1` whose master
is `k8s-master`.

```
curl --header "Content-Type: application/json-patch+json" \
--request PATCH \
--data '[{"op": "add", "path": "/status/capacity/example.com~1foo", "value": "5"}]' \
http://k8s-master:8080/api/v1/nodes/k8s-node-1/status
```

#### Note:

In the preceding request, `~1` is the encoding for the character `/`
in the patch path. The operation path value in JSON-Patch is interpreted as a
JSON-Pointer. For more details, see
[IETF RFC 6901, section 3](https://datatracker.ietf.org/doc/html/rfc6901#section-3).

#### Cluster-level extended resources

Cluster-level extended resources are not tied to nodes. They are usually managed
by scheduler extenders, which handle the resource consumption and resource quota.

You can specify the extended resources that are handled by scheduler extenders
in [scheduler configuration](https://kubernetes.io/docs/reference/config-api/kube-scheduler-config.v1/)

**Example:**

The following configuration for a scheduler policy indicates that the
cluster-level extended resource "example.com/foo" is handled by the scheduler
extender.

- The scheduler sends a Pod to the scheduler extender only if the Pod requests
  "example.com/foo".
- The `ignoredByScheduler` field specifies that the scheduler does not check
  the "example.com/foo" resource in its `PodFitsResources` predicate.

```
{
  "kind": "Policy",
  "apiVersion": "v1",
  "extenders": [
    {
      "urlPrefix":"<extender-endpoint>",
      "bindVerb": "bind",
      "managedResources": [
        {
          "name": "example.com/foo",
          "ignoredByScheduler": true
        }
      ]
    }
  ]
}
```

#### Extended resources allocation by DRA

Extended resources allocation by DRA allows cluster administrators to specify an `extendedResourceName`
in DeviceClass, then the devices matching the DeviceClass can be requested from a pod's extended
resource requests. Read more about
[Extended Resource allocation by DRA](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation/#extended-resource).