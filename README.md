# Thumbor request modifier

Thumbor HTTP loader which allows modifying the client request based on certain conditions.

## Installation

```bash
pip install thumbor-request-modifier
```

## Configuration

##### Injecting the authorization header when requested image comes from a protected API

```python
LOADER = "'thumbor_request_modifier.loader'"

HTTP_LOADER_REQUEST_MODIFIER = "[['mod_type', 'set_header', 'mod_header_name', 'Authorization', 'mod_header_value', 'AccessToken', 'cond_type', 'url_contains', 'cond_url_part', 'protected.image.api.com']]"

# Also ensure the onward forwarding of headers which can be done in two ways:

# Either indiscriminately, which may leak additional, more sensitive headers as well
HTTP_LOADER_FORWARD_ALL_HEADERS = "True"
# Or by specifying which headers may be forwarded by whitelisting them
HTTP_LOADER_FORWARD_HEADERS_WHITELIST = "['Authorization']"
```

## Deployment and versions

1. Commit changes with new version in `setup.py`;
2. `make tag -e VERSION=<VERSION>`;
3. `make deploy`.

Stable version format:

```
<MAJOR_VERSION_NUMBER>.<MINOR_VERSION_NUMBER>.<PATCH_NUMBER>
```

Version in development format:

```
<MAJOR_VERSION_NUMBER>.<MINOR_VERSION_NUMBER>.<BUILD_NUMBER>-dev
```

## Contribute

Feel free to submit additional modification and condition types.
