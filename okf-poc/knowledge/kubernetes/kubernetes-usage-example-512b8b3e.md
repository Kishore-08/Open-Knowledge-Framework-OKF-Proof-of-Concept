---
id: kubernetes-usage-example-512b8b3e
type: concept
title: Usage example
description: To work with Pod overhead, you need a RuntimeClass that defines the `overhead`
  field. As
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-overhead/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Usage example

To work with Pod overhead, you need a RuntimeClass that defines the `overhead` field. As
an example, you could use the following RuntimeClass definition with a virtualization container
runtime (in this example, Kata Containers combined with the Firecracker virtual machine monitor)
that uses around 120MiB per Pod for the virtual machine and the guest OS:

```
# You need to change this example to match the actual runtime name, and per-Pod
# resource overhead, that the container runtime is adding in your cluster.
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: kata-fc
handler: kata-fc
overhead:
  podFixed:
    memory: "120Mi"
    cpu: "250m"
```

Workloads which are created which specify the `kata-fc` RuntimeClass handler will take the memory and
cpu overheads into account for resource quota calculations, node scheduling, as well as Pod cgroup sizing.

Consider running the given example workload, test-pod:

```
apiVersion: v1
kind: Pod
metadata:
  name: test-pod
spec:
  runtimeClassName: kata-fc
  containers:
  - name: busybox-ctr
    image: busybox:1.28
    stdin: true
    tty: true
    resources:
      limits:
        cpu: 500m
        memory: 100Mi
  - name: nginx-ctr
    image: nginx
    resources:
      limits:
        cpu: 1500m
        memory: 100Mi
```

#### Note:

If only `limits` are specified in the pod definition, kubelet will deduce `requests` from those limits and set them to be the same as the defined `limits`.

At admission time the RuntimeClass [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)
updates the workload's PodSpec to include the `overhead` as described in the RuntimeClass. If the PodSpec already has this field defined,
the Pod will be rejected. In the given example, since only the RuntimeClass name is specified, the admission controller mutates the Pod
to include an `overhead`.

After the RuntimeClass admission controller has made modifications, you can check the updated
Pod overhead value:

```
kubectl get pod test-pod -o jsonpath='{.spec.overhead}'
```

The output is:

```
map[cpu:250m memory:120Mi]
```

If a [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) is defined, the sum of container requests as well as the
`overhead` field are counted.

When the kube-scheduler is deciding which node should run a new Pod, the scheduler considers that Pod's
`overhead` as well as the sum of container requests for that Pod. For this example, the scheduler adds the
requests and the overhead, then looks for a node that has 2.25 CPU and 320 MiB of memory available.

Once a Pod is scheduled to a node, the kubelet on that node creates a new [cgroup](https://kubernetes.io/docs/reference/glossary/?all=true#term-cgroup "A group of Linux processes with optional resource isolation, accounting and limits.") for the Pod. It is within this pod that the underlying
container runtime will create containers.

If the resource has a limit defined for each container (Guaranteed QoS or Burstable QoS with limits defined),
the kubelet will set an upper limit for the pod cgroup associated with that resource (cpu.cfs\_quota\_us for CPU
and memory.limit\_in\_bytes memory). This upper limit is based on the sum of the container limits plus the `overhead`
defined in the PodSpec.

For CPU, if the Pod is Guaranteed or Burstable QoS, the kubelet will set `cpu.shares` based on the
sum of container requests plus the `overhead` defined in the PodSpec.

Looking at our example, verify the container requests for the workload:

```
kubectl get pod test-pod -o jsonpath='{.spec.containers[*].resources.limits}'
```

The total container requests are 2000m CPU and 200MiB of memory:

```
map[cpu: 500m memory:100Mi] map[cpu:1500m memory:100Mi]
```

Check this against what is observed by the node:

```
kubectl describe node | grep test-pod -B2
```

The output shows requests for 2250m CPU, and for 320MiB of memory. The requests include Pod overhead: