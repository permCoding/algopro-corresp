import json  # подключить библиотеку json

with open("./json/clients.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)  # загрузить json из файла в data

filtred = filter(lambda x: x["address"]["city"]!="Кунгур", data['clients'])
sorted = sorted(filtred, key=lambda x: x["age"], reverse=True)

for client in sorted:  # перебрать список клиентов
    # вывести клиента в виде структурированной строки с отсутпом 4 пробела
    # не экранировать символы Unicode '\u00a3' - выводить как есть '£'
    print(json.dumps(client, ensure_ascii=False, indent=4))
