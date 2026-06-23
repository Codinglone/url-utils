from urllib.parse import urlsplit, urlunsplit

import idna

_DEFAULT_PORTS = {"http": 80, "https": 443}


def normalize(url):
    """Normalize a URL: lowercase host, IDNA-encode, strip default port, trim trailing slashes."""
    parts = urlsplit(url.strip())
    scheme = (parts.scheme or "").lower()

    host = parts.hostname or ""
    if host and "." in host:
        try:
            host = idna.encode(host).decode("ascii")
        except idna.IDNAError:
            pass
    host = host.lower()

    port = parts.port
    if port is None or port == _DEFAULT_PORTS.get(scheme):
        netloc = host
    else:
        netloc = f"{host}:{port}"

    path = parts.path
    if len(path) > 1:
        path = path.rstrip("/") or "/"

    return urlunsplit((scheme, netloc, path, parts.query, parts.fragment))
