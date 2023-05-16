import json  # подключить библиотеку json

with open("./json/clients.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)  # загрузить json из файла data

clients = data["clients"]

# print(clients)
# print(json.dumps(clients, ensure_ascii=False, indent=4))

# for client in clients:
#     print(client["name"], client["gender"])

# for client in filter(lambda x: x['gender']=='female', clients):
#     print(client["name"], client["gender"])


# filtred = list(filter(lambda x: x['gender']=='female', clients))
# for client in sorted(filtred, key=lambda x: x['name']):
#     print(client["name"], client["gender"])

with open("./json/results.json", "w", encoding="utf8") as f:
    filtred = list(filter(lambda x: x['gender']=='female', clients))
    results = sorted(filtred, key=lambda x: x['name'])
    json.dump(results, f, ensure_ascii=False, indent=4)
