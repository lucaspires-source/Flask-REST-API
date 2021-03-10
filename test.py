import requests

BASE = "HTTP://127.0.0.1:5000/"

response = requests.put(BASE + "/video",{"likes":10})
print(response.json())