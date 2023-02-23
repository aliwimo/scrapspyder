import os
import requests
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

OUTPUT_DIR = "output/"
source_file = './output/index.html'

with open(source_file, 'r', encoding='utf-8') as file:
    source_text = file.read()

modified_html = source_text.replace("%2F", "/")
modified_html = modified_html.replace("%3A", ":")
modified_html = modified_html.replace("https://ccweb.imgix.net/https://www.classcentral.com", "")
modified_html = modified_html.replace("https://www.classcentral.com", "")
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(modified_html, 'html.parser')

# Write the updated HTML soup to a file
filename = os.path.join(OUTPUT_DIR, 'index_modified.html')
with open(filename, 'w', encoding='utf-8') as f:
    f.write(str(soup))