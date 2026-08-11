---
id: kubernetes-develop-lifecycle-phase-4d305e15
type: concept
title: '*Develop* lifecycle phase'
description: '- Ensure the integrity of development environments.'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/security/cloud-native-security/
updated_at: '2026-08-08'
created_at: '2026-08-08'
---

## *Develop* lifecycle phase

- Ensure the integrity of development environments.
- Design applications following good practices for information security,
  appropriate for your context.
- Consider end user security as part of solution design.

To achieve this, you can:

1. Adopt an architecture, such as [zero trust](https://glossary.cncf.io/zero-trust-architecture/),
   that minimizes attack surfaces, even for internal threats.
2. Define a code review process that considers security concerns.
3. Build a *threat model* of your system or application that identifies
   trust boundaries. Use that threat model to identify risks and determine
   how to treat them.
4. Incorporate advanced security automation, such as *fuzzing* and
   [security chaos engineering](https://glossary.cncf.io/security-chaos-engineering/),
   where it's justified.