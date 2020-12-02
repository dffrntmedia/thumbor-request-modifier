# thumbor-request-modifier-http-loader

## What is it?

Custom HTTP loader for Thumbor which allows modifying client request based on certain conditions.

---

Copyright (C) 2020 Maksim Barouski

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

---

## Configuration

Install:
```
pip install thumbor-request-modifier-http-loader # or any other version
```

Set configurations in Thumbor. For example, we have to inject Authorization header when requested image is from protected API.
```sh
LOADER="'thumbor_request_modifier_http_loader.loader'"

REQUEST_MODIFIER_HTTP_LOADER_MODIFICATIONS="['mod_type', 'set_header', 'mod_header_name', 'Authorization', 'mod_header_value', 'AccessToken', 'cond_type', 'url_contains', 'cond_url_part', 'image.api.com']"

# If you set custom headers in request then you have to allow their forwarding with:
HTTP_LOADER_FORWARD_ALL_HEADERS="True"
# or
HTTP_LOADER_FORWARD_HEADERS_WHITELIST="['Authorization']"
```

## Deploy flow

1. Commit with new version in `setup.py`;
2. `make tag -e VERSION=<VERSION>`;
3) `make deploy`.

Stable version must have format:
```
<MAJOR_VERSION_NUMBER>.<MINOR_VERSION_NUMBER>
```

Version in development must have format:
```
<MAJOR_VERSION_NUMBER>.<MINOR_VERSION_NUMBER>.<BUILD_NUMBER>-dev
```
