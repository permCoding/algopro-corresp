import json  # подключить библиотеку json

with open("./json/clients.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)  # загрузить json из файла в строку data

filtred = filter(lambda x: x["address"]["city"]!="Кунгур", data['clients'])
sorted = sorted(filtred, key=lambda x: x["age"], reverse=True)

for client in sorted:
    print(client)
