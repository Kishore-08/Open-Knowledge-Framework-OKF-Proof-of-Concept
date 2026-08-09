---
id: kubernetes-device-plugin-implementation-3614a558
type: concept
title: Device plugin implementation
description: 'The general workflow of a device plugin includes the following steps:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/device-plugins/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## Device plugin implementation

The general workflow of a device plugin includes the following steps:

1. Initialization. During this phase, the device plugin performs vendor-specific
   initialization and setup to make sure the devices are in a ready state.
2. The plugin starts a gRPC service, with a Unix socket under the host path
   `/var/lib/kubelet/device-plugins/` (this path is hardcoded and is not
   affected by the kubelet's `--root-dir` or any other configuration), that
   implements the following interfaces:

   ```
   service DevicePlugin {
         // GetDevicePluginOptions returns options to be communicated with Device Manager.
         rpc GetDevicePluginOptions(Empty) returns (DevicePluginOptions) {}

         // ListAndWatch returns a stream of List of Devices
         // Whenever a Device state change or a Device disappears, ListAndWatch
         // returns the new list
         rpc ListAndWatch(Empty) returns (stream ListAndWatchResponse) {}

         // Allocate is called during container creation so that the Device
         // Plugin can run device specific operations and instruct Kubelet
         // of the steps to make the Device available in the container
         rpc Allocate(AllocateRequest) returns (AllocateResponse) {}

         // GetPreferredAllocation returns a preferred set of devices to allocate
         // from a list of available ones. The resulting preferred allocation is not
         // guaranteed to be the allocation ultimately performed by the
         // devicemanager. It is only designed to help the devicemanager make a more
         // informed allocation decision when possible.
         rpc GetPreferredAllocation(PreferredAllocationRequest) returns (PreferredAllocationResponse) {}

         // PreStartContainer is called, if indicated by Device Plugin during registration phase,
         // before each container start. Device plugin can run device specific operations
         // such as resetting the device before making devices available to the container.
         rpc PreStartContainer(PreStartContainerRequest) returns (PreStartContainerResponse) {}
   }
   ```

   #### Note:

   Plugins are not required to provide useful implementations for
   `GetPreferredAllocation()` or `PreStartContainer()`. Flags indicating
   the availability of these calls, if any, should be set in the `DevicePluginOptions`
   message sent back by a call to `GetDevicePluginOptions()`. The `kubelet` will
   always call `GetDevicePluginOptions()` to see which optional functions are
   available, before calling any of them directly.
3. The plugin registers itself with the kubelet through the Unix socket at host
   path `/var/lib/kubelet/device-plugins/kubelet.sock`.

   #### Note:

   The ordering of the workflow is important. A plugin MUST start serving gRPC
   service before registering itself with kubelet for successful registration.
4. After successfully registering itself, the device plugin runs in serving mode, during which it keeps
   monitoring device health and reports back to the kubelet upon any device state changes.
   It is also responsible for serving `Allocate` gRPC requests. During `Allocate`, the device plugin may
   do device-specific preparation; for example, GPU cleanup or QRNG initialization.
   If the operations succeed, the device plugin returns an `AllocateResponse` that contains container
   runtime configurations for accessing the allocated devices. The kubelet passes this information
   to the container runtime.

   An `AllocateResponse` contains zero or more `ContainerAllocateResponse` objects. In these, the
   device plugin defines modifications that must be made to a container's definition to provide
   access to the device. These modifications include:

   - [Annotations](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/)
   - device nodes
   - environment variables
   - mounts
   - fully-qualified CDI device names

   #### Note:

   The processing of th