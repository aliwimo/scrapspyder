import requests

url = "https://nlp-translation.p.rapidapi.com/v1/translate"

querystring = {"text":"Hello, world!!","to":"es","from":"en"}

headers = {
	"X-RapidAPI-Key": "74328c4219mshf8d62d7be11c012p1e0250jsnf9ad32fb0a56",
	"X-RapidAPI-Host": "nlp-translation.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)