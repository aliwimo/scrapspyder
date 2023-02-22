import requests
import os
from bs4 import BeautifulSoup

def translate(text):
    target_lang = 'hi'
    # Use the MyMemory API to translate the text
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_lang}"
    response = requests.get(url).json()
    return response['responseData']['translatedText']

url = "./output/mod_index.html"


with open(url, 'r', encoding='utf-8') as file:
    source_text = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(source_text, 'html.parser')

translated = ""

tags_skip = ['script', 'noscript', 'style', 'link', 'meta']

for tag in soup.find_all():
    if tag.name in tags_skip:
        continue
    if tag.string:
        print(tag.string)
        try:
            tag.string.replace_with(translate(tag.string))
        except: 
            print("translation aborted")
translated += str(soup)


# Write the updated HTML soup to a file
filename = os.path.join("./output/", 'index_translated.html')
with open(filename, 'w', encoding="utf-8") as f:
    f.write(translated)