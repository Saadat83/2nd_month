import requests

response = requests.get("https://restcountries.com/v3.1/all")
print(response.text)


