import json

with open("./json/clients.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

for client in data["clients"]:
    print(json.dumps(client, ensure_ascii=False, indent=4))
