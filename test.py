import requests

BASE = "HTTP://127.0.0.1:5000/"

data =[{"likes":10,"name":"Lucas","views":1000},
       {"likes":11230,"name":"Neymar","views":1002320},
       {"likes":1031,"name":"Boruto","views":1003230}]

for in in range(len(data)):
    response = requests.put(BASE + "video/" + str(i),data[i])
    print(response.json())
##response = requests.delete(BASE + "video/0")
##print(response)
input()
response = requests.get(BASE + "video/6")
print(response.json())
input()