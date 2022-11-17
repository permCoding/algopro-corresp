import json

with open("./json/clients.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

clients = data["clients"]  # из json выбрать только поле clients
filtred = filter(lambda x: x["gender"] == "male" ,clients)  # отфильтровать по gender

for client in sorted(filtred, key=lambda x: x["age"]):  # сортировать по ключу age
    print(json.dumps(client, ensure_ascii=False, indent=4))
