import json

with open("./json/clients.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

clients = data["clients"]
filtred = filter(lambda x: x["gender"] == "male" ,clients)
# исходные объекты содержат много полей
# сократим объекты, оставим только нужные поля - name и age
selected = map(lambda x: { "name": x["name"], "age": x["age"]}, filtred)

for client in sorted(selected, key=lambda x: x["age"]):
    print(json.dumps(client, ensure_ascii=False, indent=4))
