# url-utils

Small utilities for URL parsing, normalization, and IDN handling.

## Usage

```python
from url_utils import normalize
print(normalize("https://Example.com/"))
```

## Features

- Lowercase host
- Strip default ports
- Remove trailing slashes
- IDNA encoding via idna

## Dependencies

See `requirements.txt`.