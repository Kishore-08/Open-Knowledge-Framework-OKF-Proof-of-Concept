---
id: kubernetes-creating-a-secret-with-a-docker-config-c440e1a7
type: concept
title: Creating a Secret with a Docker config
description: You need to know the username, registry password and client email address
  for authenticating
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/containers/images/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

### Creating a Secret with a Docker config

You need to know the username, registry password and client email address for authenticating
to the registry, as well as its hostname.
Run the following command, substituting placeholders with the appropriate values:

```
kubectl create secret docker-registry <name> \
  --docker-server=<docker-registry-server> \
  --docker-username=<docker-user> \
  --docker-password=<docker-password> \
  --docker-email=<docker-email>
```

If you already have a Docker credentials file then, rather than using the above
command, you can import the credentials file as a Kubernetes
[Secret](https://kubernetes.io/docs/concepts/configuration/secret/ "Stores sensitive information, such as passwords, OAuth tokens, and ssh keys.").
[Create a Secret based on existing Docker credentials](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#registry-secret-existing-credentials)
explains how to set this up.

This is particularly useful if you are using multiple private container
registries, as `kubectl create secret docker-registry` creates a Secret that
only works with a single private registry.

#### Note:

Pods can only reference image pull secrets in their own namespace,
so this process needs to be done one time per namespace.

#### Referring to `imagePullSecrets` on a Pod

Now, you can create pods which reference that secret by adding the `imagePullSecrets`
section to a Pod definition. Each item in the `imagePullSecrets` array can only
reference one Secret in the same namespace.

For example:

```
cat <<EOF > pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: foo
  namespace: awesomeapps
spec:
  containers:
    - name: foo
      image: janedoe/awesomeapp:v1
  imagePullSecrets:
    - name: myregistrykey
EOF

cat <<EOF >> ./kustomization.yaml
resources:
- pod.yaml
EOF
```

This needs to be done for each Pod that is using a private registry.

However, you can automate this process by specifying the `imagePullSecrets` section
in a [ServiceAccount](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/)
resource. See [Add ImagePullSecrets to a Service Account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#add-imagepullsecrets-to-a-service-account)
for detailed instructions.

You can use this in conjunction with a per-node `.docker/config.json`. The credentials
will be merged.