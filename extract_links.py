import re
import os.path
import numpy as np
from urllib.parse import urlparse, urljoin, unquote

def extract_urls(source_file, output_file):
    with open(source_file, 'r', encoding='utf-8') as file:
        source_text = file.read()
    urls = []
    pattern = r'https?:\/\/\w.[^\'{})"<> ]+|www\.\w[^\'{})]+|\/[a-zA-Z0-9\-\/\.\@]+|assets+[\\a-zA-Z0-9\-.]+|[a-zA-Z0-9_]+\/+[a-zA-Z0-9\-\/\.\@]+'
    matches = re.findall(pattern, source_text)
    for match in matches:
        match = unquote(match).replace('%2F', '/')  # Replace %2F with /
        match = unquote(match).replace('\\', '/')  # Replace %2F with /
        urls.append(match)
    np.savetxt(output_file, urls, fmt="%s")

def strip_domain(link):
    if link.startswith("/http") or link.startswith("/www"):
        link = link.lstrip("/")
    if link.startswith("//"):
        link = link.lstrip("//")
    parsed_link = urlparse(link)
    if parsed_link.netloc == "ccweb.imgix.net" or parsed_link.netloc == "www.classcentral.com":
        link = parsed_link.path
        if link.startswith("/http"):
            link = link.lstrip("/")
            link = strip_domain(link)
    parsed_link = urlparse(link)
    # if not parsed_link.scheme and not link.startswith("www") and not link.startswith('/'):
    #     link = "/" + link 
    if link.startswith('/'):
        link = link.lstrip('/')
    return link

def clean_links(links, exceptions):
    links_cleaned = []
    for link in links:
        if not link in exceptions:
            if "?" in link:
                idx = link.index("?")
                link = link[:idx]
            # remove double // at the begining
            link = strip_domain(link)
            if not link in links_cleaned:
                links_cleaned.append(link)
    return links_cleaned

def is_asset(link):
    # Parse the URL to get the path and extension
    path = urlparse(link).path
    ext = os.path.splitext(path)[1]
    # Check if the URL has a file extension
    return True if ext else False

def classify_links(links):
    assets = []
    paths = []
    for link in links:
        if is_asset(link):
            assets.append(link)
        else:
            paths.append(link)
    return assets, paths

file_path = './output/index.html'
output_file_path = 'links/raw.txt'
extract_urls(file_path, output_file_path)

links = np.loadtxt(output_file_path, dtype="O")
exceptions = np.loadtxt('./links/exceptions.txt', dtype="O")
links_cleaned = clean_links(links, exceptions)
assets, paths = classify_links(links_cleaned)

np.savetxt("./links/assets.txt", assets, fmt="%s")
np.savetxt("./links/paths.txt", paths, fmt="%s")
