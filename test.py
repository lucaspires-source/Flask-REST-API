import requests

BASE = "HTTP://127.0.0.1:5000/"

response = requests.put(BASE + "video/1",{"likes":10,"name":"Lucas","views":1000})
print(response.json())
input()
response = requests.get(BASE + "video/1")
print(response.json())