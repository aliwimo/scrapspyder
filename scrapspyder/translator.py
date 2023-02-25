import os
import requests
from bs4 import BeautifulSoup

class Translator:

    def __init__(self, source, source_lang, target_lang, verbose=True):
        self.source = source
        self.dest = self.source
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.verbose = verbose
        self.pages = []
    
    def start(self):
        print(">>>>> Finding Pages")
        self.pages = self.find_pages()

        print(">>>>> Translating Pages")
        for page in self.pages:
            self.translate_page(page)

        print(">>>>> Done")

    def translate(self, text):
        try:
            url = f"https://api.mymemory.translated.net/get?q={text}&langpair={self.source_lang}|{self.target_lang}"
            response = requests.get(url).json()
            return response['responseData']['translatedText']
        except:
            if self.verbose:
                print(f"Could not translate!")
            return

    def find_pages(self):
        html_files = []
        for root, dirs, pages in os.walk(self.dest):
            for page in pages:
                if page.endswith(".html"):
                    path = (os.path.join(root, page)).replace("\\", "/")
                    html_files.append(path)
        return html_files

    def translate_page(self, source_file):
        source_text = self.read_local_file(source_file)
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(source_text, 'html.parser')
        translated = ""
        tags_skip = ['script', 'noscript', 'style', 'link', 'meta']
        for tag in soup.find_all():
            if tag.name in tags_skip:
                continue
            if tag.string:
                try:
                    tag.string.replace_with(self.translate(tag.string))
                except: 
                    if self.verbose:
                        print(f"Translation aborted {source_file}")
        translated += str(soup)
        
        # Write the updated HTML soup to a file
        with open(source_file, 'w', encoding="utf-8") as f:
            f.write(translated)
        
        if self.verbose:
            print(f"Translated: {source_file}")


    def read_local_file(self, source_file):
        try:
            with open(source_file, 'r', encoding='utf-8') as file:
                source_text = file.read()
            return source_text
        except:
            if self.verbose:
                print(f'File could not read: {source_file}')
            return
