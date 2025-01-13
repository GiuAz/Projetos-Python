# Biblioteca requests, é para trazer o codigo fonte (web)
import requests # type: ignore

response = requests.get("https://giuaz.github.io/NLW-SpaceTime/")

print(response.text)
