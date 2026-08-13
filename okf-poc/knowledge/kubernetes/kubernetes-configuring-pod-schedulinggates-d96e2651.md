---
id: kubernetes-configuring-pod-schedulinggates-d96e2651
type: concept
title: Configuring Pod schedulingGates
description: The `schedulingGates` field contains a list of strings, and each string
  literal is perceived as a
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/scheduling-eviction/pod-scheduling-readiness/
updated_at: '2026-08-13'
created_at: '2026-08-13'
---

## Configuring Pod schedulingGates

The `schedulingGates` field contains a list of strings, and each string literal is perceived as a
criteria that Pod should be satisfied before considered schedulable. This field can be initialized
only when a Pod is created (either by the client, or mutated during admission). After creation,
each schedulingGate can be removed in arbitrary order, but addition of a new scheduling gate is disallowed.

[![pod-scheduling-gates-diagram](https://kubernetes.io/docs/images/podSchedulingGates.svg)](https://mermaid.live/edit#pako:eNplkktTwyAUhf8KgzuHWpukaYszutGlK3caFxQuCVMCGSDVTKf_XfKyPlhxz4HDB9wT5lYAptgHFuBRsdKxenFMClMYFIdfUdRYgbiD6ItJTEbR8wpEq5UpUfnDTf-5cbPoJjcbXdcaE61RVJIiqJvQ_Y30D-OCt-t3tFjcR5wZayiVnIGmkv4NiEfX9jijKTmmRH5jf0sRugOP0HyHUc1m6KGMFP27cM28fwSJDluPpNKaXqVJzmFNfHD2APRKSjnNFx9KhIpmzSfhVls3eHdTRrwG8QnxKfEZUUNeYTDBNbiaKRF_5dSfX-BQQQ0FpnEqQLJWhwIX5hyXsjbYl85wTINrgeC2EZd_xFQy7b_VJ6GCdd-itkxALE84dE3fAqXyIUZya6Qqe711OspVCI2ny2Vv35QqVO3-htt66ZWomAvVcZcv8yTfsiSFfJOydZoKvl_ttjLJVlJsblcJw-czwQ0zr9ZeqGDgeR77b2jD8xdtjtDn)

Figure. Pod SchedulingGates