from url_utils import normalize

if __name__ == "__main__":
    samples = [
        "https://Example.com:443/path///",
        "HTTP://Example.com:80/",
        "https://Example.com/a/b/../c",
    ]
    for s in samples:
        print(f"{s!r:45} -> {normalize(s)!r}")
