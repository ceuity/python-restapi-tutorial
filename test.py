import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"name": "Titanic", "views": 1292, "likes": 134120},
    {"name": "Lion King", "views": 13753, "likes": 3423410},
    {"name": "Toy Story", "views": 92840, "likes": 175850},
]

for i in range(len(data)):
    response = requests.post(BASE + "video/" + str(i), data[i])
    print(response.json())

print("--------------------------GET------------------------------")

n = str(input())
response = requests.get(BASE + "video/" + n)
print(response.json())

print("---------------------------DELETE--------------------------")

n = str(input())
response = requests.delete(BASE + "video/" + n)
print(response.json)
print("")
for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i), data[i])
    print(response.json())

print("---------------------------UPDATE-------------------------")

n = str(input())
response = requests.put(BASE + "video/" + n, {"views": 99, "likes": 239})
print(response.json())
print("")
for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i), data[i])
    print(response.json())

print("---------------------------CREATE-------------------------")

n = str(input())
response = requests.post(BASE + "video/" + n, {"name": "Inception", "views": 12533, "likes": 38473})
print(response.json())
print("")
for i in range(len(data)):
    response = requests.get(BASE + "video/" + str(i), data[i])
    print(response.json())
