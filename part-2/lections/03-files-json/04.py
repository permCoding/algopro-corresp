import json  # подключить библиотеку json

with open("./json/clients.json", "r", encoding="utf8") as json_file:
    data = json.load(json_file)  # загрузить json из файла в строку data

clients = data["clients"]
updated = []
for client in clients:
    del(client["address"])
    updated.append(client)
sorted = sorted(updated, key=lambda x: x["age"], reverse=True)

with open("./json/clients_u.json", "w", encoding="utf8") as f:
    json.dump(sorted, f, ensure_ascii=False, indent=4)
