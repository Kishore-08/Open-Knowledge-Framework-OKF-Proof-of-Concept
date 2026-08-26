---
id: python-specifying-custom-filter-chains-https-docs-python-org-3-libr-266ffa0e
type: concept
title: Specifying custom filter chains[¶](https://docs.python.org/3/library/lzma.html#specifying-custom-filter-chains
  "Link to this heading")
description: A filter chain specifier is a sequence of dictionaries, where each dictionary
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/lzma.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

## Specifying custom filter chains[¶](https://docs.python.org/3/library/lzma.html#specifying-custom-filter-chains "Link to this heading")

A filter chain specifier is a sequence of dictionaries, where each dictionary
contains the ID and options for a single filter. Each dictionary must contain
the key `"id"`, and may contain additional keys to specify filter-dependent
options. Valid filter IDs are as follows:

- Compression filters:

  - [`FILTER_LZMA1`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA1 "lzma.FILTER_LZMA1") (for use with [`FORMAT_ALONE`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_ALONE "lzma.FORMAT_ALONE"))
  - [`FILTER_LZMA2`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_LZMA2 "lzma.FILTER_LZMA2") (for use with [`FORMAT_XZ`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_XZ "lzma.FORMAT_XZ") and [`FORMAT_RAW`](https://docs.python.org/3/library/lzma.html#lzma.FORMAT_RAW "lzma.FORMAT_RAW"))
- Delta filter:

  - [`FILTER_DELTA`](https://docs.python.org/3/library/lzma.html#lzma.FILTER_DELTA "lzma.FILTER_DELTA")
- Branch-Call-Jump (BCJ) filters:

  - `FILTER_X86`
  - `FILTER_IA64`
  - `FILTER_ARM`
  - `FILTER_ARMTHUMB`
  - `FILTER_POWERPC`
  - `FILTER_SPARC`

A filter chain can consist of up to 4 filters, and cannot be empty. The last
filter in the chain must be a compression filter, and any other filters must be
delta or BCJ filters.

Compression filters support the following options (specified as additional
entries in the dictionary representing the filter):

- `preset`: A compression preset to use as a source of default values for
  options that are not specified explicitly.
- `dict_size`: Dictionary size in bytes. This should be between 4 KiB and
  1.5 GiB (inclusive).
- `lc`: Number of literal context bits.
- `lp`: Number of literal position bits. The sum `lc + lp` must be at
  most 4.
- `pb`: Number of position bits; must be at most 4.
- `mode`: [`MODE_FAST`](https://docs.python.org/3/library/lzma.html#lzma.MODE_FAST "lzma.MODE_FAST") or [`MODE_NORMAL`](https://docs.python.org/3/library/lzma.html#lzma.MODE_NORMAL "lzma.MODE_NORMAL").
- `nice_len`: What should be considered a “nice length” for a match.
  This should be 273 or less.
- `mf`: What match finder to use – [`MF_HC3`](https://docs.python.org/3/library/lzma.html#lzma.MF_HC3 "lzma.MF_HC3"), [`MF_HC4`](https://docs.python.org/3/library/lzma.html#lzma.MF_HC4 "lzma.MF_HC4"),
  [`MF_BT2`](https://docs.python.org/3/library/lzma.html#lzma.MF_BT2 "lzma.MF_BT2"), [`MF_BT3`](https://docs.python.org/3/library/lzma.html#lzma.MF_BT3 "lzma.MF_BT3"), or [`MF_BT4`](https://docs.python.org/3/library/lzma.html#lzma.MF_BT4 "lzma.MF_BT4").
- `depth`: Maximum search depth used by match finder. 0 (default) means to
  select automatically based on other filter options.

The delta filter stores the differences between bytes, producing more repetitive
input for the compressor in certain circumstances. It supports one option,
`dist`. This indicates the distance between bytes to be subtracted. The
default is 1, i.e. take the differences between adjacent bytes.

The BCJ filters are intended to be applied to machine code. They convert
relative branches, calls and jumps in the code to use absolute addressing, with
the aim of increasing the redundancy that can be exploited by the compressor.
These filters support one option, `start_offset`. This specifies the address
that should be mapped to the beginning of the input data. The default is 0.