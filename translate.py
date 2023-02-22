import requests

def translate(text):
    target_lang = 'hi'
    # Use the MyMemory API to translate the text
    url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_lang}"
    response = requests.get(url).json()
    return response['responseData']['translatedText']


# Set the text and the target language
text = 'Hello, world!'
# Print the translation
print(translate(text))
