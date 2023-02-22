import numpy as np
from urllib.parse import urljoin, urlparse

sources = links = np.loadtxt("./links/sources.txt", dtype="O")


new_sources = []

for source in sources:
    source = source.replace("%2F", "/")
    source = source.replace("%3A", ":")
    source = source.replace("https://ccweb.imgix.net/https://www.classcentral.com", "")
    source = source.replace("https://www.classcentral.com", "")
    source = source.lstrip("/")
    parsed_source = urlparse(source)
    if not parsed_source.netloc:
        if "?" in source:
            idx = source.index("?")
            source = source[:idx]
    new_sources.append(source)
    print(source)

np.savetxt("./links/assets_src.txt", new_sources, fmt="%s")


