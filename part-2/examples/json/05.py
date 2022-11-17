import json
import datetime as dt

with open("./json/clients.json", "r", encoding="utf8") as json_file:
    data = json.load(json_file)

clients = data["clients"]
for client in clients:
    del client["address"]
    client["date"] = dt.datetime.now().strftime('%d.%m.%Y')
    
filtred = filter(lambda x: x["gender"] == "male" ,clients)
sorted =  sorted(filtred, key=lambda x: x["name"])

with open("./json/clients_updated.json", "w", encoding="utf8") as file_out:
    json.dump(sorted, file_out, ensure_ascii=False, indent=4)
