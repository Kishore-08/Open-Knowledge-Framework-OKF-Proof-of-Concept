---
id: apache-airflow-api-auth-https-airflow-apache-org-docs-apache-airflow-stable-b3467d3c
type: concept
title: '[[api\_auth]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id13)'
description: Settings relating to authentication on the Airflow APIs
category: apache-airflow
tags: []
source:
  name: apache-airflow
  url: https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html
updated_at: '2026-08-20'
created_at: '2026-08-20'
---

### [[api\_auth]](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#id13)

Settings relating to authentication on the Airflow APIs

#### jwt\_algorithm

> Added in version 3.0.0.

The algorithm name use when generating and validating JWT Task Identities.

This value must be appropriate for the given private key type.

If this is not specified Airflow makes some guesses as what algorithm is best based on the key type.

(“HS512” if `jwt_secret` is set, otherwise a key-type specific guess)

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__API_AUTH__JWT_ALGORITHM`

Example:
:   `"EdDSA" or "HS512"`

#### jwt\_audience

> Added in version 3.0.0.

The audience claim to use when generating and validating JWTs for the API.

This variable can be a single value, or a comma-separated string, in which case the first value is the
one that will be used when generating, and the others are accepted at validation time.

Not required, but strongly encouraged.

See also [jwt\_audience](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-execution-api-jwt-audience)

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__API_AUTH__JWT_AUDIENCE`

Example:
:   `my-unique-airflow-id`

#### jwt\_cli\_expiration\_time

> Added in version 3.0.0.

Number in seconds until the JWTs used for authentication expires for CLI commands.
When the token expires, all CLI calls using this token will fail on authentication.

Make sure that time on ALL the machines that you run airflow components on is synchronized
(for example using ntpd) otherwise you might get “forbidden” errors.

Type:
:   integer

Default:
:   `3600`

Environment Variable:
:   `AIRFLOW__API_AUTH__JWT_CLI_EXPIRATION_TIME`

#### jwt\_expiration\_time

> Added in version 3.0.0.

Number in seconds until the JWTs used for authentication expires. When the token expires,
all API calls using this token will fail on authentication.

Make sure that time on ALL the machines that you run airflow components on is synchronized
(for example using ntpd) otherwise you might get “forbidden” errors.

See also [jwt\_expiration\_time](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-execution-api-jwt-expiration-time)

Type:
:   integer

Default:
:   `86400`

Environment Variable:
:   `AIRFLOW__API_AUTH__JWT_EXPIRATION_TIME`

#### jwt\_issuer

> Added in version 3.0.0.

Issuer of the JWT. This becomes the `iss` claim of generated tokens, and is validated on incoming
requests.

Ideally this should be unique per individual airflow deployment

Not required, but strongly recommended to be set.

See also [jwt\_audience](https://airflow.apache.org/docs/apache-airflow/stable/configurations-ref.html#config-api-auth-jwt-audience)

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__API_AUTH__JWT_ISSUER`

Example:
:   `http://my-airflow.mycompany.com`

#### jwt\_kid

> Added in version 3.0.0.

The Key ID to place in header when generating JWTs. Not used in the validation path.

If this is not specified the RFC7638 thumbprint of the private key will be used.

Ignored when `jwt_secret` is used.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__API_AUTH__JWT_KID`

Example:
:   `my-key-id`

#### jwt\_leeway

> Added in version 3.0.0.

Number of seconds leeway in validating expiry time of JWTs to account for clock skew between
client and server

Type:
:   integer

Default:
:   `10`

Environment Variable:
:   `AIRFLOW__API_AUTH__JWT_LEEWAY`

#### jwt\_private\_key\_path

> Added in version 3.0.0.

The path to a file containing a PEM-encoded private key use when generating Task Identity tokens in
the executor.

Mutually exclusive with `jwt_secret`.

Type:
:   string

Default:
:   `None`

Environment Variable:
:   `AIRFLOW__API_AUTH__JWT_PRIVATE_KEY_PATH`

Example:
:   `/path/to/private_key.pem`

#### jwt\_secret

> Added in version 3.0.0.

Secret