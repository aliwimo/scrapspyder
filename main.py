import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_page(url, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Send a GET request to the URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find and download any assets in the HTML soup
    for tag in soup.find_all():
        if tag.name == 'img':
            # Download the image file
            src = tag.get('src')
            if src:
                src_url = urljoin(url, src)
                download_file(src_url, output_dir)
                tag['src'] = os.path.join('assets', os.path.basename(src_url))
        elif tag.name == 'link' and tag.get('rel') == ['stylesheet']:
            # Download the stylesheet file
            href = tag.get('href')
            if href:
                href_url = urljoin(url, href)
                download_file(href_url, output_dir)
                tag['href'] = os.path.join('assets', os.path.basename(href_url))
        elif tag.name == 'script':
            # Download the script file
            src = tag.get('src')
            if src:
                src_url = urljoin(url, src)
                download_file(src_url, output_dir)
                tag['src'] = os.path.join('assets', os.path.basename(src_url))

    # Write the updated HTML soup to a file
    filename = os.path.join(output_dir, 'index.html')
    with open(filename, 'w', encoding=response.encoding) as f:
        f.write(str(soup))

def download_file(url, output_dir):
    # Send a GET request to the URL
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
    response = requests.get(url, headers=headers)

    # Parse the URL to get the filename
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)

    # Write the response content to a file
    filename = os.path.join(output_dir, 'assets', filename)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'wb') as f:
        f.write(response.content)

    print(f'Downloaded: {url}')

# Example usage
download_page('https://w.livehd7.cc/m5/', 'output')
