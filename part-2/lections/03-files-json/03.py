import json  # подключить библиотеку json

with open("./json/clients.json", "r", encoding="utf8") as json_file:
    data = json.load(json_file)  # загрузить json из файла в строку data

filtred = filter(lambda x: x["address"]["city"]!="Кунгур", data['clients'])
sorted = sorted(filtred, key=lambda x: x["age"], reverse=True)

with open("./json/clients_s.json", "w", encoding="utf8") as f:
    json.dump(sorted, f, ensure_ascii=False, indent=4)
