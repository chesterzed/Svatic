import requests
import json

response = requests.get('https://zenquotes.io/api/random', timeout=10)
print(response)
if response.status_code == 200:
    data = response.json()
    print(data)
    quote_text = f"{data[0]['q']}\n\t\t- {data[0]['a']}"
    print(quote_text)
