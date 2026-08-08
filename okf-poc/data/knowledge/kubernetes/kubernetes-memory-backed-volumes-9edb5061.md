---
id: kubernetes-memory-backed-volumes-9edb5061
type: concept
title: Memory-backed volumes
description: On Linux nodes, memory-backed volumes (such as [`secret`](https://kubernetes.io/docs/concepts/configuration/secret/)
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Memory-backed volumes

On Linux nodes, memory-backed volumes (such as [`secret`](https://kubernetes.io/docs/concepts/configuration/secret/)
volume mounts, or [`emptyDir`](https://kubernetes.io/docs/concepts/storage/volumes/#emptydir) with `medium: Memory`)
are implemented with a `tmpfs` filesystem.
The contents of such volumes should remain in memory at all times, hence should
not be swapped to disk.
To ensure the contents of such volumes remain in memory, the `noswap` tmpfs option
is being used.

The Linux kernel officially supports the `noswap` option from version 6.3 (more info
can be found in [Linux Kernel Version Requirements](https://kubernetes.io/docs/reference/node/kernel-version-requirements/#requirements-other)).
However, the different distributions often choose to backport this mount option to older
Linux versions as well.

In order to verify whether the node supports the `noswap` option, the kubelet will do the following:

- If the kernel's version is above 6.3 then the `noswap` option will be assumed to be supported.
- Otherwise, kubelet would try to mount a dummy tmpfs with the `noswap` option at startup.
  If kubelet fails with an error indicating of an unknown option, `noswap` will be assumed
  to not be supported, hence will not be used.
  A kubelet log entry will be emitted to warn the user about memory-backed volumes might swap to disk.
  If kubelet succeeds, the dummy tmpfs will be deleted and the `noswap` option will be used.
  - If the `noswap` option is not supported, kubelet will emit a warning log entry,
    then continue its execution.

See the [section above](https://kubernetes.io/docs/concepts/cluster-administration/swap-memory-management/#setting-up-encrypted-swap) with an example for setting unencrypted swap.
However, handling encrypted swap is not within the scope of kubelet;
rather, it is a general OS configuration concern and should be addressed at that level.
It is the administrator's responsibility to provision encrypted swap to mitigate this risk.