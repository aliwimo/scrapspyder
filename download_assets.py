import os
import requests
from urllib.parse import urljoin, urlparse
import numpy as np

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
DOMAIN = "https://www.classcentral.com/"
OUTPUT_DIR = "output/"

def download_file(url):
    parsed_url = urlparse(url)
    if not parsed_url.netloc:
        url = DOMAIN + url
    # Send a GET request to the URL
    try:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            # Write the response content to a file
            filename = os.path.join(OUTPUT_DIR, parsed_url.path)
            os.makedirs(os.path.dirname(filename), exist_ok=True)
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded: {url}')
    except:
        print(f'ERROR! {url}')

assets = np.loadtxt("links/assets.txt", dtype="O")

for asset in assets:
    download_file(asset)

assets = np.loadtxt("links/assets_src.txt", dtype="O")

for asset in assets:
    download_file(asset)
