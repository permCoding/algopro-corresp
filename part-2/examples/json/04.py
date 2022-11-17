import json

with open("./json/clients.json", "r", encoding="utf8") as json_file:
    data = json.load(json_file)

clients = data["clients"]
filtred = filter(lambda x: x["gender"] == "male" ,clients)
selected = map(lambda x: { "name": x["name"], "age": x["age"]}, filtred)
sorted =  sorted(selected, key=lambda x: x["age"])

with open("./json/clients_filtred.json", "w", encoding="utf8") as file_out:
    json.dump(sorted, file_out, ensure_ascii=False, indent=4)
