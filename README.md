# url-utils

Small utilities for URL parsing, normalization, and IDN handling.

## Usage

```python
from url_utils import normalize

print(normalize("https://Example.com:443/path///"))
# https://example.com/path

print(normalize("https://xn--nxasmq6b.example/"))
# https://xn--nxasmq6b.example/
```

## What `normalize` does

- Lowercases the scheme and host
- IDNA-encodes international hostnames
- Strips default ports (80 for http, 443 for https)
- Removes trailing slashes (except on root `/`)

## Dependencies

See `requirements.txt`.
