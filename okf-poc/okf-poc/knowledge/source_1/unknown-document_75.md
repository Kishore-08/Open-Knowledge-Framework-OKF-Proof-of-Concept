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
Principle: Alert on Symptoms, Not Causes 
 
Good Alerts 
●​ High error rate 
●​ High latency 
●​ Pod crash rate 
●​ Node NotReady 
 
Bad Alerts 
●​ CPU > 70% (alone) 
●​ Memory > 80% (alone) 
 
SLO-Based Alerts 
Example: 
99.9% availability 
 
Tools 
●​ Alertmanager 
 
Interview Answer 
Alerting should focus on user impact and SLO violations rather than raw infrastructure metrics. 
 
55. Explain Kubernetes Operator pattern 
