---
id: kubernetes-vsphere-1915a01d
type: concept
title: vSphere
description: 'There are two types of provisioners for vSphere storage classes:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/storage/storage-classes/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

### vSphere

There are two types of provisioners for vSphere storage classes:

- [CSI provisioner](https://kubernetes.io/docs/concepts/storage/storage-classes/#vsphere-provisioner-csi): `csi.vsphere.vmware.com`
- [vCP provisioner](https://kubernetes.io/docs/concepts/storage/storage-classes/#vcp-provisioner): `kubernetes.io/vsphere-volume`

In-tree provisioners are [deprecated](https://kubernetes.io/blog/2019/12/09/kubernetes-1-17-feature-csi-migration-beta/#why-are-we-migrating-in-tree-plugins-to-csi).
For more information on the CSI provisioner, see
[Kubernetes vSphere CSI Driver](https://vsphere-csi-driver.sigs.k8s.io/) and
[vSphereVolume CSI migration](https://kubernetes.io/docs/concepts/storage/volumes/#vsphere-csi-migration).

#### CSI Provisioner

The vSphere CSI StorageClass provisioner works with Tanzu Kubernetes clusters.
For an example, refer to the [vSphere CSI repository](https://github.com/kubernetes-sigs/vsphere-csi-driver/blob/master/example/vanilla-k8s-RWM-filesystem-volumes/example-sc.yaml).

#### vCP Provisioner

The following examples use the VMware Cloud Provider (vCP) StorageClass provisioner.

1. Create a StorageClass with a user specified disk format.

   ```
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: fast
   provisioner: kubernetes.io/vsphere-volume
   parameters:
     diskformat: zeroedthick
   ```

   `diskformat`: `thin`, `zeroedthick` and `eagerzeroedthick`. Default: `"thin"`.
2. Create a StorageClass with a disk format on a user specified datastore.

   ```
   apiVersion: storage.k8s.io/v1
   kind: StorageClass
   metadata:
     name: fast
   provisioner: kubernetes.io/vsphere-volume
   parameters:
     diskformat: zeroedthick
     datastore: VSANDatastore
   ```

   `datastore`: The user can also specify the datastore in the StorageClass.
   The volume will be created on the datastore specified in the StorageClass,
   which in this case is `VSANDatastore`. This field is optional. If the
   datastore is not specified, then the volume will be created on the datastore
   specified in the vSphere config file used to initialize the vSphere Cloud
   Provider.
3. Storage Policy Management inside kubernetes

   - Using existing vCenter SPBM policy

     One of the most important features of vSphere for Storage Management is
     policy based Management. Storage Policy Based Management (SPBM) is a
     storage policy framework that provides a single unified control plane
     across a broad range of data services and storage solutions. SPBM enables
     vSphere administrators to overcome upfront storage provisioning challenges,
     such as capacity planning, differentiated service levels and managing
     capacity headroom.

     The SPBM policies can be specified in the StorageClass using the
     `storagePolicyName` parameter.
   - Virtual SAN policy support inside Kubernetes

     Vsphere Infrastructure (VI) Admins will have the ability to specify custom
     Virtual SAN Storage Capabilities during dynamic volume provisioning. You
     can now define storage requirements, such as performance and availability,
     in the form of storage capabilities during dynamic volume provisioning.
     The storage capability requirements are converted into a Virtual SAN
     policy which are then pushed down to the Virtual SAN layer when a
     persistent volume (virtual disk) is being created. The virtual disk is
     distributed across the Virtual SAN datastore to meet the requirements.

     You can see [Storage Policy Based Management for dynamic provisioning of volumes](https://github.com/vmware-archive/vsphere-storage-for-kubernetes/blob/fa4c8b8ad46a85b6555d715dd9d27ff69839df53/documentation/policy-based-mgmt.md)
     for more details on how to use storage policies for persistent volumes
     management.