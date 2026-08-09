---
id: unknown-document
type: concept
title: Unknown Document
description: Metadata extraction failed.
category: unknown
tags:
- unclassified
source: null
created_at: '2026-08-05'
updated_at: '2026-08-05'
aliases: []
related: []
document_type: Unknown
trust_level: Low
---

None
RoleBinding 
  | 
  v 
Role → API resources (pods, deployments) 
 
Example Rule 
resources: ["pods"] 
verbs: ["get", "list"] 
 
Interview Answer 
RBAC ensures least privilege access to Kubernetes resources via roles and bindings. 
 
34. How do Service Accounts work? 
Answer 
Service Accounts are identities for pods. 
 
Default Behavior 
Every pod gets: 
