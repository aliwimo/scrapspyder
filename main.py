import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from functions import prepare_path, trim_domain
import numpy as np

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
DOMAIN = "https://www.classcentral.com/"
OUTPUT_DIR = "output/"

def download_page(url):
    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Send a GET request to the URL
    response = requests.get(url, headers=HEADERS)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    sources = []
    for tag in soup.find_all():
        if tag.name == 'img':
            # Download the image file
            src = tag.get('src')
            if src:
                sources.append(src)
        elif tag.name == 'link':
            href = tag.get('href')
            if href and len(href) > 1:
                sources.append(href)
        elif tag.name == 'script':
            src = tag.get('src')
            if src:
                sources.append(src)

    print(sources)
    # Write the updated HTML soup to a file
    np.savetxt("./links/sources.txt", sources, fmt="%s")

    # # Write the updated HTML soup to a file
    # filename = os.path.join(OUTPUT_DIR, 'index.html')
    # with open(filename, 'w', encoding=response.encoding) as f:
    #     f.write(str(soup))

# Example usage
download_page(DOMAIN)
