import requests

# Set the text and the target language
text = 'Hello, world!'
target_lang = 'hi'

# Use the MyMemory API to translate the text
url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_lang}"
response = requests.get(url).json()
translation = response['responseData']['translatedText']

# Print the translation
print(translation)
