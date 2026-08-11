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
 
31. What are Kubernetes Secrets? 
Answer 
Secrets store sensitive data like passwords, tokens, and keys. 
Example: 
apiVersion: v1 
kind: Secret 
data: 
  password: cGFzc3dvcmQ= 
(Base64 encoded, not encrypted by default) 
 
Important Point 
Secrets are not truly secure by default: 
●​ Stored in etcd 
●​ Base64 encoded only 
 
Better Security Options 
●​ Encryption at rest in etcd 
●​ External secret managers: 
○​ AWS Secrets Manager 
○​ HashiCorp Vault 
 
Interview Answer 
