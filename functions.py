import os
import requests
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse  import urljoin, urlparse
from configs import DOMAIN, HEADERS, OUTPUT_DIR
import shutil



class HTML_TOOLS:
    def __init__(self):
        pass

    @classmethod
    def crawl_html(cls, depth=None):
        pages = [DOMAIN]
        indexed_url = [] # a list for the main and sub-HTML websites in the main website
        for i in range(depth):
            for page in pages:
                if page not in indexed_url:
                    indexed_url.append(page)
                    try:
                        response = requests.get(page, headers=HEADERS)
                    except:
                        print( "Could not open %s" % page)
                        continue
                    soup = BeautifulSoup(response.content, features="lxml")
                    links = soup('a') #finding all the sub_links
                    for link in links:
                        if 'href' in dict(link.attrs):
                            url = urljoin(page, link['href'])
                            if url.find("'") != -1:
                                continue
                            url = url.split('#')[0] 
                            if url[0:4] == 'http':
                                indexed_url.append(url)
            pages = indexed_url
        return [*set(indexed_url)]

    @classmethod
    def check_html(cls, url):
        path = OUTPUT_DIR + urlparse(url).path.lstrip("/") + ".html"
        if Path(path).is_file():
            return True
        return False
    
    @classmethod
    def download_html(cls, url):
        if cls.external_link(url):
            print(f"External link: {url}")
            return
        if cls.check_html(url):
            print(f"File exists: {url}")
            return
        else:
            file_name, file_path = cls.extract_html(url)
            try:
                response = requests.get(url, headers=HEADERS)
                file_content = BeautifulSoup(response.content, 'html.parser')
                cls.save_html(file_name, file_path, file_content)
            except:
                print(f"Could not download: {url}")

    @classmethod
    def external_link(cls, url):
        if urlparse(url).netloc != urlparse(DOMAIN).netloc:
            return True
        return False

    @classmethod
    def extract_html(cls, url):
        parsed_url = urlparse(url)
        if not parsed_url.path or parsed_url.path == "/":
            return "index.html", ""
        modified_path = parsed_url.path.rstrip(" ")
        modified_path = modified_path.rstrip("/")
        if modified_path.startswith("/"):
            modified_path = modified_path.lstrip("/")
        dirs = modified_path.split("/")
        file_name = "index.html"
        file_path = "/".join(dirs)
        return file_name, file_path

    @classmethod
    def save_html(cls, file_name, file_path, file_content):
        file_location = OUTPUT_DIR + file_path + "/" + file_name
        if not os.path.exists(OUTPUT_DIR + file_path):
            os.makedirs(OUTPUT_DIR + file_path)
        with open(file_location, 'w', encoding="utf-8") as f:
            f.write(str(file_content))
        print(f"Page downloaded: {file_location}")

    @classmethod
    def find_html_pages(cls, directory=OUTPUT_DIR):
        html_files = []
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.endswith(".html"):
                    path = (os.path.join(root, filename)).replace("\\", "/")
                    html_files.append(path)
        return html_files

    @classmethod
    def modify_html(cls, source_file):
        with open(source_file, 'r', encoding='utf-8') as f:
            source_text = f.read()
        modified_html = source_text.replace("%2F", "/")
        modified_html = modified_html.replace("%3A", ":")
        modified_html = modified_html.replace("https://ccweb.imgix.net/https://www.classcentral.com", "")
        modified_html = modified_html.replace("https://www.classcentral.com", "")
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(modified_html, 'html.parser')
        with open(source_file, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"HTML modified: {source_file}")

def take_backup():
    source_dir = OUTPUT_DIR
    dest_dir = "website_backup/"
    shutil.copytree(OUTPUT_DIR, dest_dir)

def get_links():
    # Find and extract the content you want from the HTML soup
    links = [link.get('href') for link in soup.find_all('a')]
    print((links))

class Translate:
    
    def __init__(self):
        pass

    @classmethod
    def translate(cls, text):
        target_lang = 'hi'
        # Use the MyMemory API to translate the text
        url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_lang}"
        response = requests.get(url).json()
        return response['responseData']['translatedText']

    @classmethod
    def translate_page(cls, source_file):
        with open(source_file, 'r', encoding='utf-8') as f:
            source_text = f.read()
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(source_text, 'html.parser')
        translated = ""
        tags_skip = ['script', 'noscript', 'style', 'link', 'meta']
        print(f"Translating: {source_file}")
        for tag in soup.find_all():
            if tag.name in tags_skip:
                continue
            if tag.string:
                try:
                    tag.string.replace_with(cls.translate(tag.string))
                except: 
                    print(f"Translation aborted {source_file}")
        translated += str(soup)
        # Write the updated HTML soup to a file
        with open(source_file, 'w', encoding="utf-8") as f:
            f.write(translated)
        print(f"Translated: {source_file}")