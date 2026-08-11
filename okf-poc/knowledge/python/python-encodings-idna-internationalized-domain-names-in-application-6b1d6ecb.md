---
id: python-encodings-idna-internationalized-domain-names-in-application-6b1d6ecb
type: concept
title: '`encodings.idna` — Internationalized Domain Names in Applications[¶](https://docs.python.org/3/library/codecs.html#module-encodings.idna
  "Link to this heading")'
description: This module implements [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html)
  (Internationalized Domain Names in
category: python
tags: []
source:
  name: python
  url: https://docs.python.org/3/library/codecs.html
updated_at: '2026-08-10'
created_at: '2026-08-10'
---

## `encodings.idna` — Internationalized Domain Names in Applications[¶](https://docs.python.org/3/library/codecs.html#module-encodings.idna "Link to this heading")

This module implements [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html) (Internationalized Domain Names in
Applications) and [**RFC 3492**](https://datatracker.ietf.org/doc/html/rfc3492.html) (Nameprep: A Stringprep Profile for
Internationalized Domain Names (IDN)). It builds upon the `punycode` encoding
and [`stringprep`](https://docs.python.org/3/library/stringprep.html#module-stringprep "stringprep: String preparation, as per RFC 3453").

If you need the IDNA 2008 standard from [**RFC 5891**](https://datatracker.ietf.org/doc/html/rfc5891.html) and [**RFC 5895**](https://datatracker.ietf.org/doc/html/rfc5895.html), use the
third-party [idna](https://pypi.org/project/idna/) module.

These RFCs together define a protocol to support non-ASCII characters in domain
names. A domain name containing non-ASCII characters (such as
`www.Alliancefrançaise.nu`) is converted into an ASCII-compatible encoding
(ACE, such as `www.xn--alliancefranaise-npb.nu`). The ACE form of the domain
name is then used in all places where arbitrary characters are not allowed by
the protocol, such as DNS queries, HTTP *Host* fields, and so
on. This conversion is carried out in the application; if possible invisible to
the user: The application should transparently convert Unicode domain labels to
IDNA on the wire, and convert back ACE labels to Unicode before presenting them
to the user.

Python supports this conversion in several ways: the `idna` codec performs
conversion between Unicode and ACE, separating an input string into labels
based on the separator characters defined in [**section 3.1 of RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html#section-3.1)
and converting each label to ACE as required, and conversely separating an input
byte string into labels based on the `.` separator and converting any ACE
labels found into unicode. Furthermore, the [`socket`](https://docs.python.org/3/library/socket.html#module-socket "socket: Low-level networking interface.") module
transparently converts Unicode host names to ACE, so that applications need not
be concerned about converting host names themselves when they pass them to the
socket module. On top of that, modules that have host names as function
parameters, such as [`http.client`](https://docs.python.org/3/library/http.client.html#module-http.client "http.client: HTTP and HTTPS protocol client (requires sockets).") and [`ftplib`](https://docs.python.org/3/library/ftplib.html#module-ftplib "ftplib: FTP protocol client (requires sockets)."), accept Unicode host
names (`http.client` then also transparently sends an IDNA hostname in the
*Host* field if it sends that field at all).

When receiving host names from the wire (such as in reverse name lookup), no
automatic conversion to Unicode is performed: applications wishing to present
such host names to the user should decode them to Unicode.

The module `encodings.idna` also implements the nameprep procedure, which
performs certain normalizations on host names, to achieve case-insensitivity of
international domain names, and to unify similar characters. The nameprep
functions can be used directly if desired.

encodings.idna.nameprep(*label*)[¶](https://docs.python.org/3/library/codecs.html#encodings.idna.nameprep "Link to this definition")
:   Return the nameprepped version of *label*. The implementation currently assumes
    query strings, so `AllowUnassigned` is true.

encodings.idna.ToASCII(*label*)[¶](https://docs.python.org/3/library/codecs.html#encodings.idna.ToASCII "Link to this definition")
:   Convert a label to ASCII, as specified in [**RFC 3490**](https://datatracker.ietf.org/doc/html/rfc3490.html). `UseSTD3ASCIIRules` is
    assumed to be false.

encodings.idna.ToUnicode(*label*)[¶](https://docs.python.org/3/library/codecs.html#encodings.idna.ToUnicode