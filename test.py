import requests

BASE = "HTTP://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld")
print(response.json())