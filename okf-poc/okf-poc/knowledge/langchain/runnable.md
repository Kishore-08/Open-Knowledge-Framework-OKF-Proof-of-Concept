---
id: langchain-runnable
type: concept
title: LangChain Runnable Interface
description: The standard interface implemented by LangChain components
category: langchain
tags: [langchain, runnable, lcel, chains, python]
source:
  name: LangChain Python Documentation
  url: https://python.langchain.com/docs/concepts/runnables/
updated_at: 2026-08-05
created_at: 2026-08-05
aliases: [Runnable, Runnable Interface, LCEL]
related: [langchain-chain]
---

## Runnable Interface

The Runnable interface is the standard interface implemented by most LangChain
components. It defines a common set of methods (invoke, batch, stream) so that
different components can be composed reliably.

## Core Methods

- `invoke(input)` - call the runnable on a single input.
- `batch(inputs)` - call the runnable on a list of inputs.
- `stream(input)` - call the runnable and stream the output chunks.
- `ainvoke`, `abatch`, `astream` - the corresponding async variants.

## Composition

Runnables can be composed with the pipe operator `|` to build chains. This is the
basis of the LangChain Expression Language (LCEL):

```python
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI(model="gpt-4o")
parser = StrOutputParser()
chain = model | parser

result = chain.invoke("Hello, world!")
```

`prompt | model | parser` is a Runnable itself, so it supports invoke, batch,
stream, and introspection.

## RunnablePassthrough and RunnableLambda

- `RunnablePassthrough` passes inputs through unchanged and can attach extra data.
- `RunnableLambda` wraps a plain Python function into a Runnable.
- `RunnableParallel` runs several Runnables in parallel and merges their outputs.

## Fallbacks and Retries

Runnables support `.with_fallbacks([...])` to try alternative Runnables when the
primary one fails, and `.with_retry()` to retry on transient errors.

## Streaming

Because chains are Runnables, streaming is preserved end to end: token chunks from
the model flow through the output parser to the caller via `stream()`.

## Debugging and Tracing

Every Runnable supports `.invoke(..., config={"callbacks": [...]})` and integrates
with LangSmith for tracing, so you can observe inputs, outputs, and latency of each
step in a chain.
