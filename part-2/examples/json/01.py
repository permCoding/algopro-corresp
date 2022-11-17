import json  # подключить библиотеку json

with open("./json/clients.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)  # загрузить json из файла в строку data

clients = data["clients"]  # из json выбрать только поле clients
for client in clients:  # перебрать список клиентов
    # вывести клиента в виде структурированной строки с отсутпом 4 пробела
    # не экранировать символы Unicode '\u00a3' - выводить как есть '£'
    print(json.dumps(client, ensure_ascii=False, indent=4))
