---
id: kubernetes-request-flow-ca23283c
type: concept
title: Request flow
description: 'Here is a simple example of HTTP traffic being routed to a Service by
  using a Gateway and an HTTPRoute:'
category: kubernetes
tags: []
source:
  name: kubernetes
  url: https://kubernetes.io/docs/concepts/services-networking/gateway/
updated_at: '2026-08-27'
created_at: '2026-08-27'
---

## Request flow

Here is a simple example of HTTP traffic being routed to a Service by using a Gateway and an HTTPRoute:

![A diagram that provides an example of HTTP traffic being routed to a Service by using a Gateway and an HTTPRoute](https://kubernetes.io/docs/images/gateway-request-flow.svg)

In this example, the request flow for a Gateway implemented as a reverse proxy is:

1. The client starts to prepare an HTTP request for the URL `http://www.example.com`
2. The client's DNS resolver queries for the destination name and learns a mapping to
   one or more IP addresses associated with the Gateway.
3. The client sends a request to the Gateway IP address; the reverse proxy receives the HTTP
   request and uses the Host: header to match a configuration that was derived from the Gateway
   and attached HTTPRoute.
4. Optionally, the reverse proxy can perform request header and/or path matching based
   on match rules of the HTTPRoute.
5. Optionally, the reverse proxy can modify the request; for example, to add or remove headers,
   based on filter rules of the HTTPRoute.
6. Lastly, the reverse proxy forwards the request to one or more backends.